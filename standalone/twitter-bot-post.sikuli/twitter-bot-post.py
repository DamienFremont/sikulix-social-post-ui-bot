# NOTE: Press Alt+Shift+C to to kill a running Sikuli script.

ARG_TEXT = "20210112_233929 #pet #cat #tabbycat @frimoussethecat (o.o)"
ARG_IMAGE = "file://///192.168.8.2/workdir/project-frimousse-social/20210112_233929-compressed.jpg"

try:
    # start ***********************************************
    
    # browser
    runScript("../platform/cmd-run", 'firefox')

    # twitter
    runScript("../platform/firefox-mobile")
    runScript("../platform/twitter-open")
    
    # picture
    runScript("../platform/firefox-clipboard-picture", ARG_IMAGE)

    # post
    runScript("../platform/twitter-post", ARG_TEXT, "true")

    # end ***********************************************  
    runScript("../platform/windows-takescreenshot", "-success") 
except FindFailed:
    runScript("../platform/windows-takescreenshot", "-error")
finally:
    keyUp()

# browser
#runScript("../platform/window-close.sikuli")
