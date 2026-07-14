import sys.argv

ARG_TXT = "20220730_220243 #pet #cat #tabbycat #france @frimoussethecat (o.o)"
ARG_IMG_FN = "file:c:/Users/damien/SynologyDrive/workdir/project-frimousse-social/20220730_220243-compressed.jpg"

# parameters
if len(sys.argv) > 1:
    ARG_TXT = sys.argv[1]
    ARG_IMG_FN = sys.argv[2]

try:

    # page loaded
    wait("fb-post-create.png", 30)
    
    # post
    click("fb-post-create.png")
    sleep(1)

    # upload picture
    type(Key.TAB)
    type(Key.TAB)
    type(Key.ENTER)
    sleep(2)
        
    # select picture
    runScript("firefox-file-upload-2", ARG_IMG_FN)
    sleep(2)
   
    # add text
    paste(ARG_TXT)
    sleep(1)
    
    # submit
    #click("facebook-post-next.png")
    sleep(3)    
    click("facebook-post-confirm.png")
    sleep(1)
        
finally:
    runScript("../platform/windows-takescreenshot", "-facebook")
    keyUp()
