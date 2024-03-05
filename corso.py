class Corso:
    id_corso = None
    titolo = None
    resp_cd = None
    responsabile_formatore = None
    sunto = None
    interventi = None

    def __init__(self, id_corso, titolo, resp_cd, responsabile_formatore, sunto, interventi):
        self.id_corso = id_corso
        self.titolo = titolo
        self.resp_cd = resp_cd
        self.responsabile_formatore = responsabile_formatore
        self.sunto = sunto
        self.interventi = interventi

    def to_dict(self):
        return {
            "id_corso": self.id_corso if self.id_corso else "",
            "titolo": self.titolo if self.titolo else "",
            "resp_cd": self.resp_cd if self.resp_cd else "",
            "responsabile_formatore": self.responsabile_formatore if self.responsabile_formatore else "",
            "sunto": self.sunto if self.sunto else "",
            "interventi": [intervento.to_dict() for intervento in self.interventi] if self.interventi else []
        }