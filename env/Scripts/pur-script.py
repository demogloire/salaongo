#!e:\joshua\app\salaongo\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pur==5.3.0','console_scripts','pur'
__requires__ = 'pur==5.3.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pur==5.3.0', 'console_scripts', 'pur')()
    )
