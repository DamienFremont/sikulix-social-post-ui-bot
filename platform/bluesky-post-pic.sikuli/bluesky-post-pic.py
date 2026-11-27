import sys.argv

ARG_TEXT = "TEST #pet #cat #tabbycat #france #frimoussethecat (o.o)"
ARG_IMAGE = "file:C:\Windows\Web\Wallpaper\Windows\img0.jpg"

# parameters
if len(sys.argv) > 1:
    ARG_TEXT = sys.argv[1]
    ARG_IMAGE = sys.argv[2]

try:
    
    # page loaded
    wait("bluesky-post-btn.png", 30)
    
    # post
    click("bluesky-post-btn-1.png")
    
    # post loaded
    wait("bluesky-post-confirm-no.png", 10)
    
    # add text
    sleep(1)
    click("bluesky-post-txt.png")
    runScript("../platform/windows-typelikehuman", ARG_TEXT)
    
    # upload picture
    click("bluesky-post-upload.png")
    sleep(1)
    
    # select picture
    runScript("firefox-file-upload-2", ARG_IMAGE)
    sleep(1)
    
    # submit
    wait("bluesky-post-confirm-yes.png", 30)
    click("bluesky-post-confirm-yes-1.png")

    # success
    sleep(1)    
    wait("bluesky-post-comfirmed.png", 3)

finally:
    runScript("../platform/windows-takescreenshot", "-bluesky") 
    keyUp()