customer_input = "   SRI BALAJI | sri@gmail.com | CHENNAI | 9876543210   "

# name, email, city, phone = [item.strip() for item in customer_input.strip().spit("|")]

parts = customer_input.split("|")
print(parts)

name = parts[0].strip().title()
email = parts[1].strip().lower()
city = parts[2].strip().title()
phone = parts[3].strip()

print("---Customer Profile---")
print(f"Name: {name}")
print(f"Email: {email}")
print(f"City: {city}")
print(f"phone: {phone}")

