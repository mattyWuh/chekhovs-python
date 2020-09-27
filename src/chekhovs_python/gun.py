class Gun:

    def __init__(self, max_ammo: int) -> None:
        """ Create the gun. """

        self.ammo = 0
        self.max_ammo = max_ammo

        return None
    
    def fire(self) -> str:
        """ Fire the gun. """

        noise = "Click."
        if self.ammo > 0:
            noise = "Bang!"
            self.ammo += -1

        print(noise)

        return noise

    def load(self) -> None:
        """ Load the gun. """

        print("Gun loaded.")
        self.ammo += self.max_ammo

        return None

    def unload(self) -> None:
        """ Unloads the gun. """

        for _ in range(self.max_ammo):
            self.fire()

        return None

if __name__ == "__main__":
    """ Satiate Chekhov. """
    
    revolver = Gun(max_ammo=6)
    revolver.load()
    revolver.fire()
    