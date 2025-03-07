"""Test the /config blueprint route."""

import json
import dserver_search_plugin_mongo

from .utils import compare_nested


def test_config_info_route(tmp_app_with_users, snowwhite_token):  # NOQA

    headers = dict(Authorization="Bearer " + snowwhite_token)
    r = tmp_app_with_users.get(
        "/config/info",
        headers=headers,
    )
    assert r.status_code == 200

    expected_content = {
          'search_mongo_collection': 'datasets',
          'search_mongo_uri': 'mongodb://localhost:27017/',
    }

    response = json.loads(r.data.decode("utf-8"))

    assert compare_nested(expected_content, response)


def test_config_version_route(tmp_app_with_users):  # NOQA

    r = tmp_app_with_users.get(
        "/config/versions",
    )
    assert r.status_code == 200

    expected_content = {
          'dserver_search_plugin_mongo': dserver_search_plugin_mongo.__version__,
    }

    response = json.loads(r.data.decode("utf-8"))

    assert compare_nested(expected_content, response)
