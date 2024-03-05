import pandas as pd

FILE = "MOT_lavorazioni.xlsx"
CORSI = "Corsi"
INTERVENTI = "Interventi"
GIURISPRUDENZA = "Giurisprudenza"
NORMATIVE = "Norme"
def get_corsi():
    xl = pd.ExcelFile(FILE)
    first_sheet_df = xl.parse(CORSI)
    return first_sheet_df.values.tolist()

def get_interventi():
    xl = pd.ExcelFile(FILE)
    first_sheet_df = xl.parse(INTERVENTI)
    return first_sheet_df.values.tolist()

def get_giurisprudenza():
    xl = pd.ExcelFile(FILE)
    first_sheet_df = xl.parse(GIURISPRUDENZA)
    return first_sheet_df.values.tolist()

def get_normative():
    xl = pd.ExcelFile(FILE)
    first_sheet_df = xl.parse(NORMATIVE)
    return first_sheet_df.values.tolist()


def main():
    print("Classe da usare a libreria")

if __name__ == '__main__':
    main()