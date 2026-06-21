file = open("d:/Claude_Python/Day3/notes.txt", "w")
file.write("Hello Sri!\n")
file.write("This is your first file.\n")
file.close()


#use with which closes automatically:

with open("notes.txt", "w") as file:
    file.write("Hello Sri!\n")
    file.write("This is your first file.\n")

#reading a file

with open("notes.txt","r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("notes.txt","r") as file:
    for line in file:
        print(line.strip()) #strip removes \n at end of each line

# Read all lines into a list
with open("notes.txt", "r") as file:
    lines = file.readlines()
    print(lines)  # ['Hello Sri!\n', 'This is your first file.\n']