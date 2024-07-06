
'''names = ["Megan", "Gabe", "Faye"]

names.append("Piggiewig")

names.sort()

print(names)

s = set()

s.add(1)
s.add(2)
s.add(3)
s.add(4)

s.remove(2)

print(s)
print(f"The set has {len(s)} elements.")

for i in range(6):
    print(i)

class Point():
    #magic method
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 8)
'''

class Flight():
    def __init__(self, capacity):
        self.capacity = int (capacity)
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
            
    def open_seats(self):
        return self.capacity - len(self.passengers)
    
flight = Flight(3)

people = ["Megan", "Gabe", "Faye", "Scarameow"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}.")

#Decorators, Lambda, import sys -> except