from user import User

class Privilige:
    """Composed Privilige class"""

    def __init__(self, priviliges):
        self.priviliges = priviliges

    def show_priviliges(self):
        print("Admin's Priviliges")
        for privilige in self.priviliges:
            print(f"* {privilige}")
class Admin(User):
    """Admin is a special type of a model of User's model"""

    def __init__(self, firstName, lastName, dob, bio, priviliges):
        super().__init__(firstName, lastName, dob, bio)
        self.priviliges = Privilige(priviliges)

