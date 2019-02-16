import json


# Turn reports into line graph friendly data
# where each record is a count of topics covered
# on a day


SOURCE_PATH = "../pipeline_00/fake_data_all.json"
OUTPUT_PATH = "longitudinal.json"


reports_raw = open(SOURCE_PATH, "r").read()
reports = json.loads(reports_raw)


counter = {}
for report in reports:
    counter_id = "{}..{}".format(
            report["date"],
            report["topic"]
            )
    if counter_id not in counter:
        counter[counter_id] = 0
    counter[counter_id] += 1


output = []
for counter_id in counter:
    (date, topic) = counter_id.split("..")
    output.append({
        "date": date,
        "topic": topic,
        "count": counter[counter_id]
        })


open(OUTPUT_PATH, "w").write(
        json.dumps(output)
        )
