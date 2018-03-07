import os
import sys

path = "/home/famoktech/management"
if path not in sys.path:
    sys.path.append(path)

os.environ["DJANGO_SETTINGS_MODULE"] = "management.settings"