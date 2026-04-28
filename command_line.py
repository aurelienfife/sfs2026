# OS will let you interface with the operating system
import os
import sys

# Example info about the operating system
print(os.name)

# You can a command in the OS CLI by using "system"

if sys.platform == "win32":
    os.system("ipconfig")   # Windows specific
