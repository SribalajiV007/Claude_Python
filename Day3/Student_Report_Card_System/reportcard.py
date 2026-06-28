# Mini Project 1 — Student Report Card System

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "Fail"

def generate_report(students):
    try:
        for name, marks in students.items():
            average = sum(marks.values()) / len(marks)
            grade = calculate_grade(average)

            print(f"\n---- {name} ----")
            print(
                f"Maths: {marks['maths']} | "
                f"Science: {marks['science']} | "
                f"English: {marks['english']}"
            )
            print(f"Average: {average:.2f} | Grade: {grade}")

    except Exception as e:
        print("Error generating report:", e)

def find_topper(students):
    try:
        topper = ""
        highest_average = 0

        for name, marks in students.items():
            average = sum(marks.values()) / len(marks)
            if average > highest_average:
                highest_average = average
                topper = name

        # ✅ outside the loop
        print(f"\nClass Topper: {topper} with average {highest_average:.2f}")

    except Exception as e:
        print("Error finding topper:", e)

def save_report(students):
    try:
        with open("report_card.txt", "w") as file:
            for name, marks in students.items():  # ✅ loop added
                average = sum(marks.values()) / len(marks)
                grade = calculate_grade(average)

                file.write(f"---- {name} ----\n")
                file.write(
                    f"Maths: {marks['maths']} | "
                    f"Science: {marks['science']} | "
                    f"English: {marks['english']}\n"
                )
                file.write(f"Average: {average:.2f} | Grade: {grade}\n\n")

        print("\nReport saved successfully in 'report_card.txt'")

    except Exception as e:
        print("Error saving report:", e)


# --- Data ---
students = {
    "Sri":   {"maths": 88, "science": 92, "english": 78},
    "Raj":   {"maths": 65, "science": 70, "english": 60},
    "Priya": {"maths": 95, "science": 89, "english": 97},
    "Arjun": {"maths": 45, "science": 55, "english": 50}
}

# --- Run ---
generate_report(students)
find_topper(students)
save_report(students)