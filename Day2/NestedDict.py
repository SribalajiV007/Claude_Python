customer = {
    "name": "Sri",
    "plan": {
        "type": "Postpaid",
        "price": 999,
        "data": "2GB/day"
    }
}

#Access nested value
print(customer["name"])
print(customer["plan"]["type"])
print(customer["plan"]["data"])


#Exercise

student = {
    "name": "Sri",
    "marks": {
        "python": 88,
        "maths": 76,
        "english": 91
    }
}

print(student["name"])

for key, value in student["marks"].items():
    print(f"{key} :{value}")

marks = student["marks"]
average = sum(marks.values()) / len(marks)
print(f"Average: {average}")

#Exercise 2:

inventory = {
    "apple": 50,
    "banana": 30,
    "mango": 20,
    "orange": 45
}

for key, value in inventory.items():
    print(f"{key}: {value}")

inventory["mango"] = 5
print(f"After purchase: mango = {inventory['mango']} units")

inventory["grapes"] = 60
print(f"After adding grapes: {inventory['grapes']} units")

del inventory["banana"]
print("After removing banana")

highest_item = max(inventory, key=inventory.get)
print(f"Highest stock: {highest_item} = {inventory[highest_item]} units") #grapes is higesht stock , not apple

print(inventory)

