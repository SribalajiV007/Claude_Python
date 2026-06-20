# student = {
#     "name": "Sri",
#     "age": 24,
#     "city": "Chennai"
# }

# print(student["name"])
# print(student["age"])
# print(student["city"])

# #Add new key
# student["course"] = "AI Engineering"
# print(student) 

# #update existing key
# student["age"] = 25
# print(student["age"])

# #delete a key
# del student["city"]
# print(student)

# #check if key exists 
# print("name" in student)
# print("phone" in student)

# #All keys
# print(student.keys())

# #All values
# print(student.values()) 

# #Loop through dictionary
# for key, value in student.items():
#     print(f"{key}: {value}")


#Exercise

phone = {
    "brand": "Samsung",
    "model": "Galaxy S23",
    "price": 80000,
    "color": "Black" 
}

for key, value in phone.items():
    print(f"{key}: {value}")

phone["price"] = 75000
print(f"Updated price: {phone['price']}")

phone["storage"] = "128GB"

print(phone)