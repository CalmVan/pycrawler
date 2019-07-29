# import urllib.request
#
# response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))
#
# print(type(response))
#
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))
# print(response.getheader('Date'))

# import urllib.parse
# import urllib.request
#
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
# #其中转字节流采用了bytes()方法，该方法的第一个参数需要是str（字符串）类型，需要用urllib.parse模块里的urlencode()方法来将参数字典转化为字符串；第二个参数指定编码格式，这里指定为utf8。
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read().decode('utf-8'))

# import urllib.request
# import socket
# import urllib.error
#
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
#     print(response.read())
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')


import urllib.request

request = urllib.request.Request('https://python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))