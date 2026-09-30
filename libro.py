class Libro:

  def __init__(self, titolo, autore, anno, editore, numero_pagine):
    self.titolo = titolo
    self.autore = autore
    self.anno = anno
    self.editore = editore
    self.numero_pagine = numero_pagine

  # Calcola il tempo di lettura stimato (2 minuti per pagina)
  def reading_time(self):
    return self.numero_pagine * 2  # Tempo espresso in minuti

  def __str__(self):
    return f"'{self.titolo}' di {self.autore} ({self.anno}) - Editore: {self.editore}, Pagine: {self.numero_pagine} [Tempo lettura: {self.reading_time()} min]"