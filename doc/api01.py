import pytest
import requests

def test_geo_ref_ubicacion():
    params = {
    'lat': '-27.2741',
    'lon': '-66.7529'
    }
    response = requests.get('https://apis.datos.gob.ar/georef/api/ubicacion', params=params)
    assert response.status_code == 200
    assert response.json()['ubicacion']['departamento']['nombre'] == 'Belén'
