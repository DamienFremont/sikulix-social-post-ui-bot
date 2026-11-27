import sys.argv

ARG_TEXT = "20220730_220243 #pet #cat #tabbycat #france @frimoussethecat (o.o)"
ARG_IMAGE = "file:C:\Windows\Web\Wallpaper\Windows\img0.jpg"

# parameters
if len(sys.argv) > 1:
    ARG_TEXT = sys.argv[1]
    ARG_IMAGE = sys.argv[2]

try:
    
    # post
    click("mastodon-post-create2.png")

    # add text
    sleep(1)
    runScript("../platform/windows-typelikehuman", ARG_TEXT)
    sleep(1)
    type(Key.SPACE)
    
    # upload picture
    click("20261121_182048.png")
    sleep(1)
    
    # select picture
    runScript("firefox-file-upload-2", ARG_IMAGE)
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

