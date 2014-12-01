import urllib
import urllib2
import mechanize
from BeautifulSoup import BeautifulSoup
from urlparse import urlparse
import hashlib

def searchPic(term):
    img_list = getPic(term)
    if len(img_list)>0:
        for img in img_list:
            savePic(img)
    print "done..." 

def getPic (search):
    search = search.replace(" ","%20")
    try:
        browser = mechanize.Browser()
        browser.set_handle_robots(False)

        #browser.set_debug_http(True)
        #browser.set_debug_redirects(True)
        #browser.set_debug_responses(True)

        # ---> REPLACE BY YOUR OWN USER AGENT ! <--- http://whatsmyuseragent.com/
        browser.addheaders = [('User-agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0')]
        

        #htmltext = browser.open('https://www.google.com/search?safe=off&hl=fr&site=imghp&tbm=isch&source=hp&biw=1920&bih=895&q='+search+'&oq='+search+'#q='+search+'&safe=off&hl=fr&tbm=isch&tbs=isz:l')
        
        query_args = {'q':search, 'safe':'on', 'tbm':'isch'}
        isz = {'tbs':'isz'}#urlencode doesn't work with the ':' part of the argument
        
        #unused criterion
        #hl':'fr', 'site':'imghp', 'source':'hp', 'biw':'1920', 'bih':'895','q':'poulet','oq':'poulet'}
  
        encoded_args = urllib.urlencode(query_args)
        encoded_isz = urllib.urlencode(isz)
        url = 'https://www.google.com/search?'+encoded_args+'&'+encoded_isz+':l'
        htmltext = browser.open(url)
        html = htmltext.read()

        img_urls = []
        formatted_images = []
        
        soup = BeautifulSoup(html)
        print soup
        results = soup.findAll("a")

        for r in results:
            try:
                if "imgres?imgurl" in r['href']:
                    img_urls.append(r['href'])
            except:
                a=0
        for im in img_urls:
            refer_url = urlparse(str(im))
            image_f = refer_url.query.split("&")[0].replace("imgurl=","")
            formatted_images.append(image_f)
        
        return formatted_images

    except:
        return []

def savePic(url):
    hs = hashlib.sha224(url).hexdigest()
    file_extension = url.split(".")[-1]
    uri = ""
    dest = uri+hs+"."+file_extension
    print dest
    try:
        urllib.urlretrieve(url,dest)
    except:
        print "save failed" 

searchPic("poulet")
