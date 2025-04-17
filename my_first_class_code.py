class Car:
  def __init__(self, make, model, year, color):
    self.make = make
    self.model = model
    self.year = year
    self.color = color

  def start_engine(self):
    print(f"The engine of {self.make} {self.model} is started.")

  def stop_engine(self):
    print(f"The engine of the {self.make} {self.model} is stopped.")

car1 = Car("Toyota", "Camry", 2020, "red")

print(car1.model)         # This will print "Toyota"
car1.start_engine()      # This will print "The engine of Toyota Camry is started."
car1.stop_engine()     
  # This will print "The engine of the Toyota Camry is stopped."