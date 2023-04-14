# Import scraping modules
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


def getNflPlayerUrl(last_name, first_name):
    '''
    Description:
    Get a player's unique url tag based off of pro-football-reference.com naming convention

    Inputs: last_name : string
            first_name : string

    Outputs: player_url : string
    '''    

    # lower case first and last name
    last_name = last_name.lower()
    first_name = first_name.lower()

    # change first initial to capital
    last_init = last_name[0].upper()
    first_init = first_name[0].upper()

    last_name = f"{last_init}{last_name[1:-1]}"
    first_name = f"{first_init}{first_name[1:-1]}"

    # return url_name based on naming convention
    if len(last_name) >= 4:
        url_name = f'https://www.pro-football-reference.com/players/{last_init}/{last_name[0:4]}{first_name[0:2]}00.htm'
    else:
        url_name = f'https://www.pro-football-reference.com/players/{first_init}/{last_name[0:3]}x{first_name[0:2]}00.htm'
    return url_name

def getNflPlayerStats(url):
    '''
    Description:
    Get a player's stats based off of pro-football-reference.com

    Inputs: url : string
    
    Outputs: [ypg, ypa] : [dict, dict] 
    '''

    #a;lksjdqapweorfulk;vjasdfkj

