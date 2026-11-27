import sys.argv

ARG_TEXT = "20220904_185838 #pet #cat #tabbycat #france @frimoussethecat (o.o)"
ARG_IMAGE = "file:C:\Windows\Web\Wallpaper\Windows\img0.jpg"

# parameters
if len(sys.argv) > 1:
    ARG_TEXT = sys.argv[1]
    ARG_IMAGE = sys.argv[2]
    
try:

    # check
    wait("tw-post-create-btn.png")
    sleep(1)

    # create
    click("tw-post-create-btn.png")
    wait("twitter-post-text-area-2.png",5)

    # add pict
    sleep(2)    
    click("tw-post-add-img.png")
    sleep(1)
        
    # select picture
    runScript("firefox-file-upload-2", ARG_IMAGE)
    sleep(3)

    # add text
    wait("twitter-post-text-area-3.png",5)
    click("twitter-post-text-area-3.png")
    runScript("../platform/windows-typelikehuman", ARG_TEXT)
    sleep(1)
    type(Key.ENTER)

    # submit
    click("tw-post-submit-btn.png")

finally:
    runScript("../platform/windows-takescreenshot", "-twitter") 
    keyUp()
