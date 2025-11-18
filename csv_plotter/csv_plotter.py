# csv_plotter/csv_plotter.py
"""
Usage:
  python csv_plotter.py --file data.csv --x "col_x" --y "col_y" --kind line --save output.png
If no x/y specified, the script prints column names and prompts user.
"""
import argparse
import sys
import pandas as pd
import matplotlib.pyplot as plt

def parse_args():
    parser = argparse.ArgumentParser(description="CSV Plotter — choose X and Y columns and plot")
    parser.add_argument("--file", "-f", required=True, help="Path to CSV file")
    parser.add_argument("--x", help="Column name for x axis")
    parser.add_argument("--y", help="Column name for y axis")
    parser.add_argument("--kind", choices=["line", "bar"], default="line", help="Plot type")
    parser.add_argument("--save", help="Save plot to file (e.g. out.png)")
    return parser.parse_args()

def main():
    args = parse_args()
    df = pd.read_csv(args.file)
    print(f"Loaded CSV with columns: {list(df.columns)}")
    xcol = args.x
    ycol = args.y
    if not xcol:
        xcol = input("Enter X column name: ").strip()
    if not ycol:
        ycol = input("Enter Y column name: ").strip()
    if xcol not in df.columns or ycol not in df.columns:
        print("Error: provided column names not found in CSV.")
        sys.exit(1)
    x = df[xcol]
    y = df[ycol]
    plt.figure(figsize=(8,4))
    if args.kind == "line":
        plt.plot(x, y)
    else:
        plt.bar(x, y)
    plt.xlabel(xcol)
    plt.ylabel(ycol)
    plt.title(f"{args.kind.capitalize()} plot of {ycol} vs {xcol}")
    plt.tight_layout()
    if args.save:
        plt.savefig(args.save)
        print(f"Saved plot to {args.save}")
    else:
        plt.show()

if __name__ == "__main__":
    main()
