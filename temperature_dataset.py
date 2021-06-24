"""This module contains a class `TemperatureDataset` - randomly generated
temperature data for a given period of time for a list of cities.
"""
from typing import List

import pandas as pd
import numpy as np


class TemperatureDataset:
    """Dataset with randomly generated historical temperature data.

    Temperature data is generated randomly for each date and city. It takes
        values in range [-40, 40].

    Args:
        dates (pd.DatetimeIndex): Dates to generated temperature data for.
        cities (List[str]): Cites to generate temperature data for.

    Attributes:
        data_frame (pd.DataFrame): Data frame with `len(dates) x len(cities)`
            rows containing temperature history for given dates for each city.

    """
    def __init__(self,
                 dates: pd.DatetimeIndex,
                 cities: List[str]):
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
        index = pd.MultiIndex.from_product([cities, dates],
                                           names=["city", "date"])
        data = np.random.randint(-40, 40, index.shape)
        self.data_frame = pd.DataFrame(
            data=data, index=index, columns=["temperature"])
