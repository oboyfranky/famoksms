import os
import sys

path = "/home/myusername/myproject"
if path not in sys.path:
    sys.path.append(path)

os.environ["DJANGO_SETTINGS_MODULE"] = "myproject.settings"