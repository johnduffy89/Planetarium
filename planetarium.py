from planet import planet
class planetarium(object):
    def __init__(self):
        self.planets = []
        Mercury = planet("Mercury", "Gray", "terrestrial")
        Venus = planet("Venus", "Red", "terrestrial")
        Earth = planet("Earth", "Blue", "terrestrial")
        Mars = planet("Mars", "Red", "terrestrial")
        Jupiter = planet("Jupiter", "Orange", "gas giant")
        Saturn = planet("Saturn", "Yellow", "gas giant")
        Neptune = planet("Neptune", "Blue", "gas giant")
        Uranus = planet("Uranus", "Blue", "gas giant")

        self.planets.append(Mercery)
    
            
