from jinja2 import Environment, FileSystemLoader

from loader import get_db_corsi

environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("intervento.txt")
templateCorso = environment.get_template("corso.html")

def genera_intervento(intervento):
    filename = "test"
    with open(filename, "w", "utf-8") as file:
        file.write(template.render(intervento.to_dict()))
    x = 10
    pass

def genera_corso(corso):
    filename = "test.html"
    with open(filename, "w") as file:
        file.write(templateCorso.render(corso.to_dict()))

def main():
    db_corsi = get_db_corsi()
    genera_corso(db_corsi[3])

if __name__ == '__main__':
    main()