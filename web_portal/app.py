# web_portal/app.py
import os
from datetime import datetime
from flask import Flask, request, redirect, url_for, render_template, send_from_directory, flash

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
ALLOWED_EXTENSIONS = {"log", "pdf", "csv", "zip"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "replace-with-a-secure-random-string"

# simple metadata store (file-based). For a prototype this is enough.
METADATA_FILE = os.path.join(BASE_DIR, "file_index.csv")

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def save_metadata(filename, uploader, log_datetime, description):
    header = "filename,uploader,log_datetime,description,uploaded_at\n"
    if not os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, "w", encoding="utf-8") as f:
            f.write(header)
    uploaded_at = datetime.utcnow().isoformat()
    line = f'"{filename}","{uploader}","{log_datetime}","{description}","{uploaded_at}"\n'
    with open(METADATA_FILE, "a", encoding="utf-8") as f:
        f.write(line)

def read_metadata():
    records = []
    if not os.path.exists(METADATA_FILE):
        return records
    with open(METADATA_FILE, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    if len(lines) <= 1:
        return records
    for row in lines[1:]:
        parts = []
        # naive CSV parsing for prototype: split by '","' after stripping leading/trailing quotes
        r = row.strip()
        if r.startswith('"') and r.endswith('"'):
            r = r[1:-1]
        parts = r.split('","')
        if len(parts) >= 5:
            records.append({
                "filename": parts[0],
                "uploader": parts[1],
                "log_datetime": parts[2],
                "description": parts[3],
                "uploaded_at": parts[4]
            })
    return records

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if 'file' not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files['file']
        uploader = request.form.get("uploader", "anonymous")
        log_datetime = request.form.get("log_datetime", "")
        description = request.form.get("description", "")
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file.filename
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            # if file exists, append timestamp to avoid overwrite
            if os.path.exists(save_path):
                name, ext = os.path.splitext(filename)
                filename = f"{name}_{int(datetime.utcnow().timestamp())}{ext}"
                save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(save_path)
            save_metadata(filename, uploader, log_datetime, description)
            return render_template("upload.html", success=True, filename=filename)
        else:
            flash("Invalid file type. Allowed: " + ", ".join(ALLOWED_EXTENSIONS))
            return redirect(request.url)
    return render_template("upload.html", success=False)

@app.route("/files")
def list_files():
    records = read_metadata()
    return render_template("list.html", files=records)

@app.route("/download/<path:filename>")
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

@app.route("/delete/<path:filename>", methods=["GET"])
def delete_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Remove file from disk
    if os.path.exists(file_path):
        os.remove(file_path)

    # Remove metadata from CSV
    if os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        header = lines[0]
        updated = [header]
        
        for line in lines[1:]:
            if not line.startswith(f"\"{filename}\""):
                updated.append(line)

        with open(METADATA_FILE, "w", encoding="utf-8") as f:
            f.writelines(updated)

    flash(f"File '{filename}' deleted successfully.")
    return redirect(url_for("list_files"))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
