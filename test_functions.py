from functions import *
from secret import *
user = secret_user
password = secret_password
credentials = {"username": user, "password": password}

test_title_pass = "boku no hero academia"
test_title_fail = "boku no villian academia"
file_name = "text.txt"

def get_bearer_token():
    return bearer_token(credentials)

def run_update_pass():
    bearer = get_bearer_token()
    test_value = update_manga_read_status(test_title_pass, "reading", bearer)
    if test_value == True:
        print("run_update_pass() passed")
    else:
        print("run_update_pass() failed")

def run_update_fail():
    bearer = get_bearer_token()
    test_value = update_manga_read_status(test_title_fail, "reading", bearer)
    if test_value == False:
        print("run_update_failed() passed")
    else:
        print("run_update_failed() failed")

def run_get_manga_list_pass():
    bearer = get_bearer_token()
    compare_id = get_manga_id(test_title_pass, bearer)
    if compare_id != test_title_pass:
        print("run_get_manga_list_pass() passed")
    else:
        print("run_get_manga_list_pass() failed")

def run_get_manga_list_failed():
    bearer = get_bearer_token()
    compare_id = get_manga_id(test_title_fail, bearer)
    if compare_id == test_title_pass:
        print("run_get_manga_list_pass() passed")
    else:
        print("run_get_manga_list_pass() failed")

def run_read_file():
    print(read_file(file_name))

def run_add_to_follow_list():
    bearer = get_bearer_token()
    title = "shinryaku ika musume"
    add_to_follow_list(title, id, bearer)

