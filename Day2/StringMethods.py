message = "Hello Sri, Welcome to Telecom Support!"

print(message.upper())
print(message.lower())
print(message.strip())
print(message.replace("Sri","Raj"))
print(message.split(","))

text = "telecom support"

#Capitalize
print(text.capitalize())
print(text.title())

#Check content
print(text.startswith("tel"))
print(text.endswith("port"))
print(("support" in text))

#Find Position
print(text.find("support"))

#count occurences
print(text.count("o"))

#Length
print(len(text))

#String splitting
customer_query = "billing,network,support,complaint"

services = customer_query.split(",")
print(services)

#join back
joined = " | ".join(services)
print(joined)


#String Methods Practice

customer_message = "hello, my BILL is too HIGH this month!"

cleaned = customer_message.strip().lower().replace("too high", "very high")

if "bill" in cleaned:
    print("Routing to Billing Agent")

words = cleaned.split()
print(len(words))

print(customer_message)


