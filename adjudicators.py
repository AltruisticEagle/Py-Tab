import checks
import csv
from reader import read_csv

def check_create_adjudicators(adjudicator_name):
    matches1 = checks.checks(adjudicator_name, "name") 
    if matches1 == None:
        raise ValueError("\nInvalid adjudicator name, try again")
        
def check_adjudicator_feedback(round_number, scorer_type, scorer_name, score):
    round_number = str(round_number)
    matches1 = checks.checks(round_number, "round")
    matches2 = checks.checks(scorer_type, "status_check") 
    matches3 = checks.checks(scorer_name, "name")
    matches4 = checks.checks(score, "adjudicator_feedback_score")
    matches = [matches1, matches2, matches3, matches4]
    for i in matches:
        if i == None:
            raise ValueError("\nInvalid adjudicator feedback, try again")

def check_adjudicator_already_exists(adjudicator_name):
    rows = read_csv("adjudicators.csv")
    for row in rows:
        if adjudicator_name == row["adjudicator_name"]:
            raise ValueError("\nAdjudicator already exists, try again and input a new adjudicator")

def create_adjudicators(adjudicator_name): 
    check_create_adjudicators(adjudicator_name)
    check_adjudicator_already_exists(adjudicator_name)

    with open("adjudicators.csv", "a", newline="") as file:
        fieldnames = ["adjudicator_name"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
    
        row = {"adjudicator_name": adjudicator_name}
        writer.writerow(row)

def delete_adjudicators(adjudicator_modify):
    rows = read_csv("adjudicators.csv")
    with open("adjudicators.csv", "w", newline="") as file:
        fieldnames = ["adjudicator_name"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            if row["adjudicator_name"] == adjudicator_modify:
                continue
            writer.writerow(row)

#adjudicator feedback section
def create_adjudicator_feedback(adjudicator_name, round_number, scorer_type, scorer_name, score):
    check_adjudicator_feedback(round_number, scorer_type, scorer_name, score)

    with open("adjudicator_feedback.csv", "a", newline="") as file:
        fieldnames = ["adjudicator_name", "round", "scorer_type", "scorer_name", "score"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        row = {"adjudicator_name": adjudicator_name, "round": round_number, "scorer_type": scorer_type, "scorer_name": scorer_name, "score": score}
        writer.writerow(row)

def modify_adjudicator_feedback(adjudicator_feedback_modify, round_number, scorer_name, score):
    scorer_type = "adjudicator"
    check_adjudicator_feedback(round_number, scorer_type, scorer_name, score)

    rows = read_csv("adjudicator_feedback.csv")
    with open("adjudicator_feedback.csv", "w", newline="") as file:
        fieldnames = ["adjudicator_name","round","scorer_type","scorer_name","score"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            if row["adjudicator_name"] == adjudicator_feedback_modify:
                if row["scorer_name"] == scorer_name:
                    if row["score"] == str(score):
                        if row["round"] == str(round_number):
                            continue

            writer.writerow(row)

def view_adjudicator_feedback(adjudicator_name):
    if checks.checks(adjudicator_name, "name") == None:
        raise ValueError("\nThis isn't a name, try again")
    
    rows = read_csv("adjudicator_feedback.csv")
    table = []
    found = 0
    for row in rows:
        if row["adjudicator_name"].lower() == adjudicator_name.lower():
            print(row["adjudicator_name"])
            found = found + 1
            table.append([row["round"], row["scorer_name"], row["scorer_type"], row["score"]])
            
    if found == 0:
        raise ValueError("The inputted adjudicator does not exist")
    
    return table