import pytest

from grp import create_app
from grp.controllers import AssetQuery

@pytest.fixture(scope='module')
def asset_query():
    assetQuery = AssetQuery('VOO', '2020-02-25')
    return assetQuery

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
    })

    yield app

@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
