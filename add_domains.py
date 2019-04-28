#!/usr/bin/python3
# coding:utf-8

import os

with open("./email_domains.txt",'r') as file:
    print('正在操作文件')
    domains = ''
    for line in file.readlines():
        domains += line.strip('\n') + ' '
    result = os.system('python2 /opt/iredapd/tools/spf_to_greylist_whitelists.py %s' % domains)
    if result == 0:
        print('请检查脚本')
    else:
        print("添加完成")