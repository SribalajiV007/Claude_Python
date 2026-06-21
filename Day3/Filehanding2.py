#Real Example -- Saving customer complaints
# with open("d:/Claude_Python/Day3/complaints.txt", "w") as file:
#     file.write("Complaint List\n")

def save_complaint(customer_name,complaint):
    with open("d:/Claude_Python/Day3/complaints.txt", "a") as file:
        file.write(f"{customer_name}: {complaint}\n")

def read_complaints():
    with open("d:/Claude_Python/Day3/complaints.txt","r") as file:
        for line in file:
            print(line.strip())

save_complaint("Sri", "My bill is too high")
save_complaint("Raj", "Internet is slow")
save_complaint("Priya", "Network issue")

print("---All Complaints---")
read_complaints()


# Practice problem

def save_student(name, marks):
    with open("d:/Claude_Python/Day3/students.txt", "a") as file:  # ✅ append
        file.write(f"{name}: {marks}\n")

def read_students():
    with open("d:/Claude_Python/Day3/students.txt", "r") as file:  # ✅ correct file
        for line in file:
            print(line.strip())

def find_topper():
    topper_name = ""
    topper_marks = 0
    with open("d:/Claude_Python/Day3/students.txt", "r") as file:  # ✅ correct file
        for line in file:
            parts = line.strip().split(":")
            name = parts[0].strip()
            marks = int(parts[1].strip())

            if marks > topper_marks:
                topper_marks = marks
                topper_name = name

    print(f"Topper: {topper_name} with {topper_marks} marks")

save_student("Sri", 88)
save_student("Raj", 76)
save_student("Priya", 92)

print("---- All Students ----")
read_students()
find_topper()