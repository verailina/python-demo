"""Test functionality of `TemperatureDataset` class on a small sample."""
import pandas as pd

from temperature_dataset import TemperatureDataset


cities = ["Andorrala Vella", "Vienna", "Minsk", "Brussels", "Sarajevo",
          "Sofia",  "Zagreb",  "Prague",  "Copenhagen",  "Tallinn",
          "Helsinki",  "Paris",  "Berlin",  "Athens",  "Budapest",
          "Reykjavik",  "Dublin",  "Rome",  "Riga",  "Vaduz",  "Vilnius",
          "Luxembourg",  "Valletta",  "Chisinau",  "Monaco",  "Podgorica",
          "Amsterdam",  "Haag",  "Skopje",  "Oslo",  "Warsaw",  "Lisbon",
          "Bucharest",  "Moscow",  "San Marino",  "Belgrade",  "Bratislava",
          "Ljubljana",  "Madrid",  "Stockholm",  "Bern",  "Kiev",  "London"]
dates = pd.date_range(start="2020-01-01", end="2020-12-31")


def test_temperature_dataset_creation():
    """Test creation of a temperature dataset."""
    # Empty dates and cities
    dataset = TemperatureDataset(dates=pd.DatetimeIndex([]), cities=[])
    assert dataset.data_frame.empty

    # Empty dates
    dataset = TemperatureDataset(dates=pd.DatetimeIndex([]), cities=cities)
    assert dataset.data_frame.empty

    # Empty cities
    dataset = TemperatureDataset(dates=dates, cities=[])
    assert dataset.data_frame.empty

    # Non-empty dataset
    dataset = TemperatureDataset(dates, cities)
    assert len(dataset.data_frame) == len(dates) * len(cities)
    assert dataset.data_frame.index.names == ["city", "date"]
    for city in cities:
        for date in dates:
            temperature = dataset.data_frame.loc[city, date]
            assert len(temperature) == 1
            temperature_value = temperature.max()
            assert -40 <= temperature_value <= 40
