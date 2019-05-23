'''
This is a very basic Base64decode script

Win$

'''

import base64
wins = input("Please enter the encoded string: ")
data = base64.b64decode(wins)
decoded = data.decode("utf-8")
print (decoded)
