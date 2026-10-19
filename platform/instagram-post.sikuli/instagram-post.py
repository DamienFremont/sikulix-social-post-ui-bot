import sys.argv

ARG_TXT = "20230611_222051 #pet #cat #tabbycat #france @frimoussethecat (o.o)"
ARG_IMG_FN = "file:c:/Users/damien/SynologyDrive/workdir/project-frimousse-social/20230611_222051-compressed.jpg"

# parameters
if len(sys.argv) > 1:
    ARG_TXT = sys.argv[1]
    ARG_IMG_FN = sys.argv[2]

try:

    # page loaded
    wait("insta-menu.png", 30)
    
    # post

    mouseMove("insta-menu-2.png")
    
    click("insta-post-create-btn.png")
    sleep(1)
    
    # upload picture
    click("insta-post-upload.png")
    sleep(1)
    
    # select picture
    runScript("firefox-file-upload-2", ARG_IMG_FN)
    sleep(1)
    
    # next...
    click("insta-post-next.png")
    sleep(2)
    click("insta-post-next.png")
    sleep(2)
    
    # type text
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    paste(ARG_TXT)
        
    # submit
    click("insta-post-submit.png")
    
    # SUCCESS
    wait("insta-post-submit-confirm.png", 30)    
    sleep(1)
    wait("insta-post-submit-check.png", 30)

finally:
    runScript("../platform/windows-takescreenshot", "-instagram")
    keyUp()
