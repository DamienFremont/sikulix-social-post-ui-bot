# NOTE: Press Alt+Shift+C to to kill a running Sikuli script.

# PARAMETERS
PARAM_TARGET_DIR = "C:/Users/damien/Downloads/linkedIn/"
PARAM_PROFILES_TODO = 20
PARAM_PROFILES_SKIP = 0
PARAM_SKIP_NAVTO = True
if len(sys.argv) > 2:
    PARAM_TARGET_DIR = sys.argv[1]
    PARAM_PROFILES_TODO = sys.argv[2]
    PARAM_PROFILES_SKIP = sys.argv[3]

# INIT TARGET FOLDER **********************************************************

if not os.path.exists(PARAM_TARGET_DIR):
    os.makedirs(PARAM_TARGET_DIR)
 
if PARAM_SKIP_NAVTO == False:
        
    # INIT BROWSER ****************************************************************    
    runScript("../platform/cmd-run", 'firefox')    
    runScript("../platform/windows-maximize")
    runScript("../platform/windows-fullscreen")
    runScript("../platform/firefox-navto-url", "https://www.linkedin.com/")
    runScript("../platform/firefox-zoom-0")
    
    # GET LINKEDIN CONNECTIONS ****************************************************
    runScript("../platform/firefox-navto-url", "https://www.linkedin.com/mynetwork/invite-connect/connections/")

# MARGIN TOP
VERTICAL_MARGIN_FULLSCREEN = "0"
vertMargin = VERTICAL_MARGIN_FULLSCREEN

# SCROLLING
SCROLL_BUMP_EVERY_OTHER_PROFIL = 3
profil_scroll_iteration = 0

# SKIP PROFILES ***************************************************************

# FOCUS BODY / UNFOCUS HEADER
BODY_FOCUS_REGION_X = 300
BODY_FOCUS_REGION_Y = 330
location = Location(BODY_FOCUS_REGION_X, BODY_FOCUS_REGION_Y + int(vertMargin))
click(location)

# SCROLL PROFILES
print("LinkedIn: scrool prepare")    
type(Key.DOWN)
type(Key.DOWN)
type(Key.DOWN)
type(Key.DOWN)

for x in range(PARAM_PROFILES_SKIP):
    profil_scroll_iteration = profil_scroll_iteration + 1    
    
    # SCROLL NEXT PROFILE
    print("LinkedIn: scrool to next profil")        
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.DOWN)
    if (profil_scroll_iteration == SCROLL_BUMP_EVERY_OTHER_PROFIL):
        type(Key.DOWN)
        profil_scroll_iteration = 0
    sleep(1)

# DOWNLOAD PROFILES ***********************************************************

for x in range(PARAM_PROFILES_TODO):
    profil_scroll_iteration = profil_scroll_iteration + 1

    # OPEN LINKEDIN PROFILE ***************************************************
    
    # OPEN NEW TAB
    # select profil
    region = Region(460, 110 + int(vertMargin))
    # emulate middle click or ctrl+click
    rightClick(region)
    sleep(0.5)
    region = Region(460, 110 + 25 + int(vertMargin))
    rightClick(region)
    sleep(1)
    # switch to new tab
    type("2", Key.CTRL)
    
    # SAVE LINKEDIN PROFILE INFOS *********************************************
    
    # INIT
    # TODO: runScript("../platform/firefox-current-url")
    #url = Env.getClipboard()
    runScript("../platform/linkedin-profile-getname", vertMargin)
    name = Env.getClipboard()
    # TODO: external script ?
    # Encoding with ASCII and replacing errors - DATA ALTERED!
    message_text.encode('utf-8')
    ascii_bytes_replaced = message_text.encode('ascii', errors='replace')
    questionmark_replaced = ascii_bytes_replaced.replace("?", "");
    name = questionmark_replaced
    
    # SAVE DATAS
    # TAKE HEADER SCREENSHOT    
    runScript("../platform/linkedin-profile-screenshot-head", PARAM_TARGET_DIR + name + "-header.png", vertMargin)
    # TODO: TAKE THUMBNAIL SCREENSHOT
    # TODO: DOWNLOAD CV /details/experience/
            
    # NEXT LINKEDIN PROFILE ***************************************************
    
    # CLOSE TAB
    type("1", Key.CTRL)
    sleep(0.5)
    
    # SCROLL NEXT PROFILE
    print("LinkedIn: scrool to next profil")    
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.DOWN)
    if (profil_scroll_iteration == SCROLL_BUMP_EVERY_OTHER_PROFIL):
        type(Key.DOWN)
        profil_scroll_iteration = 0
    sleep(1)
    
# END
screen = Screen()
file = screen.saveCapture(screen.getBounds())
