# -*- coding: utf-8 -*-
"""Google Search Analysis

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14EtqPRRNwztkniNjjjUD7LiLs10uCEhT
"""

!pip install pytrends
!pip install --upgrade pytrends

import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
Trending_topics = TrendReq(hl='en-US', tz=360)

kw_list=["Cloud Computing"]
Trending_topics.build_payload(kw_list,cat=0, timeframe='today 12-m')

Trending_topics.build_payload(kw_list=["Cloud Computing"],
                              cat=0, timeframe='today 12-m')
data = Trending_topics.interest_over_time()
data = data.sort_values(by="Cloud Computing", ascending = False)
data = data.head(10)
print(data)

from pytrends.request import TrendReq

# Create a pytrends object
pytrends = TrendReq(hl='en-US', tz=360)

# Define your keyword list
kw_list = ["Cloud Computing"]

# Build the payload for the keyword
pytrends.build_payload(kw_list, cat=0, timeframe='2018-01-01 2018-02-01', geo='', gprop='')

# Get historical interest data
data = pytrends.interest_over_time()

# Sort the data by the "Cloud Computing" column in descending order
data = data.sort_values(by="Cloud Computing", ascending=False)

# Get the top 10 results
data = data.head(10)

# Print the data
print(data)

data = Trending_topics.interest_by_region()
data = data.sort_values(by="Cloud Computing",
                        ascending = False)
data = data.head(10)
print(data)

data.reset_index().plot(x='geoName', y='Cloud Computing',
                        figsize=(10,5), kind="bar")
plt.style.use('fivethirtyeight')
plt.show()

df = Trending_topics.top_charts(2020, hl='en-US',
                                tz=300, geo='GLOBAL')
df.head(10)

Trending_topics.build_payload(kw_list=['Cloud Computing'])
related_queries = Trending_topics.related_queries()
related_queries.values()

keywords = Trending_topics.suggestions(
  keyword='Cloud Computing')
df = pd.DataFrame(keywords)
df.drop(columns= 'mid')