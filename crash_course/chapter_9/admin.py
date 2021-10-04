from user import User

class Privileges:
    def __init__(self):
       self.privileges = ["can add post", "can delete post", "can ban user",]

    def show_privileges(self):
        print(f"User has following privileges:")
        for privilege in self.privileges:
            print(f"\t-{privilege}")

class Admin(User):
    def __init__(self, fname, lname, age, location):
        super().__init__(fname, lname, age, location)
        self.privilege = Privileges()
