import requests

'''Simple command lines to consume public API file'''
'''Get a response that has user_id: 10'''
info = requests.get('https://jsonplaceholder.typicode.com/posts?id=41').json()

user_id = info
print (user_id)
