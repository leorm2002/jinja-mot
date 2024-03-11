from jinja2 import Environment, FileSystemLoader
import re
from loader import get_db_corsi

environment = Environment(loader=FileSystemLoader("templates/"))
templateCorso = environment.get_template("corso.html")
templateCorso2 = environment.get_template("corsoIndiceRelatore.html")

def genera_corso(corsi):
    filename = "test.html"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(templateCorso.render({"corsi" : corsi}))

def getCognomeNomeRelatore(id_intervento):
    #TM23003_20231006_CatellaniPatrizia esempio input
    cognomeNome = id_intervento.split("_")[-1]
    #todo split
    cognomeNome = " ".join(re.split('(?<=.)(?=[A-Z])', cognomeNome))
    return cognomeNome
def genera_indice_per_relatore(db_corsi):
    indice = {}
    for corso in db_corsi:
        for intervento in corso.interventi:
            id_intervento = intervento.id_intervento
            cognomeNome = getCognomeNomeRelatore(id_intervento)
            if cognomeNome not in indice:
                indice[cognomeNome] = [intervento.to_dict()]
            else:
                indice[cognomeNome].append(id_intervento.to_dict())
    ret = []
    for relatore in indice.keys():
        temp = {"relatore" : relatore, "interventi" : indice[relatore]}
        ret.append(temp)
    ret.sort(key=lambda x: x["relatore"])
    return ret


def genera_corso_indice_interventi(corsi, indice_relatore):
    filename = "corsi2.html"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(templateCorso2.render({"corsi" : corsi, "indice" : indice_relatore}))

def main():
    db_corsi = get_db_corsi()
    corsi = []
    for corso in db_corsi:
        corsi.append(corso.to_dict())
    genera_corso(corsi)
    indice_relatore = genera_indice_per_relatore(db_corsi)
    genera_corso_indice_interventi(corsi, indice_relatore)

if __name__ == '__main__':
    main()