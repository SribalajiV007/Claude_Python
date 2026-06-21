#Handling exception
try:
    number = int("hello")
except ValueError:
    print("That's not a valid number!")

#Real Example

#ValueError:
try:
    age = int(input("Enter age: "))
    print(f"You age is {age}")
except ValueError:
    print("Please enter a valid number!")

#ZeroDivision Error
try:
    result = 10/0
except ZeroDivisionError:
    print("Cannot divide by zero!")

#FileNotFoundError
try:
    with open("missing.txt","r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")

#KeyError
student = {"name": "Sri", "marks": 88}
try:
    print(student["age"])
except KeyError:
    print("Key not exist in dictionary!")

# indexError
numbers = [1,2,3]
try:
    print(number[10])
except:
    print("Index out of range") 


#Handling multiple errors at once:try:
try:
    number = int(input("Enter a number: "))
    result = 10/number
    print(f"Result: {result}")
except ValueError:
    print("That's not a number!")
except ZeroDivisionError:
    print("Cannot divide by Zero!")

#else and finally:
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print(f"You entered: {number}")
finally:
    print("Program finished")

#Real LIfe Example = connecting to Telecom Project
def get_customer_bill(customer_id, bills):
    try:
        bill = bills[customer_id]
        result = bill / 100 * 18  # Calculate Tax
        total = bill + result
        return f"Bill: {bill}, Tax: {result} -> Total: {total}"
    except KeyError:
        return f"Customer {customer_id} not found"
    except ZeroDivisionError:
        return "Invalid bill amount!"
    finally:
        print(f"Lookup attempted for customer: {customer_id}")

bills = {"C001": 1200, 
         "C002": 850,
         "C003": 799,
         "C004": 1029,
         "C005": 707.80
        } 

print(get_customer_bill("C001",bills))
print(get_customer_bill("C999",bills))


