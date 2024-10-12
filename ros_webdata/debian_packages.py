import requests
import sys
import os


DEBIAN_URL = 'https://packages.debian.org/stable/allpackages?format=txt.gz'
def get_debian_packages():
    print('get_debian_packages')
    response = requests.get(DEBIAN_URL)
    # content = response.content.decode('utf-8')
    content = response.text
    line_count = 0
    packages = {}
    for line in content.split('\n'):
        # if line_count> 20:
        #    break
        line_count += 1
        left_paren = line.find('(')
        right_paren = line.find(')')
        if left_paren < 0 or right_paren < 0:
            continue
        package_name = line[:left_paren - 1]
        package_desc = line[right_paren + 2:]
        packages[package_name] = package_desc
        # print(f'{package_name} : {package_desc}')
    return packages
