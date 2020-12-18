import json
import os.path

def save_rules(rules):
    rules_file = "rules.json"
    with open(rules_file, "w+") as f:
        json.dump(rules, f)

def load_rules():
    rules_file = "rules.json"
    if os.path.isfile(rules_file):
        with open(rules_file, "r+") as f:
            return json.load(f)
    else:
        return []


save_rules([1,2,3,4])
data_list = load_rules()

print(data)
