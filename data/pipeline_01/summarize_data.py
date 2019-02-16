import json
import csv


# Turn reports into line graph friendly data
# where each record is a count of topics covered
# on a day


SOURCE_PATH = "../pipeline_00/fake_data_all.json"
OUTPUT_PATH = "longitudinal.csv"


reports_raw = open(SOURCE_PATH, "r").read()
reports = json.loads(reports_raw)


counter = {}
for report in reports:
    year = report["date"].split("-")[-1]
    topic = report["topic"]
    if year not in counter:
        counter[year] = {
                "year": year,
                "healthcare": 0,
                "cyber-security": 0,
                "housing": 0,
                "savings": 0,
                "reserves": 0,
                "welfare": 0,
                "education": 0,
                "law": 0
                }
    counter[year][topic] += 1

with open(OUTPUT_PATH, "w") as csvfile:
    fieldnames = [
            "year",
            "healthcare",
            "cyber-security",
            "housing",
            "savings",
            "reserves",
            "welfare",
            "education",
            "law"
            ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for year in counter:
        writer.writerow(counter[year])
