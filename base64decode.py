'''
This is a very basic Base64decode script

Author : Winston M

'''

import base64
data = input("Please enter the base64 encoded string here: ")
wins = base64.b64decode(data).decode('utf-8')
print (wins)
