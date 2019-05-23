'''
This is a very basic Base64decode script

Author : Winston M

'''

import base64
data = input("Magic starts here: ")
wins = base64.b64decode(data).decode('utf-8')
print (wins)
