# Import the Chef class from the chef file
from chef import Chef


# Using inheritance to copy all the dishes from the Chef file,
# Since the chinese chef can make all the same dishes.
class Chinese_Chef(Chef):
    def make_special_dish(self):
        print("The chef makes orange chicken")

    def make_fried_rice(self):
        print("The chef makes fried rice")