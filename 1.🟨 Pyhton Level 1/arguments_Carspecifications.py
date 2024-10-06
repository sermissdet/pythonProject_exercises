def car_specifications(make, model, year=2021):
    '''This function prints the specifications of a car.'''
    print("Car Make: {}, Model: {}, Year: {}".format(make, model, year))

# Example usage
# Output: Car Make: Toyota, Model: Camry, Year: 2020
car_specifications("Toyota", "Camry", 2020)

# Output: Car Make: Honda, Model: Civic, Year: 2021
car_specifications("Honda", "Civic")          