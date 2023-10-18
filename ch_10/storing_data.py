from pathlib import Path
import json


def dump(numbers):
    path = Path("ch_10/text_files/numbers.json")
    contents = json.dumps(numbers)
    path.write_text(contents)

def get():
    path = Path("ch_10/text_files/numbers.json")
    contents = path.read_text()
    nums = json.loads(contents)
    return nums


numbers = [2,5,3,8,7,1,0,2]

# dump(numbers)
# print(get())

def get_stored_user(path):
    """Get stored user if available."""
    if path.exists():
        contents = path.read_text()
        profile = json.loads(contents)
        return profile
    else:
        return None
    
def get_new_user(path):
    """Prompt for a new user."""
    username = input("What is your name? ")
    password = input("What is your password? ")
    profile = {
        "username": username,
        "password": password
    }
    contents = json.dumps(profile)
    path.write_text(contents)
    return profile

def greet_user():
    """Greet the user by name."""
    path = Path('ch_10/text_files/profile.json')
    profile = get_stored_user(path)
    if profile: 
        print(f"Welcome back, {profile['username'].title(--upgrade)}! Here are your details")
        for key, value in profile.items():
            print(f"{key.title()}: {value.title()}")
    else:
        profile = get_new_user(path)
        print(f"We'll remember you when you come back, {profile['username']}!")
        
greet_user()

    
def get_stored_fvrt_num(path):
    """Checking if favourite number is stored or not"""
    if path.exists():
        content = path.read_text()
        content = json.loads(content)
        return content
    else:
        return None

def store_fvrt_num(path):
    n = input("Enter your favourite number: ")
    n = json.dumps(n)
    path.write_text(n)
    return n

def favourite_number():
    print("Favourite number")
    path = Path('ch_10/text_files/fvrt_num.json')
    fvrtNum = get_stored_fvrt_num(path)
    if fvrtNum: print(f"Your favourite number is {fvrtNum}.")
    else:
        fvrtNum = store_fvrt_num(path)
        print(f"Your favourite number is {fvrtNum}, we'll now remeber it.")

# favourite_number()