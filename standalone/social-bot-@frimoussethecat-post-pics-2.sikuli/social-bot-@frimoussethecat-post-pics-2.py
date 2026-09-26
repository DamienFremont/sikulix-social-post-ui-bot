# NOTE: Press Alt+Shift+C to to kill a running Sikuli script.

# CONST
ARG_BATCH_IDS = [ "20240707_183723-2", "20240719_220112-2" ]
ARG_BATCH_TEXT  = " - Meow in Nantes, FRANCE. #pet #cat #france #frimoussethecat"
ARG_BATCH_TITLE = " - Meow in Nantes, FRANCE"
ARG_BATCH_DESCR = " - Check me at https://linktr.ee/frimoussethecat #pet #cat #france #frimoussethecat"
ARG_BATCH_PATH = "file:c:/Users/damien/workspace/project-frimousse-social/2024/"
FF_CONT = "4"

# START ***********************************************

# browser
runScript("../platform/cmd-run", 'firefox')
runScript("../platform/windows-maximize")

for POST_ID in ARG_BATCH_IDS:    
    # VARS
    POST_IMAGE = ARG_BATCH_PATH + POST_ID + "-compressed.jpg"
    POST_TEXT =  POST_ID + ARG_BATCH_TEXT
    POST_TITLE = POST_ID + ARG_BATCH_TITLE
    POST_DESCR = POST_ID + ARG_BATCH_DESCR
    
    try:
        # sites
        
        # pinterest
        runScript("../platform/firefox-container-new", FF_CONT)
        runScript("../platform/pinterest-open")
        runScript("../platform/pinterest-post-pic", POST_TITLE, POST_IMAGE, POST_DESCR)
        
        # imgur
        #runScript("../platform/firefox-container-new", FF_CONT)
        #runScript("../platform/imgur-open")
        #runScript("../platform/imgur-post-pic", POST_TITLE, POST_IMAGE, POST_DESCR)
    
        # bluesky
        runScript("../platform/firefox-container-new", FF_CONT)
        runScript("../platform/bluesky-open")
        runScript("../platform/bluesky-post-pic", POST_TEXT, POST_IMAGE)
        
    finally:
        runScript("../platform/windows-takescreenshot", "-frimoussethecat")
        keyUp()

# CHECK ***********************************************
        
# browser
runScript("../platform/cmd-run", 'firefox')

# sites
runScript("../platform/firefox-cont-new-url", FF_CONT, "https://fr.pinterest.com/frimoussethecat/_pins/")
runScript("../platform/firefox-cont-new-url", FF_CONT, "https://imgur.com/user/frimoussethecat/")
runScript("../platform/firefox-cont-new-url", FF_CONT, "https://bsky.app/profile/frimoussethecat.bsky.social")
