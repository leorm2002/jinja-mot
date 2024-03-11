from typing import List

from giurisprudenza import Giurisprudenza
from norme import Norme
from cleaners import clean


class Intervento:
    titolo : str = None
    relatore : str = None
    video : str  = None
    keywords = None
    normative : List[Norme] = None
    giurisprudenza : List[Giurisprudenza] = None
    abstract : str = None
    id_intervento = None

    def __init__(self, titolo, relatore, video, keywords, abstract, normative, giurisprudenza, id_intervento):
        self.titolo = titolo
        self.relatore = relatore
        self.video = video
        self.keywords = keywords
        self.abstract = abstract
        self.normative = normative
        self.giurisprudenza = giurisprudenza
        self.id_intervento = id_intervento

    def to_dict(self):
        return {
            "titolo": self.titolo if self.titolo else "",
            "relatore": self.relatore if self.relatore else "",
            "video": clean(self.video),
            "keywords": self.keywords if self.keywords else "",
            "abstract": self.abstract if self.abstract else "",
            "normative": [norma.to_dict() for norma in self.normative],
            "giurisprudenza": [giurisprudenza.to_dict() for giurisprudenza in self.giurisprudenza],
            "id_intervento": self.id_intervento if self.id_intervento else ""
        }