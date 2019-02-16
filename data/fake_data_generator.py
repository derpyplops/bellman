import json
import random
import copy


def generate_topic(cur_year, max_year):
    topics = {
            "healthcare": {
                "initial": 9,
                "last": 41
                },
            "cyber-security": {
                "initial": 0,
                "last": 19
                },
            "housing": {
                "initial": 53,
                "last": 34
                },
            "savings": {
                "initial": 11,
                "last": 20
                },
            "reserves": {
                "initial": 5,
                "last": 13
                },
            "welfare": {
                "initial": 14,
                "last": 11
                },
            "education": {
                "initial": 36,
                "last": 45
                },
            "law": {
                "initial": 27,
                "last": 38
                }
            }
    choose_from_list = []
    for topic in topics:
        if cur_year == 0:
            expected = topics[topic]["initial"]
        elif cur_year == max_year:
            expected = topics[topic]["last"]
        else:
            initial = topics[topic]["initial"]
            last = topics[topic]["last"]
            expected = (last - initial)/2.0 + random.normalvariate(0, 5)
            expected = abs(int(expected))
        choose_from_list += [topic] * expected
    return random.choice(choose_from_list)


schema_raw = open("proposed_schema_v1.json", "r").read()
schema_json = json.loads(schema_raw)


generated = []
example = schema_json[0]
# 50 years of data, at ~365 reports
for i in range(50):
    for _ in range(365):
        topic = generate_topic(i, 49)
        print(topic)
        example_copy = copy.deepcopy(example)
        example_copy["topic"] = topic
        generated.append(example_copy)

open("fake_data.json", "w").write(
        json.dumps(generated)
        )
