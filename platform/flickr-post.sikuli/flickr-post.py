import sys.argv

ARG_IMAGE = "file:c:/Users/damien/workspace/project-frimousse-social/20240626_111533-compressed.jpg"
ARG_TITLE = "20240626_111533 - Meow in Nantes, FRANCE"
ARG_DESCR = "20240626_111533 - Meow in Nantes, FRANCE. Check me at https://linktr.ee/frimoussethecat #pet #cat #france #frimoussethecat"

# parameters
if len(sys.argv) > 1:
    ARG_TITLE = sys.argv[1]
    ARG_IMAGE = sys.argv[2]
    ARG_DESCR = sys.argv[3]

try:

    # post
    click("flickr-post-create-2.png")
    sleep(1)

    # upload picture
    click("flickr-file-upload.png")
    sleep(1)

    # select picture
    runScript("firefox-file-upload-2", ARG_IMAGE)
    sleep(1)

    # type description
    click("flickr-post-desc.png")
    paste(ARG_DESCR)
    
    # type title
    type(Key.TAB, KeyModifier.SHIFT)
    paste(ARG_TITLE)

    # submit
    click("flickr-post-submit-1.png")
    sleep(2)    
    click("flickr-post-submit2.png")
    sleep(1)

    # success
    wait("flickr-post-continue.png")
    click("flickr-post-continue-1.png")
    
finally:
    runScript("../platform/windows-takescreenshot", "-flickr")
    keyUp()
