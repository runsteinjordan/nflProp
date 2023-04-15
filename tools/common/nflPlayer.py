# Import scraping modules
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Import nflProp modules
import sys
tools_path = '../tools/common/'
sys.path.append(tools_path)
from pro_football_ref_scraper import *

class nflPlayer:
    # last_name and first_name are strings
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name
        self.games_played = None
        self.url = getNflPlayerUrl(self.last_name, self.first_name)
        self.ypg = {'passing' : None,
                    'rush' : None,
                    'rec' : None}
        self.ypa = {'passing' : None,
                    'rush' : None,
                    'rec' : None}

