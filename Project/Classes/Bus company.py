class Buses:
    def __init__(self, number, route, driver):
        self.number = number
        self.route = route
        self.driver = driver
        bus_list.append(self)

# Main routine
bus_list = []

bus1 = Buses("2010", "Y", "Greg")
bus2 = Buses("2011", "P", "Joel")
bus3 = Buses("2012", "130", "Kent")

for bus in bus_list:
    print(f"Bus number: {bus.number}\n"
          f"Route: {bus.route}\n"
          f"Driver: {bus.driver}")