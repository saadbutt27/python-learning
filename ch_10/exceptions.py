from pathlib import Path
# print(5/0)
try:    
    print(5/0)
except ZeroDivisionError:
    print("Can't divide by zero")


def division():
    print("Calculator")
    print("Give me two numbers and I'll divide them")
    print("You can enter q to quit the program")
    while True:
        num1 = input("Enter number 1: ")
        if num1 == "q":
            break
        num2 = input("Enter number 2: ")
        if num2 == "q":
            break
        try:
            answer = int(num1) / int(num2)
        except ZeroDivisionError:
            print("Cannot divide by zero")
        else: 
            # if a code successfully passes the try block it wil come into else block an if an exception is raised
            # then else block will not be executed
            print(answer)

def addition():
    print("Addition")
    print("Give me two numbers and I'll add them. Enter q to quit the program.")

    while True:
        num1 = input("Enter num1: ")
        if num1 == "q":
            break
        num2 = input("Enter num2: ")
        if num2 == "q":
            break

        try:
            ans = int(num1) + int(num2)
        except ValueError:
            print("Can't add integer with number")
        else:
            print(ans)

# addition()

def animals(path):
    path = Path(path)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"File at {path} does not exist!")
    else:
        for line in contents.splitlines():
            print(f"- {line.title()}")

# animals("ch_10/text_files/cats.txt")
# animals("text_files/dogs.txt")

def count_words(path):
    path = Path(path)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"File at {path} does not exist!")
    else:
        total = contents.count("elit")
        print(total)

count_words("ch_10/text_files/alice.txt")