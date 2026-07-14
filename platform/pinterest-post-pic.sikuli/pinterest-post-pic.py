import sys.argv

ARG_TITLE = "TEST #pet #cat #tabbycat #france @frimoussethecat (o.o)"
ARG_IMAGE = "file:c:/Users/damien/workspace/project-frimousse-social/folder.jpg"
ARG_DESCR = "20110001 #pet #cat #tabbycat #france @frimoussethecat (o.o https://linktr.ee/frimoussethecat)"

# parameters
if len(sys.argv) > 1:
    ARG_TITLE = sys.argv[1]
    ARG_IMAGE = sys.argv[2]
    ARG_DESCR = sys.argv[3]
     
try:
    # init
    #wait("pinterest-create-button-2.png", 5)
    
    # post
    #click("pinterest-create-button-1.png")
    sleep(1)  
    #click("pinterest-pin-button.png")
    runScript("../platform/firefox-url-goto", "https://fr.pinterest.com/pin-creation-tool/")
    sleep(2)
    
    # add pict
    click("pinterest-create-upload.png")
    sleep(1)

    # select picture
    runScript("firefox-file-upload-2", ARG_IMAGE)
    sleep(3)

    # add title
    click("pinterest-create-title.png")
    paste(ARG_TITLE)
    sleep(1)

    # add description
    click("pinterest-post-form-description.png")
    paste(ARG_DESCR)
    sleep(1)

    # select board
    click("pinterest-post-form-board.png")
    sleep(1)
    click("pinterest-post-form-board-selector.png")
    sleep(1)

    # submit
    click("pinterest-create-publish-button.png")
    
finally:
    runScript("../platform/windows-takescreenshot", "-twitter") 
    keyUp()
