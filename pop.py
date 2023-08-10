from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import sys, random, pdb, time, os
import logging
import argparse
import textwrap

# Configure the logger
logging.basicConfig(
    filename = 'pop.log',
    level = logging.DEBUG,
    format = '[%(levelname)s] %(asctime)s - %(message)s'
)
logger = logging.getLogger(__name__)


class Soda:
    def __init__(self, username, password, args.slowMode, args.debug, args.checkCaptcha, args.file, args.timeToWait, arga.maintainOrder, args.fizz):
        self.username = username
        self.password = password
        self.chrome_options = Options()
        self.driver = webdriver.Chrome(options = self.chrome_options)
        


if __name__ == "__main__":

    class RawTextArgumentDefaultsHelpFormatter(
        argparse.ArgumentDefaultsHelpFormatter,
        argparse.RawTextHelpFormatter
    ):
        pass
    
    # Checks if the `credentials.py` file exists.
    exists = os.path.isfile('./credentials.py')
    if not exists:
        # Inform the user that the file is missing.
        logger.info(textwrap.dedent('''
            [*] ERROR: `credentials.py` file does not exist.
                You may need to create the file, for example, 
                by copying `example_credentials.py`...

            [*] In terminal, enter the following command:
                cp example_credentials.py credentials.py

            [*] Then edit credentials.py with your
                poshmark closet and password.
                '''))
        sys.exit(-1)
    else:
        import credentials

    ## Fail gracefully if the username or password not specified in credentials.py.
    try:
        username = credentials.username
        password = credentials.password
    except AttributeError:
        # Inform the user if username and/or password is missing and provide instructions.
        logger.info(textwrap.dedent('''
            [*] ERROR: Username and/or password not specified...
            '''))
        sys.exit(-1)

    
    ## Verify that the user is using their Poshmark username and not email
    if '@' in username:
        # Inform the user to use Poshmark username for login
        logger.info(textwrap.dedent('''
                    [*] Do not use your email address to log in...
                        use your Poshmark username (closet) instead...
                    '''))
        print(textwrap.dedent('''
                    [*] Do not use your email address to log in...
                        use your Poshmark username (closet) instead...
                    '''))
        sys.exit(-1)

    # Define the argument parser with description and custom formatter
    parser = argparse.ArgumentParser(
        description=textwrap.dedent('''
        [*] Help file for pop.py
            from the depop_sharing repository:
            https://github.com/lyndskg/d3p0pp3d
        '''),
        usage = 'use "python3 %(prog)s --help" or "python3 pop.py -h" for more information',
        formatter_class=RawTextArgumentDefaultsHelpFormatter)
    
    # Add command line arguments for different options
    parser.add_argument("-d", "--debug", default = False, type = bool, required = True,
        help = "Show debug output.")
    parser.add_argument("-sm", "--slowMode", default = False, type = bool, required = True,
        help = "Run in slow mode.")
    parser.add_argument("-cc", "--checkCaptcha", default = True, type = bool, required = False,
        help = "Specify whether or not to check for Captchas.")
    parser.add_argument("-f", "--file", default = False, type = bool, required = False,
        help = textwrap.dedent('''\
            If True, the program will read the list of items to share from 'share.txt'.
           '''))
    parser.add_argument("-ttw", "--timeToWait", default = 7200, type = float, required = false, 
        help = textwrap.dedent('''\
            Time to wait between sharing sessions (in seconds).
                               
            Default: 7200 (2 hours)
            -ttw 7200
            '''))
    parser.add_argument("-mo", "--maintainOrder", default = False, type = bool, required = False,
        help = "Specify whether or not to preserve closet order based on order file.")
    parser.add_argument("-fz", "--fizz", default = False, type = bool, required = False,
        help = "Specify whether or not to share back.")

    args = parser.parse_args()
    
    pop = Soda(username, password, args.slowMode, args.debug, args.checkCaptcha, args.file, args.timeToWait, args.maintainOrder, args.fizz)

    pop.login()
    pop.share()
    pop.quit()
        