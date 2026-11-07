class Roboter:

    def __init__(self, eigener_name, start_energy):
        self.name = eigener_name
        self.energy = start_energy

    def mache_sound(self):
        print("Beep.")

    # Roboter nimmt Schaden entgegen bei Energy
    def nimm_schaden():
        pass

    # Roboter fügt anderen Roboter Schaden zu, so dass die Energy um 50 sinkt
    def strike_roboter():
        pass

    def __repr__(self):
        return f"Roboter {self.name} / Energy: {self.energy}"

terminator = Roboter("Terminator",100)
r2d2 = Roboter("R2D2",60)
r2d2.mache_sound()
print(r2d2.energy)
print(r2d2)
