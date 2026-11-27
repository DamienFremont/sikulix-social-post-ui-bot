import sys.argv

ARG_TEXT = "20220730_220243 #pet #cat #tabbycat #france @frimoussethecat (o.o)"
ARG_IMAGE = "file:C:\Windows\Web\Wallpaper\Windows\img0.jpg"

# parameters
if len(sys.argv) > 1:
    ARG_TEXT = sys.argv[1]
    ARG_IMAGE = sys.argv[2]

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
    runScript("firefox-file-upload-2", ARG_IMAGE)
    sleep(2)
   
    # add text
    runScript("../platform/windows-typelikehuman", ARG_TEXT)
    sleep(1)
    
    # submit
    #click("facebook-post-next.png")
    sleep(3)    
    click("facebook-post-confirm.png")
    sleep(1)
        
finally:
    runScript("../platform/windows-takescreenshot", "-facebook")
    keyUp()
