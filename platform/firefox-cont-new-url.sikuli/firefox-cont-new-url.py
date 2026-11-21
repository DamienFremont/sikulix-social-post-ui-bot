import sys.argv

ARG_CONT = "1"
ARG_URL = "https://www.google.com/"

# parameters
if len(sys.argv) > 1:
    ARG_CONT = sys.argv[1]
    ARG_URL = sys.argv[2]
    
# CONTAINER ***********************************************
    
# @Deprecated 
# start container v2025
# type(arg1, KeyModifier.CTRL + KeyModifier.SHIFT)

# start container v2026
type("F", KeyModifier.ALT)
type("b")
for x in range(int(ARG_CONT)-1):
    type(Key.DOWN)
type(Key.ENTER)

# URL  ***********************************************

# focus navbar
type("l", KeyModifier.CTRL)
sleep(0.5)

# copy URL
paste(ARG_URL)
type(Key.ENTER)

# unfocus navbar
#type(Key.ESC)
#sleep(1)
