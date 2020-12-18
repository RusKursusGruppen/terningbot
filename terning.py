import json
import os.path

def save_rules(rules, rules_id):
    rules_file = "rules" + str(rules_id) + ".json"
    with open(rules_file, "w+") as f:
        json.dump(rules, f)

def load_rules(rules_id, new_game=False):
    rules_file = "rules" + str(rules_id) + ".json"
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

def pretty_rules(rules, rules_id):
    title = "Terning Rules - Rules-ID=" + str(rules_id) + " - \n"
    sep_line = ("#"*len(title)) + "\n"
    str_rules = ""
    for i in range(len(rules)):
        str_rules += "Rule " + str(i+1) + ": " + rules[i] + "\n"
    return title + sep_line + str_rules
