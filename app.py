from flask import Flask, render_template, request, send_file
import csv
import os
from scraper import get_prices

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        references = request.form.get("references").split("\n")
        references = [ref.strip() for ref in references if ref.strip()]
        results = get_prices(references)

    return render_template("index.html", results=results)

@app.route("/export")
def export():
    filepath = "export.csv"
    with open(filepath, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Référence", "Agrizone", "Prodealcenter", "Agrifournitures"])
        for row in request.args.getlist("data"):
            writer.writerow(row.split(","))

    return send_file(filepath, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
