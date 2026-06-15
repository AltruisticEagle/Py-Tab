import csv

def breaking(open_breaking):
    with open("team_standings.csv", "r") as file:
        reader = csv.DictReader(file)
        teams = list(reader)
        ranked_teams = sorted(teams,
        key=lambda row: (int(row["points"]), int(row["total_speaker_score"])), reverse=True)

    with open("open_breaks.csv", "w", newline="") as file:
        fieldnames = ["team", "points", "total_speaker_score"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for _ in range(min(open_breaking, len(ranked_teams))):
            writer.writerow(ranked_teams[0])
            ranked_teams.pop(0)
        
    with open("open_breaks.csv", "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        open_breaks = []
        for i in range(len(rows)):
            open_breaks.append([i + 1, rows[i]["team"], rows[i]["points"], rows[i]["total_speaker_score"]])
    
    return open_breaks