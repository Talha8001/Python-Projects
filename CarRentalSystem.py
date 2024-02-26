class Vehicle:
  def __init__(self, make, model):
    self.make = make
    self.model = model

  def make_model(self):
    print(f"I'm a {self.make} {self.model}.")

  def moves(self):
    print("Moves Going..")
  
mycar = Vehicle('Tesla', 'Model 3')

# print(mycar.make)
# print(mycar.model)

mycar.make_model()
mycar.moves()


your_car = Vehicle('Civi', 'Newf4')
your_car.make_model()
your_car.moves()

class Airplane(Vehicle):
  def moves(self):
    print("File along..")

class Truck(Vehicle):
  def moves(self):
    print("Truck Moving...")

class moter(Vehicle):
  def moves(self):
    print("Bike Moving..")

your_Airplane = Airplane('Private', 'MB29')
your_Truck = Truck('G19', 'Gulish')
your_moter = moter('CD-70', 'Honda')

your_Airplane.make_model()
your_Airplane.moves()

your_Truck.make_model()
your_Truck.moves()

your_moter.make_model()
your_moter.moves()
