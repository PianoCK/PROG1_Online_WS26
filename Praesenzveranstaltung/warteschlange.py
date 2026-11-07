class Warteschlange:
    def __init__(self):
        self.schlange = []

    def ausgabe(self):
        print(self.schlange)

    def ankommen(self, name):
        self.schlange.append(name)

    def verlassen(self):
        if len(self.schlange) > 0:
            name = self.schlange.pop(0)
            print(f"{name} bitte ins Wartezimmer 1.")


w = Warteschlange()
w.ausgabe()
w.ankommen("Alina")
w.ankommen("Bernd")
w.ankommen("Christoph")
w.ausgabe()
w.verlassen()
w.verlassen()
w.verlassen()