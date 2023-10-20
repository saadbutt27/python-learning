from pathlib import Path 

# path = Path("ch_10/text_files/pi_file.txt")
# path = Path("ch_10/text_files/pi_million.txt")
# contents = path.read_text()
# print(contents)

# lines = contents.splitlines() # splitlines function will spit the lines and make a list
# print(lines)

# pi_string = ""
# for line in lines:
#     pi_string += line.lstrip()

# print(pi_string[:40])

# print(len(pi_string))

# birthday = input("Enter your birthday in ddmmyyyy format: ")
# if(birthday in pi_string):
#     print("Yuhuu")
# else: 
#     print("Nuhuuu")

path = Path("text_files/alice.txt")
try:
    contents = path.read_text()
except FileNotFoundError:
    print(f"File at {path} not found!")
# print(contents)

# linesList = contents.splitlines()
# print(linesList)
else:
    # for line in contents.splitlines():
    #     line = line.replace("python", "javascript")
    #     print(line)
    contents_1 = contents.split()
    print(contents_1, len(contents_1))