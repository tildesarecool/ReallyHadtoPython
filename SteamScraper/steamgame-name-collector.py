
from pydoc import doc
from unittest import result
from attr import attr
import bs4, requests, webbrowser, sys, pyperclip
from bs4 import BeautifulSoup


STEAM_LIBRARY_URL = "https://steamcommunity.com/id/subassy/games/?tab=all&sort=name" # my steam library
URL_TRUE = 200 # status code from "requests" that it "found the URL" thus it's as good as 'true' in this context
# STEAM_LIBRARY_URL = "https://steeeeamcommmmmmunity.com/id/subassy/games/?tab=all"

def testLibURL(LibraryURL):
    testExists = requests.get(LibraryURL)
    #print(testExists.status_code)
    return testExists.status_code # returns int, 200 means returns true; or returns 'response object'. or i'm not sure. 200 anyway
#    try:
    #return testExists.raise_for_status()
#    except: break

#################################### many hours later ####################################
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

'''
#################################### many hours later ####################################


#testLibURL(STEAM_LIBRARY_URL)

def getGameUUID():
    #soup = bs4.BeautifulSoup(file.txt, 'html.parser')
    #testResult = testLibURL(STEAM_LIBRARY_URL)
    #if testResult == URL_TRUE:
    # with open("saved-library-page.html", "r") as f:
    result = requests.get(STEAM_LIBRARY_URL) # resut.text will show whole source of page
    doc = BeautifulSoup(result.text, "html.parser")
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
    pyperclip.copy(result.text)# put contents of whatever the results.get fucntion above is downloading
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



getGameUUID()



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