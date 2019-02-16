import json
import csv


# Turn reports into line graph friendly data
# where each record is a count of topics covered
# on a day


SOURCE_PATH = "../pipeline_00/fake_data_all.json"
OUTPUT_PATH = "longitudinal.json"


reports_raw = open(SOURCE_PATH, "r").read()
reports = json.loads(reports_raw)


counter = {}
for report in reports:
    year = int(report["date"].split("-")[-1])
    decade = year/10*10
    topic = report["topic"]
    if topic not in counter:
        counter[topic] = {
                1950: 0,
                1960: 0,
                1970: 0,
                1980: 0,
                1990: 0,
                2000: 0,
                2010: 0
                }
    counter[topic][decade] += 1


output = []
for topic in counter:
    data = [
            counter[topic][1950],
            counter[topic][1960],
            counter[topic][1970],
            counter[topic][1980],
            counter[topic][1990],
            counter[topic][2000],
            counter[topic][2010]
            ]
    output.append({
        "label": topic,
        "data": data,
        })

open(OUTPUT_PATH, "w").write(
        json.dumps(output)
        )
