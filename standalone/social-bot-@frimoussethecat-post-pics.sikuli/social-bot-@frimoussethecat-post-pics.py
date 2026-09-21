# NOTE: Press Alt+Shift+C to to kill a running Sikuli script.

# CONST
ARG_ID    = "20240719_220112"
ARG_TEXT  = " - Frimousse, 14 years old, in Nantes, FRANCE. #pet #cat #france #frimoussethecat"
ARG_TITLE = " - Frimousse, 14 years old, in Nantes, FRANCE."
ARG_DESCR = " - Check me at https://linktr.ee/frimoussethecat #pet #cat #france #frimoussethecat"
ARG_PATH = "file:c:/Users/damien/workspace/project-frimousse-social/"
FF_CONT = "4"

# VARS
POST_IMAGE = ARG_PATH + ARG_ID + "-compressed.jpg"
POST_TEXT =  ARG_ID + ARG_TEXT
POST_TITLE = ARG_ID + ARG_TITLE
POST_DESCR = ARG_ID + ARG_DESCR

try:
    # START ***********************************************
    
    # browser
    runScript("../platform/cmd-run", 'firefox')    
    runScript("../platform/windows-maximize")
    
    # Facebook
    runScript("../platform/firefox-container-new", FF_CONT)
    runScript("../platform/facebook-open")
    runScript("../platform/facebook-post", POST_TEXT, POST_IMAGE)
    
    # Instagram
    runScript("../platform/firefox-container-new", FF_CONT)
    runScript("../platform/instagram-open")
    runScript("../platform/instagram-post", POST_TEXT, POST_IMAGE)
    
    # X/Twitter
    runScript("../platform/firefox-container-new", FF_CONT)
    runScript("../platform/twitter-open")
    runScript("../platform/twitter-post", POST_TEXT, POST_IMAGE)

    # Pinterest
    #runScript("../platform/firefox-container-new", ARG_FFC_ID)
    #runScript("../platform/pinterest-open")
    #runScript("../platform/pinterest-post-pic", ARG_TXT, ARG_IMG_FN)
    
    # Imgur
    #runScript("../platform/firefox-container-new", ARG_FFC_ID)
    #runScript("../platform/imgur-open")
    #runScript("../platform/imgur-post-pic", ARG_TXT, ARG_IMG_FN)
    
    # Tumblr
    runScript("../platform/firefox-container-new", FF_CONT)
    runScript("../platform/tumblr-open")
    runScript("../platform/tumblr-post", POST_TEXT, POST_IMAGE)
 
    # Flickr
    runScript("../platform/firefox-container-new", FF_CONT)
    runScript("../platform/flickr-open")
    runScript("../platform/flickr-post", POST_TITLE, POST_IMAGE, POST_DESCR)
    
    # Mastodon
    runScript("../platform/firefox-container-new", FF_CONT)
    runScript("../platform/mastodon-open")
    runScript("../platform/mastodon-post", POST_TEXT, POST_IMAGE)

    # Cara
    runScript("../platform/firefox-container-new", FF_CONT)
    runScript("../platform/cara-open")
    runScript("../platform/cara-post", POST_TEXT, POST_IMAGE)
    # FIXME next: empty tab 
    sleep(5)
    
    # Threads
    runScript("../platform/firefox-container-new", FF_CONT)
    runScript("../platform/threads-open")
    runScript("../platform/threads-post", POST_TEXT, POST_IMAGE)   
    
    # Bluesky
    #runScript("../platform/firefox-container-new", FF_CONT)
    #runScript("../platform/firefox-url-goto", "https://bsky.app/profile/frimoussethecat.bsky.social")
    
    # END ***********************************************
    
finally:
    runScript("../platform/windows-takescreenshot", "-frimoussethecat")
    keyUp()

# CHECK ***********************************************

# browser    
runScript("../platform/cmd-run", 'firefox')

# sites
runScript("../platform/firefox-cont-new-url", FF_CONT, "https://www.facebook.com/frimoussethecat/")
runScript("../platform/firefox-cont-new-url", FF_CONT, "https://www.instagram.com/frimousse_the_cat/")
runScript("../platform/firefox-cont-new-url", FF_CONT, "https://x.com/frimoussethecat")
#runScript("../platform/firefox-cont-new-url", FF_CONT, "https://fr.pinterest.com/frimoussethecat/_pins/")
#runScript("../platform/firefox-cont-new-url", FF_CONT, "https://imgur.com/user/frimoussethecat/")
runScript("../platform/firefox-cont-new-url", FF_CONT, "https://www.tumblr.com/blog/frimoussethecat")
runScript("../platform/firefox-cont-new-url", FF_CONT, "https://www.flickr.com/photos/frimoussethecat/")
runScript("../platform/firefox-cont-new-url", FF_CONT, "https://mastodon.social/@frimoussethecat")
runScript("../platform/firefox-cont-new-url", FF_CONT, "https://cara.app/home")
runScript("../platform/firefox-cont-new-url", FF_CONT, "https://www.threads.com/@frimousse_the_cat")
#runScript("../platform/firefox-cont-new-url", FF_CONT, "https://bsky.app/profile/frimoussethecat.bsky.social")
