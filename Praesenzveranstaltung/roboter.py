class Roboter:

    def __init__(self, eigener_name, start_energy):
        self.name = eigener_name
        self.energy = start_energy

    def mache_sound(self):
        print("Beep.")

    # Roboter fügt anderen Roboter Schaden zu, so dass die Energy um 50 sinkt
    def strike_roboter():
        pass

    def __repr__(self):
        return f"Roboter {self.name} / Energy: {self.energy}"

robi = Roboter("Robi",100)
robbi = Roboter("Robbi",60)
robi.mache_sound()
print(robi.energy)
print(robi)
