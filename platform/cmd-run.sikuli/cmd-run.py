# TODO: DELETE ME

import sys.argv

arg1 = "firefox"

# parameters
if len(sys.argv) > 1:
    arg1 = sys.argv[1]

# open run
type("r", KeyModifier.WIN)

sleep(1)

# run cmd
paste(arg1)
type(Key.ENTER)

# wait
sleep(1)