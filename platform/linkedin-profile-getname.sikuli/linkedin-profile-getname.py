# NOTE: using 1080p resolution
import sys.argv
import shutil

# CONST
ARG_VERTICAL_MARGIN = "0"

# parameters
if len(sys.argv) > 1:
    ARG_VERTICAL_MARGIN = sys.argv[1]
    
# RESET SCREEN
type("0", Key.CTRL)
sleep(0.5)
type(Key.HOME)
sleep(0.5)

# SELECT NAME
location = Location(400, 360 + int(ARG_VERTICAL_MARGIN))
click(location)
click(location)
click(location)
sleep(0.5)

# COPY TEXT
type("c", Key.CTRL)
sleep(0.5)

# CLEAR SELECT
click(location)

# GET TEXT
message_text = Env.getClipboard()
print("LinkedIn: Profile Name: " +message_text)
