# How many departure cities (not airports) does the flights database cover?

def num_of_departure_cities():
    '''This function will return all distinct departure cities that flight DataFrame has'''
    departure_cities = flights.origin.nunique()
    return departure_cities

total_departure_cities = num_of_departure_cities()
print(total_departure_cities)

# Total number departure cities the flights database covers is 3 .