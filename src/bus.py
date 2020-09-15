class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []

    def drive(self):
        return("Vroom vroom")

    def get_passengers_on_bus(self):
        return len(self.passengers)
        