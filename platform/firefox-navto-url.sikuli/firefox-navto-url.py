# NOTE: Press Alt+Shift+C to to kill a running Sikuli script.

# PARAMETERS
PARAM_URL = "C:/Users/damien/Downloads/linkedIn/"
if len(sys.argv) > 0:
    PARAM_URL = sys.argv[1]

# nav to url
type("l", KeyModifier.CTRL)
paste(PARAM_URL)
type(Key.ENTER)

# wait loading
sleep(1)

# unfocus
type(Key.ESC)
