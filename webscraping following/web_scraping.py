from cgitb import text
from bs4 import BeautifulSoup
import requests, re
# tim's github repo for this video series
# https://github.com/techwithtim/Beautiful-Soup-Tutorial

#################### video 3

# some crypto coin price scraping on cointmarketcap.com

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")



tbody = doc.tbody
# prints table body 
# looking at sibling of tags
trs = tbody.contents

# applying below notes
'''prices = {}
for tr in trs:
    for td in tr.contents[2:4]:'''
        # imagine print line here
'''for tr in trs:
    name, price = tr.contents[2:4]
    print(name.p.string)
    print()
'''
# effectively the "top 10" coins for the site
'''
for tr in trs[:10]:
    name, price = tr.contents[2:4]
    print(name.p.string)
    print()
'''
# find tags with price
'''for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    print()
'''
# confirming we have a column of prices from those 

'''for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    print(price.a.string)
'''
# output
'''
$47,423.15
$3,392.76
$1.00
$432.74
$1.00
$0.8633
$1.18
$106.23
$111.77
$92.63
'''

for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string
    # well this does't work. not sure why
    #cprices[fixed_name] = fixed_price

#print(fixed_name)

#    print(price.a.string)











####  siblings
# find next sibling in the form
#trs[0].next_sibling

# also plural siblings
# trs[0].next_siblings # or prior sinblings trs[0].previous_siblings
# actually a "generator"
'''print(trs[0].next_siblings)'''
# output:
# <generator object PageElement.next_siblings at 0x0000025080A2F610>
# so convert to list
'''print(list(trs[0].next_siblings))'''
# output: giant wall of html. so clearly well a big long list as it implies


# parents/descendents
'''
trs[0].parent.name # entire tbody tag
'''

'''list(trs[0].children)'''

# applying this













#################### end video 3



#################### video 2
# "searching and filtering"
'''
with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")
'''
# .find() - first result instances
# .find_all() - all the instances

# change values 
'''
tag = doc.find("option")
tag['selected'] = 'false'
tag['color'] = 'blue'
print(tag)
'''
# output:
# <option color="blue" selected="false" value="course-type">Course type*</option>
'''
tags = doc.find_all(["p", "div", "li"])
print(tags)
'''
# just prints contents of those tags


'''
tags = doc.find_all(["option"], text="Undergraduate")
print(tags)
'''
# output: [<option value="undergraduate">Undergraduate</option>]


# just demonstration of attributes
'''
tags = doc.find_all(["option"], text="Undergraduate", value="undergraduate")
print(tags)
'''
# output:
# [<option value="undergraduate">Undergraduate</option>]


# finding class names
# class is already term in html so use class_
'''tags = doc.find_all(class_="btn-item")
print(tags)
'''
# output:
# [<a class="btn-item" href="https://www.w3docs.com/learn-html.html">Learn HTML</a>, <a class="btn-item" href="https://www.w3docs.com/quiz/#">Select Quiz</a>]

# ---------> basic regular expressions

'''
tags = doc.find_all(text=re.compile("\$.*"))
for tag in tags:
    print(tag.strip())
'''
#print(tags)
# output: 
# before strip
# ['\n        $2345\n      ', '\n        $123\n        ']
# after strip
# $2345
# $123

# ----------> limit number of search results
'''
tags = doc.find_all(text=re.compile("\$.*"), limit=1)
for tag in tags:
    print(tag.strip())
'''
# output:
# $2345

# -------------------> save modificaitons to html doc
'''
tags = doc.find_all("input", type="text")
for tag in tags:
    tag['placeholder'] = "I changed you"
# apparently "w" will create new file or overwrite existing file
# and yes, it did create a new file with that "i changed you" string
with open("changed.html", "w") as file:
    file.write(str(doc))
'''

#    print(tag.strip())

















#################### end video 2




#################### video 1

# I pulled the html from the repo
'''
with open ("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser") # confirmed as working
'''
#print(doc.prettify)

# finding by tag name
#tag = doc.title
# get first instance of a tag and print tags as well as contents
'''print(tag)'''
# print only contents of string
'''print(tag.string)'''

#tags = doc.find_all("p")
#this will give me both the p tags as well as the contents of all instances of the p tag
# also with [ ] surrounded
'''print(tags)'''

# can also set the value of a tag, like making the title equal to "hello"

# read html from web site
# go to newegg 3080 page
# https://www.newegg.com/gigabyte-geforce-rtx-3080-gv-n3080vision-oc-10gd/p/N82E16814932460

'''url = "https://www.newegg.com/gigabyte-geforce-rtx-3080-gv-n3080vision-oc-10gd/p/N82E16814932460"

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")
'''
#print(doc.prettify())

'''prices = doc.find_all(text="$")
'''
#print(prices)
# output: ['$', '$', '$', '$']

# we need to retrieve the "paraent" of the $ to get the contents
'''
parent = prices[0].parent
strong = parent.find("strong")
'''
#print(strong)
# output: <strong>999</strong>
'''
print(strong.string)
'''
# this version is just the price. 999 in this case.



#################### video 1