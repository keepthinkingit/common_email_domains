#!/usr/bin/python3
# coding:utf-8

with open("./email_domains.txt",'r') as file:
    print('正在操作文件')
    domains = ''
    for line in file.readlines():
        domains += line.strip('\n') + ' '
    python3 /opt/iredapd/tools/spf_to_greylist_whitelists.py domains
    print("Import complete.")