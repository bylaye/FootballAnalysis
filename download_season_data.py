"""
Download Season data Top European League.
"""

import os
from datetime import date

"""List Top League"""
leagues = {
    'E0': 'England',
    'I1': 'Italy',
    'D1': 'Germany',
    'SP1': 'Spain',
    'F1': 'France',
    'P1': 'Portugal',
    'N1': 'Netherlands',
    'B1': 'Belgium'
}


def season_list(number_season=1):
    """
    Generate season league in format:
    example season 2005-2006 = "0506", 2010-2011 = "1011"
    >>> year = 2024
    >>> season_list(3)
    ['2324', '2223', '2122']
    >>> 
    """
    seasons = []
    LIMIT_SEASON = 2006
    year = date.today().year
    # limit the max old season to 2005-2006
    if (year - number_season) < LIMIT_SEASON:
        number_season = year - LIMIT_SEASON
    for i in range(number_season):
        year_before = year-1
        season = str(year_before)[2:] + str(year)[2:]
        seasons.append(season)
        year -= 1
    return seasons
