from webtools import User, Browser
from getpass import getpass
    

email = input("What is your username: ")
pwd = getpass("What is your password: ")
usr = User(email, pwd)
print("Thanks!")
print("Give me a few seconds to pull up your browser...")

with Browser() as safari:
    safari.login_to_Microsoft(usr)
    login_successful = (safari.title == 'Microsoft account | Home')
    if login_successful:
        safari.maximize_window()
        safari.search_bing()
        print("All searches have been completed!")
    else:
        print("There was a problem logging in. Please try again.")
