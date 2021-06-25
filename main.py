import os
from functions import *
from to_add import *

try:
    print("Welcome, please login with your Mangadex account...")
    user = input("Username: ")
    password = input("Password: ")

    user = secret_u
    password = secret_p

    print("Logging in...")
    credentials = {"username": user, "password": password}
    bearer_token = bearer_token(credentials)
    
    input_value = input("Select what you would like to do:\n"+
                        "1: Create CSV file of your manga list with read status\n"+
                        "2: Update read status of a manga\n"+
                        "Input: ")
    
    while(input_value != ""):
        
        if input_value == "1":
            print("Please wait while your list is being created...")
            manga_list = get_list_of_manga_and_read_status(bearer_token)
            create_csv("Mangadex Follow List.csv", manga_list)
            print(  f"Congratulations! Your list has been created at {os.getcwd()}" )

        if input_value == "2":
            manga_title = input("Please enter the name of the manga that you would like to update the read status of: ")
            manga_status = input("Please enter the reading status of the manga (reading, plan_to_read, completed, dropped, re_reading): ")
            successful_update = update_manga_read_status(manga_title, manga_status, bearer_token)
            if successful_update == True:
                print("Update complete!")
            else:
                print("Manga title not found. Please try again.")

        if input_value == "3": #framework for future json file input
            for manga in new_manga_to_add:
                read_status = new_manga_to_add[manga]
                successful_update = update_manga_read_status(manga, read_status, bearer_token)
                if successful_update == False:
                    failed_to_add[manga] = read_status
            create_csv("Failed To Update Manga Read Status.csv", failed_to_add)
            


        input_value = input("Select what you would like to do:\n"+
                            "1: Create CSV file of your manga list with read status\n"+
                            "2: Update read status of a manga\nEnter to exit\n"+
                            "Input: ")



except:
    print("Cannot connect to Mangadex. Please try again later.")
