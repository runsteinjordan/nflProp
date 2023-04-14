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

from tools.common.nflPlayer import *


test = nflPlayer('Beckham','Odell')
print(test.url)

test2 = nflPlayer('Rodgers','Aaron')
print(test2.url)