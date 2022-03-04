import json
import server
from tests.conftest import client


def test_purchase_more_places_than_points(client, mocker):
    mocker.patch.object(
        server,
        'clubs',
        [{
            "name":"Club Test",
            "email":"secretary@clubtest.com",
            "points":"8"
            }]
        )
    mocker.patch.object(
        server,
        'competitions',
        [{
            "name":"Competition Test",
            "date":"2020-03-27 10:00:00",
            "numberOfPlaces":"12"
            }]
        )
    response = client.post(
        '/purchasePlaces',
        data={
            'competition': 'Competition Test',
            'club': 'Club Test',
            'places': '9'
            }
        )
    assert response.status_code == 200
    assert b'Sorry, you required more places than possible - Try again' in response.data


def test_purchase_more_than_12_places(client, mocker):
    mocker.patch.object(
        server,
        'clubs',
        [{
            "name":"Club Test",
            "email":"secretary@clubtest.com",
            "points":"15"
            }]
        )
    mocker.patch.object(
        server,
        'competitions',
        [{
            "name":"Competition Test",
            "date":"2020-03-27 10:00:00",
            "numberOfPlaces":"14"
            }]
        )
    response = client.post(
        '/purchasePlaces',
        data={
            'competition': 'Competition Test',
            'club': 'Club Test',
            'places': '13'
            }
        )
    assert response.status_code == 200
    assert b'Sorry, you only can book 12 places maximum - Try again' in response.data