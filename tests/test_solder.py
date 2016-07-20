from Battle.Units import Solder


def test_health():
    solder = Solder()
    assert solder.get_health == 100
