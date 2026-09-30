class Biblioteca:

  def __init__(self):
    self.libri = []

  # Inserimento
  def aggiungi_libro(self, libro):
    if len(self.libri) < 1000:
      self.libri.append(libro)
      print("Libro aggiunto con successo.")
    else:
      print("Capacità massima della biblioteca raggiunta (1000 libri).")

  # Ricerca per titolo
  def cerca_per_titolo(self, titolo):
    risultati = []
    for l in self.libri:
      if titolo.lower() in l.titolo.lower():
        risultati.append(l)
    return risultati

  # Conteggio
  def conteggio_libri(self):
    return len(self.libri)