class Norme:
    descrizione_normalizzata = None
    link = None

    def __init__(self, descrizione_normalizzata, link):
        self.descrizione_normalizzata = descrizione_normalizzata
        self.link = link

    def to_dict(self):
        return {
            "descrizione_normalizzata": self.descrizione_normalizzata,
            "link": self.link
        }