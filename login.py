MSG_WELCOME = """
Welcome to Assignment 1"""

OPT_LOGIN = "1"
OPT_REGISTER = "2"
OPT_EXIT = "3"

MSG_OPTIONS = f"""
You can login with your existing account
If you don't have an account you need to register an account
Options:
    {OPT_LOGIN}. Login
    {OPT_REGISTER}. Register
    {OPT_EXIT}. Exit"""

MSG_OPTIONS_ASK = f"""
Please select option ({OPT_LOGIN}, {OPT_REGISTER} or {OPT_EXIT}): """


def login():
    print("Login")


def register():
    print("Register")


if __name__ == "__main__":
    print(MSG_WELCOME)
    print(MSG_OPTIONS)
    while True:
        option = input(MSG_OPTIONS_ASK)
        if option == "":
            pass
        elif option == "1":
            login()
            break
        elif option == "2":
            register()
            break
        elif option == "3":
            print("Exiting...")
            exit(0)
        else:
            print(f"Invalid option '{option}'. Exiting...")
            exit(1)
        
        
