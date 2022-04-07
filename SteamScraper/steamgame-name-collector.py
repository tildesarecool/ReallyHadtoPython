
######## was in use
#from pydoc import doc
#from unittest import result
#from attr import attr
#import bs4, requests, webbrowser, sys, pyperclip
#from bs4 import BeautifulSoup
######## was in use


######## was in use
# STEAM_LIBRARY_URL = "https://steamcommunity.com/id/subassy/games/?tab=all&sort=name" # my steam library
# URL_TRUE = 200 # status code from "requests" that it "found the URL" thus it's as good as 'true' in this context
######## was in use

# STEAM_LIBRARY_URL = "https://steeeeamcommmmmmunity.com/id/subassy/games/?tab=all"

######## was in use
#def testLibURL(LibraryURL):
#    testExists = requests.get(LibraryURL)
    #print(testExists.status_code)
#    return testExists.status_code # returns int, 200 means returns true; or returns 'response object'. or i'm not sure. 200 anyway
######## was in use

#    try:
    #return testExists.raise_for_status()
#    except: break

#################################### many hours later ####################################

    #result = requests.get(STEAM_LIBRARY_URL) # resut.text will show whole source of page
    #doc = BeautifulSoup(result.text, "html.parser")

import requests, pyperclip
from bs4 import BeautifulSoup
STEAM_LIBRARY_URL = "https://steamcommunity.com/id/subassy/games/?tab=all&sort=name"
URL_TRUE = 200 # status code from "requests" that it "found the URL" thus it's as good as 'true' in this context

result = requests.get(STEAM_LIBRARY_URL) # resut.text will show whole source of page
loadToBeaut = BeautifulSoup(result.text, "html.parser")

    # print(doc.find_all("a")[1])
# scriptContent = loadToBeaut.find_all("script")[17] # this is winning line: it is 18th script tag or 17 counting from 0
#scriptContent = loadToBeaut.find_all("script")[17] # this is winning line: it is 18th script tag or 17 counting from 0
scriptContent = str(loadToBeaut.select('#responsive_page_template_content > script:nth-child(4)')[0])
'''
# (keep this)
PostambleStartPos = (scriptContent.find("= ") + 2)
print(PostambleStartPos)
print(scriptContent[0:PostambleStartPos])
'''
PostambleStartPos = (scriptContent.find("= ") + 2)
#print(scriptContent.find(("rgChangingGames")))
startSuffixPos = scriptContent.find("rgChangingGames") - 8
endSuffixPos = len(scriptContent)
wholeOfSuffix = scriptContent[(startSuffixPos):endSuffixPos]


#startKeepPos = scriptContent[PostambleStartPos]
#endKeepPos = scriptContent[startSuffixPos]
#justGamedata = scriptContent[startKeepPos:endKeepPos]
#print(str(endKeepPos))
#print("the start position is " + str(PostambleStartPos) + " and the end is " + str(startSuffixPos))
justGamedata = scriptContent[PostambleStartPos:startSuffixPos]
#print(justGamedata)

'''pyperclip.copy(justGamedata)'''

#pyperclip.copy(result.json()) # this did not go well
#print(type(justGamedata)) # (string)

'''
writeAfile = open("justGamedata.txt", "x")
writeAfile.write(justGamedata)
writeAfile.close()
'''


#print(wholeOfSuffix)
#print(len(scriptContent))

'''
# this thing works for suffix
pyperclip.copy(wholeOfSuffix)
'''
#rawString = scriptContent[:49]
'''
preambleText = scriptContent[:49] # <--- this goes up to 'rgGames = ', so exclude this string
noMorePreamble = scriptContent.replace(preambleText, '')
'''

#scriptContent.find()

#print(scriptContent.count("]")) # 
'''print(scriptContent.find("rgChangingGames")) # just 1. obviously.'''

# apparently remove prefix/suffix is a thing
#print(str(noMorePreamble[-815:-1])) # well str(noMorePreamble[-815:-1]) technically does it



#postText = noMorePreamble.split(sep=";") # splits return list not string

#print(type(postText)) # returns list

#print(rawString)
#elems = scriptContent[0]

#print(type(elems))
#print(type(scriptContent))
#getmore = elems.get_text("[{")
#getmore = elems.get_text(separator="=")
#tryAtCData = elems.cdata_list_attributes[]
#pyperclip.copy(scriptContent)
#pyperclip.copy(str(postText)) # my list/string converting needs work
#pyperclip.copy(noMorePreamble)
#pyperclip.copy(str(rawString))
#pyperclip.copy(str(elems.get_text(separator="=")))
#pyperclip.copy(str(elems))
#pyperclip.copy(str(getmore))
#pyperclip.copy(str(getmore))

#print(scriptContent)


'''
apparnetly an unassigned string literal with three quotes is a multi-line comment in ptyon

It took many hours to figure this out, but this page
"https://steamcommunity.com/id/subassy/games/?tab=all&sort=name" 
with all the list of game names etc
isn't actually the the html
it's auto-generated with a giant javascript data
there's one javascript variable equal to ...i guess that's an array.
it starts
var rgGames = [{"appid":1025480,"
Anyway, it uses that rgGames variable to then generate this whole table for all the games on-the-fly
That data actually is in an okay format
so really all i have to do is download the whole page locally which what i should do anyway
or use pyperclip to capture the whole page and copy it to the clipboard
then parse out just that javascript tag then grab all the data since there's all those appid: name: 
lists in there anyway
maybe it's actually json format. i can't tell.
actually i could probably insert a newline after every comma,
the udemy course covered that
so i wouldn't have to parse html at all. just this gaint maybe/maybe not json-like data blob


since I'm almost positive the data block on the steam library page is json formatted already
it'd make sense to figure out how to capture just that portion of the page and convert into something 
python can read like a dictionary
then eventually write the back out to a file just so it doesn't have to retreived again if for no other 
reason
I my library doesn't change that often so the retrieving part could be an optional thing with the default
being to just load in the data from the last retrieval

I started using this video
https://www.youtube.com/watch?v=-51jxlQaxyA
to learning about python/json
as I could expect, the library is
import json
then with the long string of data available (starting from a curly brace {) 
assign it to a variable 
json_stirng == (long json formatting string) - won't work if not valid json
follwoing by another variable
data = json.loads(json_string) - the 's' in 'loads' actually stands for 'string'. there's also file mode
assume that's done successfully, possible to append with  something like
data['test'] = True
new_json = json.dumps(data)
print(new_json) - that test is appended to end
or
new_json = json.dumps(data, indent=2)
to put in the indentation
and also
new_json = json.dumps(data, indent=2, sort_keys=True)
to sort keys alphabetically
I'll use the capture json data i already saved as a file, gameslibrary.json as a test


'''
# this is the working json code - march 25 2022
''''
import json
with open("justonegame.json", "r") as f:
    data = json.load(f) # no s load, because loading as file


# print(data.items())

with open("appended-one-game.json", "w",) as f:
    json.dump(data, f, indent=2, sort_keys=True)

'''


'''
felt like i should save this
this is contnets of justonegame.json and it works with the json/open file function
i mean no json errors from vscode anyway. could end up with other issues.
-------------------------
{
    "appid":1025480,
    "name":"1-Bit Revival: The Residuals of Null",
    "app_type":1,
    "logo":"https:\/\/cdn.akamai.steamstatic.com\/steam\/apps\/1025480\/capsule_184x69.jpg",
    "friendlyURL":1025480,"availStatLinks":
    {
        "achievements":true,
        "global_achievements":true,
        "stats":false,
        "gcpd":false,
        "leaderboards":false,
        "global_leaderboards":false
    },
        "hours_forever":"0.6",
        "last_played":1642216987
}
--------------------
output:
dict_items([('appid', 1025480), ('name', '1-Bit Revival: The Residuals of Null'), ('app_type', 1), ('logo', 'https://cdn.akamai.steamstatic.com/steam/apps/1025480/capsule_184x69.jpg'), ('friendlyURL', 1025480), ('availStatLinks', {'achievements': True, 'global_achievements': True, 'stats': False, 'gcpd': False, 'leaderboards': False, 'global_leaderboards': False}), ('hours_forever', '0.6'), ('last_played', 1642216987)])


'''


#################################### many hours later ####################################


#testLibURL(STEAM_LIBRARY_URL)

######## was in use
#def getGameUUID():
######## was in use    

    #soup = bs4.BeautifulSoup(file.txt, 'html.parser')
    #testResult = testLibURL(STEAM_LIBRARY_URL)
    #if testResult == URL_TRUE:
    # with open("saved-library-page.html", "r") as f:

######## was in use
    #result = requests.get(STEAM_LIBRARY_URL) # resut.text will show whole source of page
    #doc = BeautifulSoup(result.text, "html.parser")
######## was in use

    #ToFind = doc.find_all(text="Steam")
    # print(doc.find_all("img")[1])
    #print(doc.find_all(text="Days"))
    # print(doc.find_all("a")[1]) # THIS FORM WORKS, DON'T MODIFY: # print(doc.find_all("a")[1]) #
    #print(doc.find(Days))
    # print(doc.title) # well at least this works: <title>Steam Community :: subassy :: Games</title>
    # print(doc.title.contents) # also works; contents: ['Steam Community :: subassy :: Games']
    #findings = doc.find_all(id="global_header")[0] #, "gameListRowItemTopPrimary")
    # findings = doc.find_all(attrs={"id": "global_action_menu"}) # this works!
    #findings = doc.find_all(attrs={"class": "gameListRowItemTopPrimary"}) # this one doesn't!
    # apparently there's a different notation for classes versus divs 
    # findings = doc.find_all("div", class_="gameListRowItemTopPrimary") # well this still return empty but at least no error
    # findings = doc.find_all(class_="submenu_store") # well this worked but gameListRowItemTopPrimary didn't so it's a mystery so far
    #putOnClipboard = 

######## was in use
  #  pyperclip.copy(result.text)# put contents of whatever the results.get fucntion above is downloading
######## was in use
#     
    #print(doc)
    
    #findings = doc.find_all(class_="game_capsule") 
    #print(findings)
# gameListRowItemTopPrimary

    #print(doc.find_all(attrs="class"))
    
        #result = requests.get(STEAM_LIBRARY_URL) # resut.text will show whole source of page
        #doc = BeautifulSoup(result.text, "html.parser")
        # the div containting the game title has the class name" gameListRowItemName ellipsis"
        # this doesn't seem to be working so I'll try local instead
        #GameFind = doc.find_all(text="Revival") 
        #print(GameFind)

        
        


        # 
    #else:
    #    sys.exit()


######## was in use
#getGameUUID()
######## was in use


###################################################################################################


        # this where the "css selector" part comes in, have to use firefox to hopefully get valid css path string
        # loadToBeaut.contents contains all the html
        # in firefox dev tools I found the section I wanted, right clicked, went to copy sub-menu and selected
        # 'css selector' but that didn't give ma a whole thing with '>' which I thought it would have, just #delayedimage_game_logo_1025480_0, that's it
        # so I tried 'css path' sintead and got this
        # html.responsive body.flat_page.migrated_profile_page.responsive_page div.responsive_page_frame.with_header div.responsive_page_content div#responsive_page_template_content.responsive_page_template_content div.pagecontent.no_header div#BG_bottom.maincontent div#mainContents div#tabs_basebg.games_list div#games_list_row_container div#games_list_rows div#game_1025480.gameListRow div.gameListRowLogo a img#delayedimage_game_logo_1025480_0.game_capsule
        # so i'm going to try that one and see what happens
        # this does not work
        # uuidOfGameElem = loadToBeaut.select('html.responsive body.flat_page.migrated_profile_page.responsive_page div.responsive_page_frame.with_header div.responsive_page_content div#responsive_page_template_content.responsive_page_template_content div.pagecontent.no_header div#BG_bottom.maincontent div#mainContents div#tabs_basebg.games_list div#games_list_row_container div#games_list_rows div#game_1025480.gameListRow')
        # my list of unsuccessful attempts
        # uuidOfGameElem[0].text.strip()
        # loadToBeaut.select()
        # loadToBeaut.select('div') # this actually had several thousand results in IDLE
        # loadToBeaut.find_all(name='div',text='id')
        # loadToBeaut.has_attr('id')
        # loadToBeaut.ROOT_TAG_NAME # actually returned " '[document]' "
        # loadToBeaut.select('#delayedimage_game_logo_1025480_0')
        # loadToBeaut.find(name='div',attrs='games_list_row_container')
        # uuidOfGameElem = loadToBeaut
        # I decided to watch this playlist on beautiful soup 4 in particular:
        # https://www.youtube.com/watch?v=gRLHr664tXA&list=PLzMcBGfZo4-lSq2IDrA6vpZEV92AmQfJK
        # doesn't hurt that it's from 2021 rather than 2015






################################# MORE NOTES - PARSING HTML ON LOCAL DRIVE (VIDEO ONE)
#        with open("saved-library-page.html", "r") as f:
#            doc = BeautifulSoup(f, "html.parser")
    # print(doc) # just displays the whole thing
    # print(doc.prettify()) # this version just makes it indented and look a little better
    # in " tag = doc.title " title didn't come up in the intellisense thing but this works for print:
    # output:
    # <title>Steam Community :: subassy :: Games</title>
    ########tag = doc.title # just gets first instance of tag, 
    # print(tab.string) # would also work
    # can also use tag.string = "hello" to over-write the title tag content
    ##########print(tag)
#    tag = doc.find_all("img") # grabs all the image tags
    #tagcount = tag.count()
#    tagImage = doc.find_all("img")[0] # displays only first image tag
#    print(tagImage)

        #print(str(testResult)) # convert to string unecessary in this case
        # print(testResult) # debug test to make sure it was getting here
        #getLibraryPage = requests.get(STEAM_LIBRARY_URL) # variable now holds entire contents of the URL
        #loadToBeaut = bs4.BeautifulSoup(getLibraryPage.text, 'html.parser') # don't forget the parser part
        # following the youtube video I'm going to laod the HTML page locally
        # saved-library-page.html
        # C:\Users\Keith\Documents\repos\ReallyHadtoPython\SteamScraper\saved-library-page.html