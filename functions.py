import requests
import csv
import operator
import json
import collections

url = "https://api.mangadex.org"

def bearer_token(credentials):
    auth = requests.post(
        f"{url}/auth/login", json=credentials
        ).json()
    if auth["result"] == "ok":
        token = auth["token"]["session"]
        bearer = {"Authorization": f"Bearer {token}"}
        return bearer
    else:
        print(auth["errors"][0]["detail"])
        return {}

def get_list_of_manga_and_read_status(bearer):
    list_of_manga = requests.get(
        f"{url}/manga/status", headers=bearer
    ).json()

    manga_status = list_of_manga["statuses"]
    return get_manga_name_read_status(manga_status, bearer)
    
def get_manga_name_read_status(list_of_manga_ids, bearer):
    follow_list = {}
    for id in list_of_manga_ids:
        manga_query = requests.get(
            f"{url}/manga/{id}/", headers=bearer
        ).json()
        print(manga_query["data"]["attributes"]["title"]["en"])
        follow_list[manga_query["data"]["attributes"]["title"]["en"]] = list_of_manga_ids[id]

    sorted_list = collections.OrderedDict(sorted(follow_list.items(), key=operator.itemgetter(1)))

    return sorted_list

def update_manga_read_status(title, status, bearer):
    if status == "null":
        status = None
    payload = json.dumps(
        {
        "status" : status
        }, 
        indent = 4
        )
    id = get_manga_id(title)
    if id == title:
        print(f"\'{title}\' update to \'{status}\': failed")
        return False
    else:
        update_reading_status = requests.post(
            f"{url}/manga/{id}/status", headers=bearer, data=payload
        ).json()
        print(f"\'{title}\' update to \'{status}\': {update_reading_status['result']}")

        if(status == "reading"):
            add_to_follow_list(title, id, bearer)
        return True

def add_to_follow_list(title, id, bearer):
    title_to_add_to_follow = requests.post(
        f"{url}/manga/{id}/follow", headers=bearer
    ).json()
    if(title_to_add_to_follow["result"] == "ok"):
        print(f"\'{title}\' successfully added to follow list")
    else:
        print(f"\'{title}\' failed to add to follow list")

def remove_from_follow_list(title, id, bearer):
    title_to_add_to_follow = requests.delete(
        f"{url}/manga/{id}/follow", headers=bearer
    ).json()
    if(title_to_add_to_follow["result"] == "ok"):
        print(f"\'{title}\' successfully removed from follow list")
    else:
        print(f"\'{title}\' failed to remove from follow list")

def get_manga_id(title):
    payload = {
        "limit":1,
        "title":title
        }
    manga_query = requests.get(
        f"{url}/manga", params=payload
    ).json()

    if len(manga_query['results']) == 0:
        return title
    else:
        manga_id = manga_query["results"][0]["data"]["id"]
        return manga_id

def create_csv(document_title, follow_list):
    try:
        with open(document_title, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Title", "Read Status"])
            print("Creating...")
            for manga in follow_list:
                    writer.writerow(
                        [
                            manga,
                            follow_list[manga]
                        ]
                    )
            print("Completed.")
    except PermissionError:
        print("Please close previous csv file when trying to make a new one.")

def read_file(filename): #input file -> title must not contain commas; txt file lines should look like "title,status"
    output_dict = {}
    with open(filename, "r") as list:
        list_of_titles_and_status = list.readlines()
        for title_and_status in list_of_titles_and_status:
            pair = title_and_status.split(",")
            output_dict[pair[0]] = pair[1].rstrip()
    return output_dict