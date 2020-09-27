from chekhovs_python.gun import Gun

def test_fire() -> None:
    """ Tests both outcomes of the `fire` method. """

    revolver = Gun(max_ammo=6)
    assert revolver.fire() == "Click."
    revolver.load()
    assert revolver.fire() == "Bang."
    assert revolver.ammo == 5

    return None

def test_load() -> None:
    """ Tests the `load` method. """

    ammo = 6
    revolver = Gun(max_ammo=ammo)
    revolver.load()

    assert revolver.ammo == ammo
    assert revolver.max_ammo == ammo

    return None

def test_unload() -> None:
    """ Tests the `unload` method. """

    ammo = 6
    revolver = Gun(max_ammo=ammo)
    revolver.load()
    revolver.unload()
    assert revolver.ammo == 0

    return None
