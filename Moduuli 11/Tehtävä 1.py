#  Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. Jokaisella
#  julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on
#  päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat. Tee aliluokkiin metodi tulosta_tiedot,
#  joka tudostaa kyseisen julkaisun kaikki tiedot. Luo pääohjelmassa julkaisut Aku Ankka
#  (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
#  Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

class Publishing:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"Name: {self.name}")


class Book(Publishing):

    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        super().print_name()
        print(f"Author: {self.author}, Page count: {self.page_count}")


class Magazine(Publishing):

    def __init__(self, name, editor, page_count):
        self.editor = editor
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        super().print_name()
        print(f"Editor: {self.editor}, Page count: {self.page_count}\n")


publishings = []
publishings.append(Magazine("Aku Ankka", "Aki Hyyppä", 42))
publishings.append(Book("Hytti No: 6", "Rosa Liksom", 200))
for i in publishings:
    i.print_information()
