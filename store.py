# import requests
# from pyquery import PyQuery as pq
#
# url = 'https://www.zhihu.com/explore'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
# }
# html = requests.get(url, headers=headers).text
# doc = pq(html)
# items = doc('.explore-tab .feed-item').items()
# for item in items:
#     question = item.find('h2').text()
#     author = item.find('.author-link-line').text()
#     answer = pq(item.find('.content').html()).text()
    # file = open('explore.txt', 'a', encoding='utf-8')
    # file.write('\n'.join([question, author, answer]))
    # file.write('\n' + '=' * 50 + '\n')
    # file.close()


#json文件存储
# import json
#
# str = '''
# [{
#     "name": "Bob",
#     "gender": "male",
#     "birthday": "1992-10-18"
# }, {
#     "name": "Selina",
#     "gender": "female",
#     "birthday": "1995-10-18"
# }]
# '''
# print(type(str))
# data = json.loads(str)
# print(data)
# print(type(data))
# # a = json.dumps(data)
# # print(a)
# # print(type(a))
# print(data[0]['name'])
# print(data[0].get('name'))
#
# print(data[0].get('age'))
# print(data[0].get('age', 25))


# import json
#
# str = '''
# [{
#     'name': 'Bob',
#     'gender': 'male',
#     'birthday': '1992-10-18'
# }]
# '''
# data = json.loads(str)

# import json
#
# with open('data.json', 'r') as file:
#     str = file.read()
#     data = json.loads(str)
#     print(data)


# import json
#
# data = [{
#     'name': 'David',
#     'gender': 'male',
#     'birthday': '1992-10-18'
# }]
# with open('data.json', 'w') as file:
#     file.write(json.dumps(data,indent=2))


# import json
#
# data = [{
#     'name': '王伟',
#     'gender': '男',
#     'birthday': '1992-10-18'
# }]
# with open('data.json', 'w', encoding='utf-8') as file:
#     file.write(json.dumps(data, indent=2, ensure_ascii=False))


#csv文件存储
# import csv
#
# with open('data.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerow(['10001', 'Mike', 20])
#     writer.writerow(['10002', 'Bob', 22])
#     writer.writerow(['10003', 'Jordan', 21])
#
# import csv
#
# with open('data.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile, delimiter=' ')
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerow(['10001', 'Mike', 20])
#     writer.writerow(['10002', 'Bob', 22])
#     writer.writerow(['10003', 'Jordan', 21])

# import csv
#
# with open('data.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerows([['10001', 'Mike', 20], ['10002', 'Bob', 22], ['10003', 'Jordan', 21]])

# import csv
#
# with open('data.csv', 'w') as csvfile:
#     fieldnames = ['id', 'name', 'age']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
#     writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
#     writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})

# import csv
#
# with open('data.csv', 'a') as csvfile:
#     fieldnames = ['id', 'name', 'age']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writerow({'id': '10004', 'name': 'Durant', 'age': 22})


# import csv
#
# with open('data.csv', 'a', encoding='utf-8') as csvfile:
#     fieldnames = ['id', 'name', 'age']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writerow({'id': '10005', 'name': '王伟', 'age': 22})


# import csv
#
# with open('data.csv', 'r', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)

import pandas  as pd

df = pd.read_csv('data.csv')
print(df)