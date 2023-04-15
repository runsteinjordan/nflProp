# Import scraping modules
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Import data manipulation modules
import pandas as pd
import numpy as np
# Import data visualization modules
import matplotlib as mpl
import matplotlib.pyplot as plt
import re

# Import nflProp modules
import sys
tools_path = '../tools/common/'
sys.path.append(tools_path)
from nflPlayer import *

test = nflPlayer('Beckham','Odell')
print(test.url)

test2 = nflPlayer('Rodgers','Aaron')
print(test2.url)