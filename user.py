class User:
    """ "Modeling a User"""

    def __init__(self, firstName, lastName, dob, bio):
        self.firstName = firstName
        self.lastName = lastName
        self.dob = dob
        self.bio = bio
        self.followers = 0  # default value
        self.login_attempts = 0

    def describe_user(self):
        print(
            f"----User Profile----\nName: {self.firstName.title()} {self.lastName.title()}\nDate of Birth: {self.dob}\nBio: {self.bio.title()}\nNo. of followers: {self.followers}\n"
        )

    def greet_user(self):
        print(f"Hello, {self.firstName.title()}\n")

    def update_followers(self, increment):
        """ "An updater function which will update nimber of followers"""
        if self.followers + increment >= 0:
            self.followers += increment

    def increment_login_attempts(self):
        """ "Increment login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


