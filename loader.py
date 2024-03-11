from corso import Corso
from excel_supplier import *
from giurisprudenza import Giurisprudenza
from intervento import Intervento
from norme import Norme


def load_corsi(corsi, db_interventi):
    #prende in inpute list di liste di interventi
    corsiOut = []
    for intervento in corsi:
        id_corso = intervento[0]
        data_inizio = intervento[1]
        data_fine = intervento[2]
        modalita = intervento[3]
        titolo = intervento[4]
        settore = intervento[5]
        resp_cd = intervento[6]
        responsabile_formatore = intervento[7]
        note = intervento[8]
        sunto = intervento[9]
        interventi = db_interventi[id_corso] if id_corso in db_interventi else []
        corsiOut.append(Corso(id_corso, titolo, resp_cd, responsabile_formatore, sunto, interventi))
    return corsiOut

def sorta(norme):
    return norme.posizione

def load_interventi(interventi, db_norme, db_giurisprudenza):
    #ritorna una lista di interventi
    db_interventi = {}
    for intervento in interventi:
        data = intervento[0]
        id_corso = intervento[1]
        id_intervento = intervento[2]
        titolo = intervento[3]
        relatore = intervento[4]
        qualifica = intervento[5]
        note = intervento[6]
        video = intervento[7]
        audio = intervento[8]
        img = intervento[9]
        trascrizione = intervento[10]
        abstract = intervento[15]
        key1 = intervento[16]
        key2 = intervento[17]
        key3 = intervento[18]
        key4 = intervento[19]
        key5 = intervento[20]
        keywords = [key1, key2, key3, key4, key5]
        normative = db_norme[id_intervento] if id_intervento in db_norme else []
        giurisprudenza = db_giurisprudenza[id_intervento] if id_intervento in db_giurisprudenza else []
        #sorto
        normative.sort(key=lambda x: x.posizione, reverse=False)
        giurisprudenza.sort(key=lambda x: x.posizione, reverse=False)
        intervento = Intervento(titolo, relatore, video, keywords,abstract, normative, giurisprudenza, id_intervento)
        if id_corso in db_interventi:
            db_interventi[id_corso].append(intervento)
        else:
            db_interventi[id_corso] = [intervento]
    return db_interventi

def load_norme(norme):
    #ritorna un dizionario key = id_intervento, value = lista di norme
    db_norme = {}
    for norma in norme:
        id_intervento = norma[1]
        descrizione_normalizzata = norma[4]
        link = norma[6]
        posizione = norma[2]
        if id_intervento in db_norme:
            db_norme[id_intervento].append(Norme(descrizione_normalizzata, link, posizione))
        else:
            db_norme[id_intervento] = [Norme(descrizione_normalizzata, link, posizione)]
    return db_norme

def load_giurisprudenza(giurisprudenza):
    #ritorna un dizionario key = id_intervento, value = lista di giurisprudenza
    db_giurisprudenza = {}
    for giurisprudenza in giurisprudenza:
        id_intervento = giurisprudenza[1]
        descrizione_normalizzata = giurisprudenza[4]
        link = giurisprudenza[6]
        posizione = giurisprudenza[2]

        if id_intervento in db_giurisprudenza:
            db_giurisprudenza[id_intervento].append(Giurisprudenza(descrizione_normalizzata, link, posizione))
        else:
            db_giurisprudenza[id_intervento] = [Giurisprudenza(descrizione_normalizzata, link, posizione)]
    return db_giurisprudenza

def get_db_corsi():
    giurisprudenza = load_giurisprudenza(get_giurisprudenza())
    norme = load_norme(get_normative())
    interventi = load_interventi(get_interventi(), norme, giurisprudenza)
    corsi = load_corsi(get_corsi(), interventi)
    return corsi
    
def main():
    print("Classe da usare a libreria")


if __name__ == '__main__':
    main()