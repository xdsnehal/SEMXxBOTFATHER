
import glob
from pathlib import Path
from SemxXSpam.utils import load_plugins
import logging
from . import MK
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "SemxXSpam/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Semx X BotSpam Successfully Deployed !!")
print("Enjoy..!  Do Visit @HACKERxSPAM")

if __name__ == "__main__":
    MK.run_until_disconnected()
   
