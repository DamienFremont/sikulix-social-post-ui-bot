import sys.argv

ARG_TEXT = "This is a test."
ARG_DELAY = "0.1"

# parameters
if len(sys.argv) > 1:
    ARG_TEXT = sys.argv[1]
if len(sys.argv) > 2:
    ARG_DELAY = sys.argv[2]

# type text
Settings.TypeDelay = float(ARG_DELAY)
type(ARG_TEXT)
sleep(1)
