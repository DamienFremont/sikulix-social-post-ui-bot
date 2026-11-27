# NOTE: Press Alt+Shift+C to to kill a running Sikuli script.

# CONST
ARG_IMAGE = "20260206_152100-gb.512.png"
ARG_TITLE = "Testing stuff..."
ARG_DESCR = " #gamedev #retro #demake"
ARG_PATH = "file:c:/Users/damien/workspace/project-demake/_MARKETING/"
FF_CONT = "5"

# VARS
POST_IMAGE = ARG_PATH + ARG_IMAGE
POST_TITLE = ARG_TITLE
POST_DESCR = ARG_DESCR
POST_TEXT =  ARG_TITLE + ARG_DESCR

try:
    # START ***********************************************
    
    # browser
    runScript("../platform/cmd-run", 'firefox')    
    runScript("../platform/windows-fullscreen")
    
    # facebook
    runScript("../platform/firefox-container-new", FF_CONT)
    runScript("../platform/facebook-open")
    runScript("../platform/facebook-post", POST_TEXT, POST_IMAGE)
    
    # instagram
    runScript("../platform/firefox-container-new", FF_CONT)
    runScript("../platform/instagram-open")
    runScript("../platform/instagram-post", POST_TEXT, POST_IMAGE)
    
    # twitter
    runScript("../platform/firefox-container-new", FF_CONT)
    runScript("../platform/twitter-open")
    runScript("../platform/twitter-post", POST_TEXT, POST_IMAGE)

    # pinterest
    #runScript("../platform/firefox-container-new", ARG_FFC_ID)
    #runScript("../platform/pinterest-open")
    #runScript("../platform/pinterest-post-pic", ARG_TEXT, ARG_IMAGE)
    
    # imgur
    #runScript("../platform/firefox-container-new", ARG_FFC_ID)
    #runScript("../platform/imgur-open")
    #runScript("../platform/imgur-post-pic", ARG_TEXT, ARG_IMAGE)
    
    # tumblr
    #runScript("../platform/firefox-container-new", FF_CONT)
    #runScript("../platform/tumblr-open")
    #runScript("../platform/tumblr-post", POST_TEXT, POST_IMAGE)
 
    # flickr
    #runScript("../platform/firefox-container-new", FF_CONT)
    #runScript("../platform/flickr-open")
    #runScript("../platform/flickr-post", POST_TITLE, POST_IMAGE, POST_DESCR)
    
    # mastodon
    #runScript("../platform/firefox-container-new", FF_CONT)
    #runScript("../platform/mastodon-open")
    #runScript("../platform/mastodon-post", POST_TEXT, POST_IMAGE)

    # cara
    #runScript("../platform/firefox-container-new", FF_CONT)
    #runScript("../platform/cara-open")
    #runScript("../platform/cara-post", POST_TEXT, POST_IMAGE)
    # FIXME next: empty tab 
    sleep(5)
    
    # threads
    #runScript("../platform/firefox-container-new", FF_CONT)
    #runScript("../platform/threads-open")
    #runScript("../platform/threads-post", POST_TEXT, POST_IMAGE)   
    
    # bluesky
    #runScript("../platform/firefox-container-new", FF_CONT)
    #runScript("../platform/firefox-url-goto", "https://bsky.app/profile/frimoussethecat.bsky.social")

    # CHECK ***********************************************
    
    # browser    
    #runScript("../platform/cmd-run", 'firefox')
    # sites

    
    # END ***********************************************
finally:
    runScript("../platform/windows-takescreenshot", "-frimoussethecat")
    keyUp()

# browser
#runScript("../platform/window-close.sikuli")
