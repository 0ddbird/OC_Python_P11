def test_index_route(client):
    rv = client.get("/")

    assert rv.status_code == 200
    # Check the response too (ex content in HTML -> assert title is in the response)
