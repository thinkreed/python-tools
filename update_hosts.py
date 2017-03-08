#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import requests



HOSTS_URL='https://raw.githubusercontent.com/racaljk/hosts/master/hosts'

LOCAL_HOSTS='/etc/hosts'

def update():
    r = requests.get(HOSTS_URL)
    with open(LOCAL_HOSTS, "w+") as hosts:
        hosts.writelines(r.text)

if __name__ == '__main__':
    update()
