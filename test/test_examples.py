import pypsa


def test_ac_dc_meshed():
    """
    Plain testing if retrievement works.
    """
    n = pypsa.examples.ac_dc_meshed()
    assert not n.buses.empty


def test_storage_hvdc():
    """
    Plain testing if retrievement works.
    """
    n = pypsa.examples.storage_hvdc()
    assert not n.buses.empty


def test_scigrid_de():
    """
    Plain testing if retrievement works.
    """
    n = pypsa.examples.scigrid_de()
    assert not n.buses.empty
