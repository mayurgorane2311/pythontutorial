# Ex 1 on requests modules in python basically it used for to aceses http url thorough python
# import requests
#
# x = requests.get('https://w3schools.com/python/demopage.htm')
#
# print(x.text)

# Ex 2 json modules in python

import json

dictionary = {"mayur":"python programmer","gorane":"surname","qualification":["be","diploma"],"ravan":(452,"ram")}

print(dictionary)

par = json.load(dictionary)
