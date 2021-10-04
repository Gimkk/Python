#task9-11
from user import Admin

user = Admin("David","boom", 45, "australia")
user.describe_user()
user.greet_user()
user.show_privileges()
user.show_logins()

for _counter in range(1,5):
    user.increment_login_attempts()

user.show_logins("increment")
user.reset_login_attempts()
user.show_logins("reset")