import bs4, requests 

# STEAM_LIBRARY_URL = "https://steamcommunity.com/id/subassy/games/?tab=all"
STEAM_LIBRARY_URL = "https://steeeeamcommmmmmunity.com/id/subassy/games/?tab=all"

def testLibURL(LibraryURL):
    testExists = requests.get(LibraryURL)
#    try:
    return testExists.raise_for_status()
#    except: break



#def getGameUUID():
#    soup = bs4.BeautifulSoup(file.txt, 'html.parser')

#print(testLibURL(STEAM_LIBRARY_URL))

