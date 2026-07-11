# NOTE: using 1080p resolution
import sys.argv
import shutil

# CONST
ARG_1 = "test-head.png"
ARG_VERTICAL_MARGIN = "0"

SCREENSHOT_REGION_X1 = 400
SCREENSHOT_REGION_Y1 = 78
SCREENSHOT_REGION_X2 = 1190
SCREENSHOT_REGION_Y2 = 555

# parameters
if len(sys.argv) > 1:
    ARG_1 = sys.argv[1]
    ARG_VERTICAL_MARGIN = sys.argv[2]

# RESET ZOOM
type("0", Key.CTRL)
sleep(0.5)

# TAKE SCREENSHOTS
screen = Screen()

type(Key.HOME)
sleep(0.5)

x = SCREENSHOT_REGION_X1
y = SCREENSHOT_REGION_Y1 + int(ARG_VERTICAL_MARGIN)
w = SCREENSHOT_REGION_X2 - SCREENSHOT_REGION_X1
h = SCREENSHOT_REGION_Y2 - SCREENSHOT_REGION_Y1

region = Region(x, y, w, h)
file = screen.saveCapture(region)

# moves img to destination
shutil.move(file, ARG_1)

print("LinkedIn: Profile temp saved at: " + file)
print("LinkedIn: Profile Header saved at: " + ARG_1)