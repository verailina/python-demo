"""Testing `TemperatureDataset`"""
import pandas as pd
import numpy as np

from temperature_dataset import TemperatureDataset


def test_temperature_dataset__init__(mocker):
    """Test construction of a `TemperatureDataset`."""
    df_mock = mocker.patch("pandas.DataFrame")
    index_mock = mocker.patch("pandas.MultiIndex.from_product")
    rand_mock = mocker.patch("numpy.random.randint")

    dates = [mocker.Mock() for _ in range(3)]
    cities = [mocker.Mock() for _ in range(4)]
    dataset = TemperatureDataset(dates, cities)
    index_mock.assert_called_once_with([cities, dates], names=["city", "date"])
    rand_mock.assert_called_once_with(-40, 40, index_mock.return_value.shape)
    df_mock.assert_called_once_with(data=rand_mock.return_value,
                                    index=index_mock.return_value,
                                    columns=["temperature"])
    assert dataset.data_frame == df_mock.return_value



