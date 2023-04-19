from typing import Dict

import pandas as pd

DATA_DIR = "~/apps/home/labrecqb/chess/data/kaggle/chess_fide_ratings/archive/"
PLAYERS_FILE = DATA_DIR + "players.csv"
RATINGS_FILE = DATA_DIR + f"ratings_{year}.csv"

### Load the data

# PLAYERS
def load_players_df():
    return pd.read_csv(PLAYERS_FILE)


# RATINGS: 2016 - 2021
def load_ratings_dfs() -> Dict[int, pd.DataFrame]:
    ratings_dfs: Dict[int, pd.DataFrame] = {}
    for year in range(2016, 2022):
        ratings_dfs[year] = pd.read_csv(RATINGS_FILE.format(year=year))
    return ratings_dfs
