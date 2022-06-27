class Persona:
  def __init__(self, nombre):
    self.nombre = nombre

  def avanza(self):
    print('Estoy caminando')

class Ciclista(Persona):
  def __init__(self, nombre):
    super().__init__(nombre)

  def avanza(self):
    print("Ando moviendome en mi bicicleta")

def run():
  daniel = Persona("Daniel")
  daniel.avanza()

  tommy = Ciclista("Tommy")
  tommy.avanza()

if __name__ == "__main__":
  run()