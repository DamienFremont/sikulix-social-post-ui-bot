# NOTE: Press Alt+Shift+C to to kill a running Sikuli script.

# CONST
TARGET_DIR = "C:/Users/damien/Downloads/"
# parameters
if len(sys.argv) > 1:
    TARGET_DIR = sys.argv[1]

# browser
runScript("../platform/cmd-run", 'firefox')
    
# LOAD
type("l", KeyModifier.CTRL)
paste("https://www.linkedin.com/mynetwork/invite-connect/connections/")
type(Key.ENTER)
sleep(1)

# RESET ZOOM
type("0", Key.CTRL)
sleep(0.5)
type(Key.HOME)
sleep(0.5)

# FULL SCREEN
type(Key.F11)
VERTICAL_MARGIN_FULLSCREEN = "0"
vertMargin = VERTICAL_MARGIN_FULLSCREEN

# SCROLLING
SCROLL_BUMP = 3
scrollCounter = 0

# START
for x in range(1):
    scrollCounter = scrollCounter + 1
    
    # OPEN NEW TAB
    region = Region(450, 215 + int(vertMargin))
    rightClick(region)
    sleep(0.5)
    region = Region(470, 215 + 25 + int(vertMargin))
    rightClick(region)
    sleep(1)
    
    # SWITCH TAB
    type("2", Key.CTRL)
    
    # INIT DATAS
    runScript("../platform/linkedin-profile-getname", vertMargin)
    name = Env.getClipboard()

    # TAKE HEADER SCREENSHOT
    runScript("../platform/linkedin-profile-screenshot-head", TARGET_DIR + name + "-header.png", vertMargin)
    
    # CLOSE TAB
    type("1", Key.CTRL)
    sleep(0.5)
    
    # SCROLL
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.DOWN)
    if (scrollCounter == SCROLL_BUMP):
        type(Key.DOWN)
        scrollCounter = 0
        print("Key.DOWN screen as ")
    sleep(1)
    
# END
screen = Screen()
file = screen.saveCapture(screen.getBounds())
