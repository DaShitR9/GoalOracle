import math

def poisson(k, lamb):
    return (math.exp(-lamb) * (lamb ** k)) / math.factorial(k)

def predict_scores(lambda_a, lambda_b, max_goals=5):
    print("\n📊 Score Probabilities (Team A vs Team B):\n")
    highest_prob = 0
    best_score = (0, 0)

    for i in range(max_goals + 1):
        for j in range(max_goals + 1):
            prob = poisson(i, lambda_a) * poisson(j, lambda_b)
            print(f"{i}-{j}: {prob*100:.2f}%")
            if prob > highest_prob:
                highest_prob = prob
                best_score = (i, j)

    print(f"\n✅ Most Probable Scoreline: {best_score[0]}-{best_score[1]} with {highest_prob*100:.2f}% chance\n")

def display_team_stats(team_name, stats):
    print(f"\n📈 {team_name} - Per 90 Metrics:")
    print(f"Goals Scored:     {stats['goals_scored']}")
    print(f"Goals Conceded:   {stats['goals_conceded']}")
    print(f"Shots on Target:  {stats['shots_on_target']}")
    print(f"Chances Created:  {stats['chances_created']}")
    print(f"Possession:       {stats['possession']}%")
    print(f"Pass Completion:  {stats['pass_completion']}%\n")

# -----------------------
# MAIN PROGRAM
# -----------------------

print("⚽ Football Match Score Predictor (No Libraries)")

# Team A inputs
print("\n🔴 Enter stats for Team A:")
lambda_a = float(input("Average goals scored per 90: "))
goals_conceded_a = float(input("Average goals conceded per 90: "))
shots_a = int(input("Shots on target per 90: "))
chances_a = int(input("Chances created per 90: "))
possession_a = float(input("Possession (%): "))
pass_completion_a = float(input("Pass completion (%): "))

# Team B inputs
print("\n🔵 Enter stats for Team B:")
lambda_b = float(input("Average goals scored per 90: "))
goals_conceded_b = float(input("Average goals conceded per 90: "))
shots_b = int(input("Shots on target per 90: "))
chances_b = int(input("Chances created per 90: "))
possession_b = float(input("Possession (%): "))
pass_completion_b = float(input("Pass completion (%): "))

# Store stats
team_a_stats = {
    "goals_scored": lambda_a,
    "goals_conceded": goals_conceded_a,
    "shots_on_target": shots_a,
    "chances_created": chances_a,
    "possession": possession_a,
    "pass_completion": pass_completion_a
}

team_b_stats = {
    "goals_scored": lambda_b,
    "goals_conceded": goals_conceded_b,
    "shots_on_target": shots_b,
    "chances_created": chances_b,
    "possession": possession_b,
    "pass_completion": pass_completion_b
}

# Display stats
display_team_stats("Team A", team_a_stats)
display_team_stats("Team B", team_b_stats)

# Predict score probabilities
predict_scores(lambda_a, lambda_b)
