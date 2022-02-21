from flask import session
import os
import requests
import json

def get_cards():
    board_id = os.getenv ('BOARD_ID')
    key = os.getenv ('API_KEY')
    token = os.getenv ('API_TOKEN')
    url = f"https://api.trello.com/1/boards/{board_id}/lists"

    headers = {
       "Accept": "application/json"
    }

    query = {
        "key" : key,
        "token" : token, 
        "cards" : "open"
    }

    response = requests.get(
       url,
       headers=headers,
       params = query
    )

    

    cards = []
    trellolists = json.loads(response.text)

    for trellolist in trellolists:
        status = trellolist ["name"]
        for card in trellolist ["cards"]:
            id = card ["id"]
            title = card ["name"]
            item = { 'id': id, 'title': title, 'status': status }
            cards.append(item)
    
    return cards




def get_lists():
    board_id = os.getenv ('BOARD_ID')
    key = os.getenv ('API_KEY')
    token = os.getenv ('API_TOKEN')
    url = f"https://api.trello.com/1/boards/{board_id}/lists"

    headers = {
       "Accept": "application/json"
    }

    query = {
        "key" : key,
        "token" : token, 
        "fields" : "id,name"
    }

    response = requests.get(
       url,
       headers=headers,
       params = query
    )

    return json.loads(response.text)

    
def post_add(title):
    key = os.getenv('API_KEY')
    token = os.getenv('API_TOKEN')
    url = f"https://api.trello.com/1/cards"

    headers = {
       "Accept": "application/json"
    }

    query = {
        "key" : key,
        "token" : token, 
        "idList" : get_lists()[0]["id"],
        "name": title
    }

    response = requests.post(
       url,
       headers=headers,
       params=query
    )

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

def get_card(id):
    
    items = get_cards()
    return next((item for item in items if item['id'] == id), None)

def delete_card (id):
    existing_card = get_card(id)
    board_id = os.getenv ('BOARD_ID')
    key = os.getenv ('API_KEY')
    token = os.getenv ('API_TOKEN')
    url = f"https://api.trello.com/1/cards/{id}"

    headers = {
       "Accept": "application/json"
    }

    query = {
        "key" : key,
        "token" : token, 
        "fields" : "id,name,closed"
        
    }

    data= {
	    "id": id,
	    "name": existing_card ["title"],
	    "closed": "true"
    }

    response = requests.put(
       url,
       headers=headers,
       params = query,
       data=(data)
    )

def update_status (id):
    existing_card = get_card(id)
    board_id = os.getenv ('BOARD_ID')
    key = os.getenv ('API_KEY')
    token = os.getenv ('API_TOKEN')
    url = f"https://api.trello.com/1/cards/{id}"

    headers = {
       "Accept": "application/json"
    }

    query = {
        "key" : key,
        "token" : token, 
        "fields" : "id,name,idList"
        
    }

    trellolists = get_lists()
    cardstatus = existing_card ["status"]
    newidlist = ""
    for trellolist in trellolists:
        status = trellolist ["name"]
        if status == cardstatus:
            if trellolists.index(trellolist)+1 != len(trellolists):
                newidlist=trellolists[trellolists.index(trellolist)+1] ["id"]
                break
            else: 
                newidlist=trellolist["id"]
                break        

    data= {
	    "id": id,
	    "name": existing_card ["title"],
	    "idList" : newidlist
    }

    response = requests.put(
       url,
       headers=headers,
       params = query,
       data=(data)
    )


