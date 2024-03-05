class Giurisprudenza:
    descrizione_normalizzata = None
    link = None

    def __init__(self, descrizione_normalizzata, link):
        self.descrizione_normalizzata = descrizione_normalizzata
        self.link = link

    def to_dict(self):
        return {
            "descrizione_normalizzata": self.descrizione_normalizzata if self.descrizione_normalizzata else "",
            "link": self.link if self.link else ""
        } 
