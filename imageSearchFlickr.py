import flickr,os #download flickr.py at https://code.google.com/p/flickrpy/ and put in the same folder
import sys
import urllib
import hashlib    
from rauth import OAuth1Service

#find public image from a given user
def search_by_user(name):
    user = flickr.people_findByUsername(name)
    photoList = flickr.people_getPublicPhotos(user.id)
    urls = []

    for photo in photoList:
        urls.append(getURL(photo, 'Large', False))

    for url in urls:
        print url

#find all our photos
def search_perso():
    flickr.email = 'sparkling.wall@yahoo.fr'
    flickr.password = 'thewall2014'
    
    #To do only the first time
    if (False):
        permission = "read"
        myAuth = flickr.Auth()
        frob = myAuth.getFrob()
        link = myAuth.loginLink(permission,frob)
        raw_input("Please make sure you are logged into Flickr in Firefox")
        firefox=os.popen('firefox \"'+link+'\"')
        raw_input("A Firefox window should have opened. Press enter when you have authorized this program to access your account")
        token = myAuth.getToken(frob)
        f = file('token.txt','w')
        f.write(token)
        f.close()


    #user = flickr.people_findByEmail(flickr.email)
    user = flickr.test_login()
    print user.username
    photoList = flickr.photos_search(user.id, True, '')#can be used to search by theme
    
    urls = []
    for photo in photoList:
        urls.append(getURL(photo, 'Large', False))

    for url in urls:
        print url

#search images by tag on all the site
def search_by_tag(tag, number):
    photoList = flickr.photos_search('', False, tag, '', '', '', '', '', '', '', number, 1)
    
    urls = []
    for photo in photoList:
        urls.append(getURL(photo, 'Large', False))

        for url in urls:
            print url



#return the URL of a photo 
def getURL(photo, size, equal=False):
    method = 'flickr.photos.getSizes'
    data = flickr._doget(method, photo_id=photo.id)
    for psize in data.rsp.sizes.size:
        if psize.label == size:
            if equal and psize.width == psize.height:
                return psize.source
            elif not equal:
                return psize.source
    raise flickr.FlickrError, "No URL found"




#search_by_user('sparkling.wall')
#search_perso()
search_by_tag('poulet', 10)
