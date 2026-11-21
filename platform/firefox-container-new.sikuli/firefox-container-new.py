import sys.argv

arg1 = "4"

# parameters
if len(sys.argv) > 1:
    arg1 = sys.argv[1]

# @Deprecated 
# start container v2025
# type(arg1, KeyModifier.CTRL + KeyModifier.SHIFT)

# start container v2026
type("F", KeyModifier.ALT)
type("b")
for x in range(int(arg1)-1):
    type(Key.DOWN)
type(Key.ENTER)
