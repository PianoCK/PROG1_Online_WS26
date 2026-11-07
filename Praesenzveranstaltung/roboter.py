class Roboter:
    def __init__(self, eigener_name, start_energy, kampfpower):
        self.name = eigener_name
        self.energy = start_energy
        self.kampfpower = kampfpower

    # Roboter nimmt Schaden entgegen bei Energy
    def nimm_schaden(self, schaden):
        self.energy -= schaden
        if self.energy < 0:
            self.energy = 0
        print(f"{self.name} hat {schaden} Schaden genommen")
        print(f"und hat jetzt {self.energy} Energiepunkte.")
        
    # Roboter fügt anderen Roboter Schaden zu, so dass die Energy um 50 sinkt
    def greift_an(self, gegner):
        gegner.nimm_schaden(self.kampfpower)

    def __repr__(self):
        return f"Roboter {self.name} / Energy: {self.energy}"

    def mache_sound(self):
        print("Beep.")

terminator  = Roboter("Terminator",100, 50)
r2d2        = Roboter("R2D2",60, 20)
terminator.greift_an(r2d2)
