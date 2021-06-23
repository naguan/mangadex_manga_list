from functions import *

user = "nguan"#input("Username: ")
password = "Lx2JtJ6RxFV!dfJ"#input("Password: ")
credentials = {"username": user, "password": password}

def get_bearer_token():
    return bearer_token(credentials)

def run_update():
    bearer = get_bearer_token()
    update_manga_read_status("girl with the sanpaku eyes", "reading", bearer)

def run_get_manga_list():
    bearer = get_bearer_token()
    get_manga_id("tomo-chan", bearer)

