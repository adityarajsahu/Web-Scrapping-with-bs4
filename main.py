import requests
from bs4 import BeautifulSoup


#url of the website to be scrapped.
url = "https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53"

# get the HTML in form of string.
r = requests.get(url)
html_content = r.content
# print(html_content)

# parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')
# 'html.parser' is the parser type.
# print(soup.prettify)

# HTML tree traversal
title = soup.title
#soup.title is the bs4 element object
# print(title)
# title.string gives us the string inside the title tag.
# print(title.string)

paras = soup.find_all('p')
# print(paras)
#find_all() returns a list of tag objects which contain the specified tag.

anchors = soup.find_all('a')
# print(anchors)

#get all the links in a page
# for link in anchors:
#     print(link.get('href'))

class_of_first_p = soup.find('p')['class']
#find() returns only the first tag object that contains the specified tag.
# ['class'] provides us the list of classes in that tag.
# print(class_of_first_p)

#find all the elements with a specific class name
# p_with_class_name = soup.find_all('p', class_ = "class_name")
# print(p_with_class_name)

# get the text from tags / soup
p_text = soup.find('p').get_text()
# print(p_text)  

# find tags by id
# find_by_id = soup.find(id='id_name')
# print(find_by_id)

#find children of a tag
# children_of_id = find_by_id.children
# .content - tag's children are available as a list
# .children - tag's children are available as a generator

# for elem in find_by_id.contents:
#     print(elem) 

# find the parent of a tag
first_p = soup.find('p')
parent_of_first_p = first_p.parent
# print(parent_of_first_p)

# .parent creates a generator that can be iterated.
for item in first_p.parents:
    # print(item)
    print(item.name)

# find element using select(), select() returns a list 
elem1 = soup.select('.class_name')
elem2 = soup.select('#id_name')
print(elem1)
print(elem2)