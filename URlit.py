import pyshorteners as ps
url=input('Enter the url to shorten it: ')
def shortenurl(url):
    s= ps.Shortener()
    print("Short url: " , s.tinyurl.short(url))
    
shortenurl(url)