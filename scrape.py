import urllib
from bs4 import BeautifulSoup

def find_between( s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index( last, start)
        return s[start:end]
    except ValueError:
        return ""

url = "https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player=nanoluck"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html,features="html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out


text = soup.get_text().splitlines()
#prints rank level exp
#print str(text[0])

#gets total level line 
print find_between(str(text[0]), "," , ",")
