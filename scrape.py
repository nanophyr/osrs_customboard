import urllib
from bs4 import BeautifulSoup

def ripToLines():
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    text = soup.get_text().splitlines()
    return text

def find_between( s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index( last, start)
        return s[start:end]
    except ValueError:
        return ""

def ripToLines(soup):
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    text = soup.get_text().splitlines()
    return text


#returns total level for given user
def getTotal(user):
    url = "https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player=" + user
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html,features="html.parser")
    text = ripToLines(soup)
    return find_between(str(text[0]), "," , ",")


#prints rank level exp
#print str(text[0])

