# Test verifying that the movable feasts route is working and returning the correct data
def test_get_movable_feasts(client):
    res = client.get("/movable-feasts/2026")
    assert res.status_code == 200
    data = res.json()
    assert len(data) == 22
    assert data["easter_sunday"] == "2026-04-05"


# Test verifying that the fixed feasts route is working and returning the correct data
def test_get_fixed_feasts(client):
    res = client.get("/fixed-feasts/2026")
    assert res.status_code == 200
    data = res.json()
    assert len(data) == 24
    assert data["epiphany"] == "2026-01-06"