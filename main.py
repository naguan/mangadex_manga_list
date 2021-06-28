import os
from functions import *
from to_add import *
from secret import *

try:
    print("Welcome, please login with your Mangadex account...")
    user = input("Username: ") or secret_user
    password = input("Password: ") or secret_password

    print("Logging in...")
    credentials = {"username": user, "password": password}
    bearer_token = bearer_token(credentials)
    while len(bearer_token) == 0 :
        print("Invalid username or password. Please try again.")
        user = input("Username: ") or secret_user
        password = input("Password: ") or secret_password

        print("Logging in...")
        credentials = {"username": user, "password": password}

        bearer_token = bearer_token(credentials)
    
    input_value = input("\nSelect what you would like to do:\n"+
                        "1: Create CSV file of your manga list with read status\n"+
                        "2: Update read status of a manga\n"+
                        "3: Update read status of all manga in .txt file\n"+
                        "Input: ")
    
    while(input_value != ""):
        
        if input_value == "1":
            print("\nPlease wait while your list is being created...")
            manga_list = get_list_of_manga_and_read_status(bearer_token)
            create_csv("Mangadex Follow List.csv", manga_list)
            print(  f"Congratulations! Your list has been created at {os.getcwd()}" )

        if input_value == "2":
            manga_title = input("\nPlease enter the name of the manga that you would like to update the read status of: ")
            manga_status = input("Please enter the reading status of the manga (reading, plan_to_read, completed, dropped, re_reading, null): ")
            successful_update = update_manga_read_status(manga_title, manga_status, bearer_token)
            if successful_update == True:
                print("\nUpdate complete!")
            else:
                print("\nManga title not found. Please try again.")

        if input_value =="3":
            print("\nNotice: Please make sure each line is formatted as follows: \'title,read status\'\n"+
                "Make sure titles are as specific as possible and do not contain commas."+
                "CSV file will be created with the manga that failed to be updated.")
            try:
                filename = input("Please enter file name: ")
                new_manga_to_add = read_file(filename)
                for manga in new_manga_to_add:
                    read_status = new_manga_to_add[manga]
                    successful_update = update_manga_read_status(manga, read_status, bearer_token)
                    if successful_update == False:
                        failed_to_add[manga] = read_status
                create_csv("Failed To Update Manga Read Status.csv", failed_to_add)
                print(  f"List of manga that failed to be updated has been created at {os.getcwd()}" )
            except FileNotFoundError:
                print("\nFile not found. Please try again.")

        if input_value == "0": #for manual dict input from .py file 
            for manga in new_manga_to_add:
                read_status = new_manga_to_add[manga]
                successful_update = update_manga_read_status(manga, read_status, bearer_token)
                if successful_update == False:
                    failed_to_add[manga] = read_status
            create_csv("Failed To Update Manga Read Status.csv", failed_to_add)
            
        input_value = input("\nSelect what you would like to do:\n"+
                            "1: Create CSV file of your manga list with read status\n"+
                            "2: Update read status of a manga\n"+
                            "3: Update read status of all manga in .txt file\n"+
                            "Enter to exit\n"
                            "Input: ")
    print("\nGoodbye")
except requests.HTTPError:
    print(requests.HTTPError)
except requests.ConnectionError:
    print(requests.ConnectionError)
except requests.RequestException:
    print(requests.RequestException)
except requests.Timeout:
    print(requests.Timeout)
except:
    print("Cannot connect to Mangadex. Please try again later.")
