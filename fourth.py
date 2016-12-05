# Create a Rocket class.
# It should take 3 parameters in its constructor
# 1st parameter: the type of the rocket as a string, "falcon1" or "falcon9".
# 2nd parameter: the starting fuel level as a number, defaults to 0.
# 3rd parameter: number of launches as a number, defaults to 0.
#
# It should have 3 methods:
#
# launch()
# it should use 1 fuel if it's a falcon1 and 9 fuels if it's a falcon9.
# it should increment the launches by one if it had enough fuel for the launch.
#
# refill()
# it should refill the rocket's fuel level to 5 if falcon1 and to 20 if falcon9.
# it should return the amount of fuel used for the refill.
# example: if the rocket is a falcon1 and has fuel level 3, then it should return 2.
#
# getStats()
# it should return its stats as a string like: "name: falcon9, fuel: 11, launches: 1"

################################################

# The following code should work with the class:
class Rocket:
    def __init__(self, rocket_name, fuel = 0, launch_number = 0):
        self.rocket_name = rocket_name
        self.fuel = fuel
        self.launch_number = launch_number

    def launch(self):
        if self.rocket_name == 'falcon1':
            self.launch_number += 1
            self.fuel -= 1
        elif self.rocket_name =='falcon9':
            self.launch_number += 1
            self.fuel -= 9

    def refill(self):
        add_fuel = 0
        if self.rocket_name == 'falcon1':
            while self.fuel < 5:
                self.fuel += 1
                add_fuel += 1
        elif self.rocket_name =='falcon9':
            while self.fuel < 20:
                self.fuel += 1
                add_fuel += 1
        return add_fuel

    def getStats(self):
        return('name: ' + str(self.rocket_name) + ' fuel: ' + str(self.fuel) + ' launches: ' + str(self.launch_number))

falcon1 = Rocket('falcon1')
returned_falcon9 = Rocket('falcon9', 11, 1)

falcon1.refill() # 5
falcon1.launch()

print(falcon1.getStats()) # name: falcon1, fuel: 4, launches: 1
print(returned_falcon9.getStats()) # name: falcon9, fuel: 11, launches: 1
