import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def get_valid_mark(subject_name):
    while True:
        try:
            mark = float(input(f"Enter marks for {subject_name}: "))
            if 0 <= mark <= 100:
                return mark
            print("Invalid input. Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def get_grade(average_mark):
    if average_mark >= 90:
        return "A+"
    elif average_mark >= 80:
        return "A"
    elif average_mark >= 70:
        return "B"
    elif average_mark >= 60:
        return "C"
    elif average_mark >= 50:
        return "D"
    else:
        return "F"


def get_performance(average_mark):
    if average_mark >= 80:
        return "Distinction"
    elif average_mark >= 60:
        return "Pass"
    else:
        return "Needs Improvement"


def calculate_summary(marks):
    marks_array = np.array(marks, dtype=float)
    average_mark = float(np.mean(marks_array))
    final_grade = get_grade(average_mark)
    performance = get_performance(average_mark)
    return {
        "average_mark": average_mark,
        "grade": final_grade,
        "performance": performance,
    }


def plot_marks(subjects, marks, output_path="marks_chart.png"):
    df = pd.DataFrame({"Subject": subjects, "Marks": marks})
    plt.figure(figsize=(10, 6))
    plt.bar(df["Subject"], df["Marks"], color=["#4CAF50", "#2196F3", "#FF9800", "#9C27B0", "#F44336"])
    plt.title("Subject-wise Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.ylim(0, 100)
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def main():
    print("====================================")
    print("Welcome to the Marks/Grade Predictor")
    print("====================================")

    while True:
        try:
            num_subjects = int(input("Enter the number of subjects: "))
            if num_subjects > 0:
                break
            print("Number of subjects must be greater than 0.")
        except ValueError:
            print("Please enter a valid integer.")

    subjects = []
    marks = []

    for i in range(1, num_subjects + 1):
        subject_name = f"Subject {i}"
        subjects.append(subject_name)
        marks.append(get_valid_mark(subject_name))

    summary = calculate_summary(marks)
    average_mark = summary["average_mark"]
    final_grade = summary["grade"]
    performance = summary["performance"]

    print("\nResults:")
    print("-" * 30)
    print(f"Average Mark: {average_mark:.2f}")
    print(f"Final Grade: {final_grade}")

    print(f"Performance: {performance}")

    df = pd.DataFrame({"Subject": subjects, "Marks": marks})
    print("\nSubject-wise Summary:")
    print(df.to_string(index=False))

    plot_marks(subjects, marks)
    print("\nChart saved as marks_chart.png")


if __name__ == "__main__":
    main()
