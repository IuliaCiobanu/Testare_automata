class Masina:
    model=None
    culoare="orange"
    marca=None
    vitexa_max=0
    an_fabricatie=0
    capacitate_motor=0
    serie_sasiu=None
    tip_combustibil="motorina"
    cutie_viteza="automata"
    viteza_curenta=0

    # constructor
    def __init__(self,marca,model,culoare):
        self.marca=marca
        self.model=model
        if culoare=="orange":
            self.culoare="portocaliu"

    # metodele
    def paint(self,colour):
        self.culoare=colour

    def start_masina(self):
        self.viteza_curenta=self.viteza_curenta+5