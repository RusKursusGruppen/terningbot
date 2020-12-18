import json
import os.path

def save_rules(rules):
    rules_file = "rules.json"
    with open(rules_file, "w+") as f:
        json.dump(rules, f)

def load_rules(new_game=False):
    rules_file = "rules.json"
    if os.path.isfile(rules_file) and (not new_game):
        with open(rules_file, "r") as f:
            return json.load(f)
    else:
        rules = [""]*20
        rules[0] = "Tag 1 bunder!"
        rules[1] = "Tag 1/2 bunder!"
        rules[10] = "Lav en ny regel"
        rules[18] = "Giv 1/2 bunder!"
        rules[19] = "Giv 1 bunder!"
        return rules
