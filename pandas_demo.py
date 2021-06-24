"""Demonstration of pandas usage."""
from typing import List

import pandas as pd
import numpy as np

cities = ["Andorrala Vella", "Vienna", "Minsk", "Brussels", "Sarajevo",
          "Sofia",  "Zagreb",  "Prague",  "Copenhagen",  "Tallinn",
          "Helsinki",  "Paris",  "Berlin",  "Athens",  "Budapest",
          "Reykjavik",  "Dublin",  "Rome",  "Riga",  "Vaduz",  "Vilnius",
          "Luxembourg",  "Valletta",  "Chisinau",  "Monaco",  "Podgorica",
          "Amsterdam",  "Haag",  "Skopje",  "Oslo",  "Warsaw",  "Lisbon",
          "Bucharest",  "Moscow",  "San Marino",  "Belgrade",  "Bratislava",
          "Ljubljana",  "Madrid",  "Stockholm",  "Bern",  "Kiev",  "London"]
dates = pd.date_range(start="2020-01-01", end="2020-12-31")


def generate_temperature_data(
        dates: pd.DatetimeIndex,
        cities: List[str]) -> pd.DataFrame:
    """Generate dataframe storing a history of temperature data.

    Temperature data is generated randomly for each date and city. It takes
    values in range [-40, 40].

    Args:
        dates (pd.DatetimeIndex): Dates to generate temperature data for.
        cities (List[str]): Cites to generate temperature data for.

    Returns:
        pd.DataFrame: Data frame with `len(dates) x len(cities)` rows
        containing temperature history for given dates for each city.
    """
    index = pd.MultiIndex.from_product([cities, dates], names=["city", "date"])
    data = np.random.randint(-40, 40, index.shape)
    return pd.DataFrame(data=data, index=index, columns=["temperature"])

