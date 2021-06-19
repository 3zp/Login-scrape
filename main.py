import requests
import uuid
import os
from os import system
system("title " + "instagram.com/avhs")
req = requests.session()
UID = str(uuid.uuid4())
logurl = 'https://i.instagram.com/api/v1/accounts/login/'
username = input("Username : ")
password = input("Password : ") 
headers = {
    'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US",
    "X-IG-Capabilities": "3brTvw==",
    "X-IG-Connection-Type": "WIFI",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    'Host': 'i.instagram.com',
    'Connection': 'keep-alive'
}

logdata = {
    'uuid': UID,
    'password': password,
    'username': username,
    'device_id': UID,
    'from_reg': 'false',
    '_csrftoken': 'missing',
    'login_attempt_countn': '0'
}



def f():
        global coo
        headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'x-csrftoken': 'xX0K5q7XikrU1LAnenqEVKqb7J3qK4S6',
        'x-ig-app-id': '936619743392459',
        'x-instagram-ajax': '0c15f4d7d44a',
        'x-requested-with': 'XMLHttpRequest'
        }
        r = requests.get('https://www.instagram.com/accounts/edit/?__a=1', headers=headers, cookies=coo)
        email = r.json()['form_data']['email']
        phone = r.json()['form_data']['phone_number']
        emailc = r.json()['form_data']['is_email_confirmed']
        phonec = r.json()['form_data']['is_phone_confirmed']
        gender = r.json()['form_data']['gender']
        bday = r.json()['form_data']['birthday']
        print("Email :",email)
        print("Confirmed Email :",emailc)
        print("Phone :",phone)
        print("Confirmed Phone :",phonec)
        print("Gender :",gender)
        print("Birthday :",bday)
        input()

def login():
    global log, loginJS, change
    global coo
    global f
    log = req.post(logurl, headers=headers, data=logdata)
    loginJS = log.json()
    if 'logged_in_user' in log.text:
        coo = log.cookies
        f()
    else:
        print("Error")
        input()
login()
