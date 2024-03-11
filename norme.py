from cleaners import clean
class Norme:
    descrizione_normalizzata = None
    link = None
    posizione = None
    def __init__(self, descrizione_normalizzata, link, posizione):
        self.descrizione_normalizzata = descrizione_normalizzata
        self.link = link
        self.posizione = posizione

    def to_dict(self):
        return {
            "descrizione_normalizzata": clean(self.descrizione_normalizzata),
            "link": clean(self.link)
        }