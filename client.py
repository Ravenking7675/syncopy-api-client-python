import requests

def _url(path):
    return "https://syncopy-api.herokuapp.com{}".format(path)

def generate_key(unique_str, username, isPc):
    url = _url("/generate_key")
    
    body={
        "unique_str": unique_str,
        "username": username,
        "isPc": isPc
    }
    
    resp = requests.post(url, json=body)
    return resp

def get_key_with_username(username):
    url = _url("/key/{}".format(username))
    resp = requests.get(url)
    return resp

def add_connection(uuid_sender, uuid_reciever):

    url = _url("/add_connection")
    
    body = {
        "uuid_sender": uuid_sender,
        "uuid_reciever": uuid_reciever
    }
    
    resp = requests.post(url, json=body)
    return resp

def connections(uuid):
   
    url = _url("/connections/{}".format(uuid))
    resp = requests.get(url)
    return resp

def clip(sender, sender_id, reciever, reciever_id, time, content):
    url = _url("/clip")
    
    body = {
    "sender": sender,
    "sender_id": sender_id,
    "reciever": reciever,
    "reciever_id": reciever_id,
    "time": time,
    "content": content,
    "checked": False
    }
    
    resp = requests.post(url, json=body)
    return resp


def recieved_all(uuid):
    
    url = _url("/recieved/{}".format(uuid))

    resp = requests.get(url)
    return resp
    
def recieved_n(uuid, n):
    
    url = _url("/recieved/{}/{}".format(uuid, n))
    
    resp = requests.get(url)
    return resp

def recieved_recent(uuid):
    
    url = _url("/recieved/{}/1".format(uuid))
    
    resp = requests.get(url)
    return resp

def recieved_checked(uuid):
    url = _url("/recieved/{}/1".format(uuid))
    
    resp = requests.post(url)
    return resp

def sent_n(uuid, n):
    
    url = _url("/sent/{}/{}".format(uuid, n))
    
    resp = requests.get(url)
    return resp

def sent_all(uuid):
    
    url = _url("/sent/{}".format(uuid))

    resp = requests.get(url)
    return resp

def sent_delete_all(uuid):
    
    url = _url("/sent/{}".format(uuid))

    resp = requests.delete(url)
    return resp
