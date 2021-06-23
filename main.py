import os
from functions import *

try:
    print("Welcome, please login with your Mangadex account...")
    user = input("Username: ")
    password = input("Password: ")

    print("Logging in...")
    credentials = {"username": user, "password": password}
    bearer_token = bearer_token(credentials)

    input_value = input("Select what you would like to do:\n1: Create CSV file of your manga list with read status\n2: Update read status of a manga\n")
    if input_value == "1":
        print("Please wait while your list is being created...")
        create_csv(get_list_of_manga_and_read_status(bearer_token))
        print(
            f"Congratulations! Your list has been created at {os.getcwd()}"
            )
    if input_value == "2":
        manga_title = input("Please enter the name of the manga that you would like to update the read status of: ")
        manga_status = input("Please enter the reading status of the manga (reading, plan_to_read, completed, dropped, re_reading): ")
        update_manga_read_status(manga_title, manga_status, bearer_token)
        print("Update complete!")



except:
    print("Something went awry. Please try again later.")
