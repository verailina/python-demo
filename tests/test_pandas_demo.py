"""Testing pandas demo functions."""
import pandas as pd
import numpy as np

from pandas_demo import generate_temperature_data


def test_generate_temperature_data(mocker):
    """Test generation of temperature data."""
    df_mock = mocker.patch("pandas.DataFrame")
    index_mock = mocker.patch("pandas.MultiIndex.from_product")
    rand_mock = mocker.patch("numpy.random.randint")

    dates = [mocker.Mock() for _ in range(3)]
    cities = [mocker.Mock() for _ in range(4)]
    df = generate_temperature_data(dates, cities)
    index_mock.assert_called_once_with([cities, dates], names=["city", "date"])
    rand_mock.assert_called_once_with(-40, 40, index_mock.return_value.shape)
    df_mock.assert_called_once_with(data=rand_mock.return_value,
                                    index=index_mock.return_value,
                                    columns=["temperature"])
    assert df == df_mock.return_value



