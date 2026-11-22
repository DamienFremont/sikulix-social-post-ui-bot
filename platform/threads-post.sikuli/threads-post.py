import sys.argv

ARG_TXT = "20220730_220243 #pet #cat #tabbycat #france @frimoussethecat (o.o)"
ARG_IMG_FN = "file:c:/Users/damien/SynologyDrive/workdir/project-frimousse-social/20220730_220243-compressed.jpg"

# parameters
if len(sys.argv) > 1:
    ARG_TXT = sys.argv[1]
    ARG_IMG_FN = sys.argv[2]
    
try:

    # page loaded
    wait("threads-post-create-2.png", 30)
    
    # post
    click("threads-post-create-2.png")
    
    # add text
    sleep(1)
    paste(ARG_TXT)
    
    # upload picture
    click("threads-post-upload.png")
    sleep(1)
    
    # select picture
    runScript("firefox-file-upload-2", ARG_IMG_FN)
    sleep(3)
    
    # submit
    click("threads-post-confirm4.png")   

finally:
    runScript("../platform/windows-takescreenshot", "-threads")
    keyUp()
