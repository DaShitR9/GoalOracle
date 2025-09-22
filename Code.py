import math

# ========================
# 📥 Input Functions
# ========================

def get_team_stats(team_name):
    print(f"\n🔴 Enter stats for {team_name}:")
    return {
        "goals_scored": float(input("  Average goals scored per 90: ")),
        "goals_conceded": float(input("  Average goals conceded per 90: ")),
        "shots_on_target": int(input("  Shots on target per 90: ")),
        "chances_created": int(input("  Chances created per 90: ")),
        "possession": float(input("  Possession (%): ")),
        "pass_completion": float(input("  Pass completion (%): "))
    }

# ========================
# 📊 Display Functions
# ========================

def display_team_stats(team_name, stats):
    print(f"\n📊 ─── {team_name.upper()} STATS ───")
    for key, value in stats.items():
        label = key.replace("_", " ").title()
        suffix = "%" if "percent" in key or "possession" in key else ""
        print(f"🔹 {label:<20}: {value}{suffix}")

def display_score_probabilities(score_probs):
    print("\n📈 ─── SCORELINE PROBABILITIES ───")
    print("🧮 Format: Team A - Team B\n")
    print(f"{'Scoreline':<10} {'Probability':>12}")
    print("-" * 24)
    for (a, b), prob in sorted(score_probs.items(), key=lambda x: -x[1])[:10]:  # Top 10
        print(f"{a}-{b:<7} {prob*100:>10.2f}%")

def display_outcome_probabilities(win_a, draw, win_b):
    print("\n🔮 ─── MATCH OUTCOME ───")
    print(f"🏆 Team A Win: {win_a*100:.2f}%")
    print(f"🤝 Draw:       {draw*100:.2f}%")
    print(f"⚔️ Team B Win: {win_b*100:.2f}%")

# ========================
# 🔢 Poisson Function
# ========================

def poisson_probability(k, lambd):
    return (lambd ** k) * math.exp(-lambd) / math.factorial(k)

# ========================
# 📈 Score & Outcome Prediction
# ========================

def predict_score_probabilities(lambda_a, lambda_b, max_goals=5):
    score_probs = {}
    for goals_a in range(max_goals + 1):
        for goals_b in range(max_goals + 1):
            prob = poisson_probability(goals_a, lambda_a) * poisson_probability(goals_b, lambda_b)
            score_probs[(goals_a, goals_b)] = prob
    return score_probs

def calculate_outcomes(score_probs):
    win_a = sum(prob for (a, b), prob in score_probs.items() if a > b)
    draw = sum(prob for (a, b), prob in score_probs.items() if a == b)
    win_b = sum(prob for (a, b), prob in score_probs.items() if a < b)
    return win_a, draw, win_b

# ========================
# 🚀 Main Function
# ========================

def main():
    print("\n⚽ WELCOME TO GOALORACLE DELUXE ⚽")
    print("✨ Predict match outcomes with style and stats ✨")

    team_a = get_team_stats("Team A")
    team_b = get_team_stats("Team B")

    display_team_stats("Team A", team_a)
    display_team_stats("Team B", team_b)

    lambda_a = team_a["goals_scored"]
    lambda_b = team_b["goals_scored"]

    score_probs = predict_score_probabilities(lambda_a, lambda_b)
    display_score_probabilities(score_probs)

    win_a, draw, win_b = calculate_outcomes(score_probs)
    display_outcome_probabilities(win_a, draw, win_b)

# Run it
if __name__ == "__main__":
    main()
