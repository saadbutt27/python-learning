from pathlib import Path

path = Path("ch_10/text_files/programming.txt")

path.write_text("I love programming ummah.")
print(path.read_text())

path = Path("ch_10/text_files/guest.txt")
name = input("Enter your name: ")
path.write_text(name)

path = Path("ch_10/text_files/guest_book.txt")
names = ""
print("Enter names and when you are done write quit")
while True:
    name = input("Enter name: ")
    if name != "quit":
        names += name + " \n"
    else:
        break

path.write_text(names)