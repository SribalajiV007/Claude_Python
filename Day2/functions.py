def greet():
    print("Hello Sri!")

greet()
greet()


def greet(name):
    print(f"Hello {name}!")

#name = input("Enter your name: ") 
#greet(name)

def add(a,b):
    return a + b

result = add(10,5)
print(result) #15

# ^Functions with default values:

def greet(name, message = "Good morning"):
    print(f"{message}, {name}!")

greet("Sri")
greet("Raj", "Good Night")

# ^Grade Calculator using function

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks > 50:
        return "C"
    else:
        return "Fail"
    
students = [88, 92, 45, 67, 78]

for mark in students:
    grade = calculate_grade(mark)
    print(f"Marks: {mark} -> Grade: {grade}")


#Function exercise

marks = [78, 92, 45, 88, 61]
def is_even(mark):
    if mark % 2 == 0:
        return True
    else:
        return False
    
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def find_largest(mar):
    return max(mar)

print(is_even(88))              
print(is_even(45))              
print(calculate_average(marks)) 
print(find_largest(marks))
