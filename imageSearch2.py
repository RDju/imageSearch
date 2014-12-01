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

        browser.addheaders = [('User-agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0')]
        htmltext = browser.open('https://www.google.com/search?safe=off&hl=fr&site=imghp&tbm=isch&source=hp&biw=1920&bih=895&q='+search+'&oq='+search+'#q='+search+'&safe=off&hl=fr&tbm=isch&tbs=isz:l')
        html =  htmltext.read()

        query_args = {'safe':'on', 'hl':'fr', 'site':'imghp', 'tbm':'isch', 'source':'hp', 'biw':'1920', 'bih':'895','q':'poulet','oq':'poulet', 'tbs':'isz:l'}
        encoded_args = urllib.urlencode(query_args)
        url = 'https://www.google.com/search'
        print urllib2.urlopen(url, encoded_args).read()
        
        #print html

        img_urls = []
        formatted_images = []
        
        soup = BeautifulSoup(html)
        results = soup.findAll("a")
        #print results
        #results = soup.findAll("img")
        #print results

        for r in results:
            try:
                if "imgres?imgurl" in r['href']:
                    img_urls.append(r['href'])
                    #print r['href']
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
