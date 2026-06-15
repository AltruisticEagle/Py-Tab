import csv
import teams

class T:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def w(self):
        with open("teams.csv", "a") as f:
            writer = csv.DictWriter(f, fieldnames=["team_name", "member_1", "member_1_junior_status", "member_2", "member_2_junior_status", "junior_status"])
            writer.writerow({"team_name": f"{self.a} and {self.c}", "member_1": self.a, "member_1_junior_status": self.b, "member_2": self.c, "member_2_junior_status": self.d, "junior_status": "Yes" if self.b.lower() == "y" or self.d.lower() == "y" else "No"})
    
    def m(self):
        ...
            
def main():
    p = input_team()
    t = T(p[0], p[1], p[2], p[3])
    t.w()
    t.m()

def input_team():
    return (input("Enter the name of member 1: "), input("Is member 1 a junior? (y/n): "), input("Enter the name of member 2: "), input("Is member 2 a junior? (y/n): "))


class Team:
    def __init__(self, team_name, member_1, member_1_junior_status, member_2, member_2_junior_status):
        self.team_name = team_name
        self.member_1 = member_1
        self.member_1_junior_status = member_1_junior_status
        self.member_2 = member_2
        self.member_2_juunior_status = member_2_junior_status
    
    def create_teams(self):
        teams.check_team(self.team_name)
        teams.create_team_check(self.team_name, self.member_1, self.member_2, )
        ...

    def modify_teams(self, modify_parameter, modify_to):
        teams.modify_team_check(modify_parameter, modify_to)
        self.modify_teams(modify_parameter, modify_to)

    def delete_teams(self):
        ...