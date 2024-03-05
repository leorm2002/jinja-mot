from typing import List

from giurisprudenza import Giurisprudenza
from norme import Norme


class Intervento:
    titolo : str = None
    relatore : str = None
    video : str  = None
    keywords = None
    normative : List[Norme] = None
    giurisprudenza : List[Giurisprudenza] = None
    abstract : str = None

    def __init__(self, titolo, relatore, video, keywords, abstract, normative, giurisprudenza):
        self.titolo = titolo
        self.relatore = relatore
        self.video = video
        self.keywords = keywords
        self.abstract = abstract
        self.normative = normative
        self.giurisprudenza = giurisprudenza

    def to_dict(self):
        return {
            "titolo": self.titolo if self.titolo else "",
            "relatore": self.relatore if self.relatore else "",
            "video": self.video if self.video else "",
            "keywords": self.keywords if self.keywords else "",
            "abstract": self.abstract if self.abstract else "",
            "normative": [norma.to_dict() for norma in self.normative],
            "giurisprudenza": [giurisprudenza.to_dict() for giurisprudenza in self.giurisprudenza]
        }