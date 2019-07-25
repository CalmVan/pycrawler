# html = '''
# <div>
#     <ul>
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>
# '''
# # from pyquery import PyQuery as pq
# # doc = pq(html)
# # print(doc('li'))
# #
# # from pyquery import PyQuery as pq
# # doc = pq(url='https://maoyan.com/board/4')
# # print(doc('title'))
# #
# # from pyquery import PyQuery as pq
# # import requests
# # doc = pq(requests.get('https://maoyan.com/board/4').text)
# # print(doc('title'))
#
# from pyquery import PyQuery as pq
# doc = pq(filename='test.html')
# print(doc('li'))


#css选择器
# html = '''
# <div id="container">
#     <ul class="list">
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>
# '''
#
# # from pyquery import PyQuery as pq
# # doc = pq(html)
# # print(doc('#container .list li>a'))
# #print(type(doc('#container .list li')))
#
#查找节点（子节点）
# from pyquery import PyQuery as pq
# doc = pq(html)
# items = doc('.list')
# print(type(items))
# print(items)
# # lis = items.find('li')
# # print(type(lis))
# # print(lis)
# lis = items.children()
# print(type(lis))
# print(lis)

#查找节点（父节点）
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
# from pyquery import PyQuery as pq
# doc = pq(html)
# items = doc('.list')
# container = items.parent()
# print(type(container))
# print(container)

# from pyquery import PyQuery as pq
# doc = pq(html)
# items = doc('.list')
# parents = items.parents()
# print(type(parents))
# print(parents)

from pyquery import PyQuery as pq
doc = pq(html)
li = doc('.list .item-0.active')
print(li.siblings())