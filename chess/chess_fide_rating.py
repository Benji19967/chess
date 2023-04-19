from typing import Dict

import matplotlib.pyplot as plt
import pandas as pd
from pydantic import BaseModel

from chess.load_data import load_players_df, load_ratings_dfs

class ColumnsRating(BaseModel):
    fide_id: str = "fide_id"
    year: str = "year"
    month: str = "month"
    rating_standard: str = "rating_standard"
    rating_rapid: str = "rating_rapid"
    rating_blitz: str = "rating_blitz"

columns = ColumnsRating()

### Load data
df_players: pd.DataFrame = load_players_df()
ratings_dfs: Dict[int, pd.DataFrame] = load_ratings_dfs()

### ----- Questions

# 1) Find the range for different ratings. Example: IM == [2000, 2200)

# 2) Find the 10 highest rated players in 2016

# 3) Find the 3 "best" countries according to a metric of your choosing.
#    What metric did you use?

# 4) Find the 3 players with the steepest evolution over 1 calendar year
#    and plot their ratings.

# 5) Find the (player, month) with biggest difference in standard vs rapid
#    rating.

# 6) Find the youngest and oldest GMs.

### ----- Question

print(df_players.head())
print(ratings_dfs[2016].head())

# Question 1
# For each player that has a title we need to find his or her highest rating.
num_players = len(df_players)
num_titled_players = len(df_players[pd.notna(df_players["title"])])
fide_ids_titled_players = df_players[pd.notna(df_players["title"])]["fide_id"]
print(fide_ids_titled_players)

# Question 2
df = ratings_dfs[2016]
df

# Get highest rating among all months for each player
idx = (
    df.groupby(["fide_id"])["rating_standard"].transform(max)
    == df["rating_standard"]
)
df_highest_rating_per_player = df[idx]

df.nlargest(n=10, columns="rating_standard")
