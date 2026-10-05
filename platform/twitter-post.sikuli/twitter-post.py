import sys.argv

ARG_TXT = "20220904_185838 #pet #cat #tabbycat #france @frimoussethecat (o.o)"
ARG_IMG_FN = "file:c:/Users/damien/SynologyDrive/workdir/project-frimousse-social/20220904_185838-compressed.jpg"

# parameters
if len(sys.argv) > 1:
    ARG_TXT = sys.argv[1]
    ARG_IMG_FN = sys.argv[2]
    
try:

    # post
    wait("twitter-post-text-area-2.png", 5)
    sleep(1)

    # add pict
    click("twitter-post-upload.png")
    sleep(1)
    
    # select picture
    runScript("firefox-file-upload-2", ARG_IMG_FN)
    sleep(3)

    # add text
    click("twitter-post-text-area-2.png")
    paste(ARG_TXT)
    sleep(1)
    type(Key.ENTER)

    # submit
    click("tw-post-submit-btn.png")

finally:
    runScript("../platform/windows-takescreenshot", "-twitter") 
    keyUp()
