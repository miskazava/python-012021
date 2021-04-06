class Kontakt:
  def __init__(self, jmeno, email):
    self.jmeno = jmeno
    self.email = email

class Uchazec(Kontakt):
  def __init__(self, datum_pohovoru):
    super().__init__(jmeno, email)
    self.datum_pohovoru = datum_pohovoru
    self.zapis_z_pohovoru = ""

  def uloz_zapis(self, text_zapis):
    if aktualni_datum > datum_pohovoru:
      return "chyba"
    else:
      self.text_zapis = text_zapis
      return "zapis ulozen"
