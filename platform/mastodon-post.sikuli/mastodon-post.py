import sys.argv

ARG_TXT = "20220730_220243 #pet #cat #tabbycat #france @frimoussethecat (o.o)"
ARG_IMG_FN = "file:c:/Users/damien/SynologyDrive/workdir/project-frimousse-social/20220730_220243-compressed.jpg"

# parameters
if len(sys.argv) > 1:
    ARG_TXT = sys.argv[1]
    ARG_IMG_FN = sys.argv[2]

try:
    
    # post
    click("mastodon-post-create2.png")

    # add text
    sleep(1)
    runScript("../platform/windows-typelikehuman", ARG_TXT)
    sleep(1)
    type(Key.SPACE)
    
    # upload picture
    click("20261121_182048.png")
    sleep(1)
    
    # select picture
    runScript("firefox-file-upload-2", ARG_IMG_FN)
    sleep(3)    
            
    # submit
    click("mastodon-post-confirm.png")
    
    # access
    click("mastodon-post-access-3.png")
    sleep(1)


    # check upload
    #wait("mastodon-post-check.png", 120)
    
finally:
    runScript("../platform/windows-takescreenshot", "-mastodon")
    keyUp()

