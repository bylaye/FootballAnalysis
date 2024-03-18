"""
Download Season data Top European League.
"""

import os
from datetime import date, datetime
import sys
import requests

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
        print(f'Warning: Limit season league = {LIMIT_SEASON}')
    for i in range(number_season):
        year_before = year-1
        season = str(year_before)[2:] + str(year)[2:]
        seasons.append(season)
        year -= 1
    return seasons


def path_directory(parent=os.getcwd(), name='SeasonDatasets'):
    path_dataset = os.path.join(parent, name)
    if not os.path.isdir(path_dataset):
        os.makedirs(path_dataset)
    return path_dataset


def download_datasets(league, season):
    """Download match results by season grouped by league"""

    url = "https://www.football-data.co.uk/mmz4281"
    path_dataset = path_directory()
    full_url = os.path.join(url, season, league)
    try:
        response = requests.get(full_url)
        response.raise_for_status()
        file_name = season+'.csv'
        league_path = path_directory(path_dataset, league)
        file_data = os.path.join(league_path, file_name)
        with open(file_data, 'wb') as file:
            file.write(response.content)
    except requests.exceptions.RequestException as e:
        print(e)
    except IOError as e:
        print(e)
    except Exception as e:
        print(e)
