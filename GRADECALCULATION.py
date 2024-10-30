def calculate_weighted_average(grades):
    weights = {
        "homework": 0.4,
        "midterm": 0.3,
        "final": 0.2,
        "participation": 0.1
    }
    
    weighted_sum = (
        sum(grades["homework"]) / len(grades["homework"]) * weights["homework"] +
        grades["midterm"] * weights["midterm"] +
        grades["final"] * weights["final"] +
        grades["participation"] * weights["participation"]
    )
    
    return weighted_sum

def calculate_unweighted_average(grades):
    total_sum = sum(grades["homework"]) + grades["midterm"] + grades["final"] + grades["participation"]
    total_assignments = len(grades["homework"]) + 3
    unweighted_average = total_sum / total_assignments
    
    return unweighted_average

def main():
    grades_list = []

    for i in range(1, 6):
        score, total = map(int, input(f"Enter the score and total for Homework #{i}: ").split())
        grades_list.append((score, total))

    score, total = map(int, input("Enter the score and total for Midterm: ").split())
    grades_list.append((score, total))

    score, total = map(int, input("Enter the score and total for Final: ").split())
    grades_list.append((score, total))

    score, total = map(int, input("Enter the score and total for Participation: ").split())
    grades_list.append((score, total))

    percentages = [score / total for score, total in grades_list]

    grades = {
        "homework": percentages[:5],
        "midterm": percentages[5],
        "final": percentages[6],
        "participation": percentages[7]
    }

    weighted_average = calculate_weighted_average(grades)
    unweighted_average = calculate_unweighted_average(grades)

    print(f"\nWeighted Average: {weighted_average * 100:.2f}%")
    print(f"Unweighted Average: {unweighted_average * 100:.2f}%")

if __name__ == "__main__":
    main()