# 🚀 AI Intern Assignment – Aeron Systems  
### File Upload Portal + CSV Plotter Utility

![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Flask](https://img.shields.io/badge/Backend-Flask-orange)
![Pandas](https://img.shields.io/badge/Data-Pandas-yellow)
![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-lightgrey)

---

## 📌 Overview

This repository contains two prototype utilities developed as part of the **AI Intern selection assignment for Aeron Systems**:

### **1️⃣ Web Utility — File Upload Portal (Flask)**  
A clean, user-friendly interface for uploading, listing, downloading, and deleting files with metadata.  
Supports: `.log`, `.pdf`, `.csv`, `.zip`.

### **2️⃣ Data Utility — CSV Plotter Tool**  
A command-line tool that loads any CSV file, lets the user select columns, and generates either line or bar plots.

---

## 🎯 Objectives

- Build a functional web portal using Python + Flask  
- Enable metadata capture along with file upload  
- Implement CRUD operations (Upload / Read / Download / Delete)  
- Build a data visualization tool using pandas + matplotlib  
- Demonstrate clean code, modular design, and professional documentation  
- Show how AI tools assisted during development  

---

# 🏗 Project Structure

```
AI-Prototyping/
│
├── web_portal/ # Flask Web App
│ ├── app.py
│ ├── uploads/
│ ├── file_index.csv # Metadata store
│ ├── templates/
│ │ ├── base.html
│ │ ├── index.html
│ │ ├── upload.html
│ │ └── list.html
│ └── static/
│ └── styles.css
│
├── csv_plotter/ # CSV Plotting Tool
│ ├── csv_plotter.py
│ ├── requirements.txt
│ └── sensor_data.csv
│
├── AI_prompts.pdf
├── screen_recording.mp4
└── README.md
```

---

# 🌐 1️⃣ Web Utility – File Upload Portal (Flask)

A modern, clean portal with:

### ✔ Upload Files (with metadata)
- File type validation  
- Avoids overwriting with timestamp renaming  
- Saves metadata to CSV  

### ✔ View Uploaded Files
- Shows filename, uploader, timestamp, description  
- Styled table with hover effects  

### ✔ Download Files

### ✔ Delete Files
- Removes file from folder  
- Updates metadata CSV  
- Confirmation popup  

---

## 🖼 UI Screenshots (Optional)

You can add screenshots here:

```
web_portal_demo/
home.png
upload.png
list.png
delete.png
```

---

# 🔧 How to Run the Web Portal

```
cd web_portal
python -m venv venv
venv\Scripts\activate # Windows
pip install -r requirements.txt
python app.py
```

Open in browser:

👉 http://127.0.0.1:5000

---

# 📊 2️⃣ Data Utility – CSV Plotter Tool

### Features:
- Load any CSV  
- Auto-display available columns  
- Choose X and Y columns  
- Select plot type ("line" or "bar")  
- Show plot  
- Optionally save to PNG  

---

## 🔧 How to Run the CSV Plotter

```
cd csv_plotter
..\web_portal\venv\Scripts\activate # activate the same venv
pip install -r requirements.txt
python csv_plotter.py --file sensor_data.csv
```

---

## 📄 Sample IoT Dataset Included

`sensor_data.csv` includes:

- Timestamp  
- Temperature  
- Humidity  
- Vibration  
- Battery voltage  
- Pressure  

Useful for telemetry and industrial IoT use cases.

---

# 🧱 Tech Stack

| Component        | Technology        |
|------------------|-------------------|
| Backend          | Flask (Python)    |
| Frontend         | HTML, CSS (custom)|
| Data Processing  | Pandas            |
| Visualization    | Matplotlib        |
| Storage          | Local filesystem + CSV |
| Environment      | Python 3.10+      |

---

# 🔍 System Architecture

### Web Portal
```
User → Flask → Validation → Save File → Metadata CSV → UI Display → Download/Delete
```

### CSV Plotter
```
CSV → Pandas → Column Selection → Matplotlib → Graph Output/PNG File
```

---

# 🤖 Use of AI Tools

AI tools were used to accelerate development while maintaining quality.

### ✔ ChatGPT Used For:
- Generating Flask route templates  
- Designing HTML templates  
- Writing modern CSS  
- Structuring CLI argument parsing  
- Improving metadata CSV logic  
- Creating README.md  

### ✔ Manual Enhancements Done By Developer:
- Timestamp-based filename collision handling  
- Delete functionality addition  
- Styling improvements & layout polish  
- IoT sensor dataset creation  
- Error handling  
- Secure file handling  
- Project structure cleanup  

---

# 🎥 Video Demonstration

A 5–7 minute screen recording (`screen_recording.mp4`) shows:

- Running Flask app  
- Uploading, listing, downloading, deleting files  
- Running the CSV Plotter  
- Showing AI_prompts.pdf  
- Code walkthrough  

---

# 🏁 Conclusion

This assignment demonstrates:

- Web application development  
- File handling & metadata management  
- Data visualization & CLI tooling  
- Professional documentation  
- Clean code best practices  
- Effective use of AI for productivity  

---

# 🙋‍♂️ Developer

**Hasitha Reddy**  
B.Tech – AIML  
Email: hasitha.eppalapalli.btech2022@sitpune.edu.in 

