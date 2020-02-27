"""
This file (asset_test.py) contains the unit tests for the asset_query.py file.
"""
from datetime import datetime
import pytest

def test_parseDate(asset_query):
    testValue = datetime(2020, 2, 15)
    assert asset_query.parseDate('2020-02-15') == testValue

def test_parseDate_invalid(asset_query):
    with pytest.raises(ValueError):
        assert asset_query.parseDate('2020-02')
