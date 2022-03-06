from fastapi import status


def test_convert(client):
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK
