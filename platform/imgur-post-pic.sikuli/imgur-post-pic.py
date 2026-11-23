import sys.argv

ARG_TITLE = "TEST #pet #cat #tabbycat #france @frimoussethecat (o.o)"
ARG_IMAGE = "file:C:\Windows\Web\Wallpaper\Windows\img0.jpg"
ARG_DESCR = "20110001 #pet #cat #tabbycat #france @frimoussethecat (o.o https://linktr.ee/frimoussethecat)"

# parameters
if len(sys.argv) > 1:
    ARG_TITLE = sys.argv[1]
    ARG_IMAGE = sys.argv[2]
    ARG_DESCR = sys.argv[3]
    
try:
    # post
    click("imgur-post-pic-create.png")
    sleep(1)

    # add pict
    click("imgur-post-pic-create-upload.png")
    sleep(1)

    # select picture
    runScript("firefox-file-upload-2", ARG_IMAGE)
    sleep(3)

    # upload error
    if exists("imgur-post-pic-create-upload-error.png"):
        # add pict
        click("imgur-post-pic-create-upload.png")
        sleep(1)
        
        # select picture
        runScript("firefox-file-upload-2", ARG_IMAGE)
        sleep(3) 
    
    # add title
    click("imgur-post-pic-title.png")
    paste(ARG_TITLE)
    sleep(1)

    # add title
    click("imgur-post-form-description.png")
    paste(ARG_DESCR)
    sleep(1)

    # submit
    click("imgur-post-pic-publish.png")
    sleep(1)
    
    click("imgur-post-pic-confirm.png")
    
finally:
    runScript("../platform/windows-takescreenshot", "-imgur") 
    keyUp()
