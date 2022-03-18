# Which are the two most connected cities?
import pandas as pd

def most_connected_city():
    df = pd.DataFrame(flights.dest.value_counts())
    two_most_connected_cities = df.nlargest(2,"dest").index.tolist()
    return two_most_connected_cities

two_most_connected_cities = most_connected_city()
print(two_most_connected_cities)

# the two most connected cities are : ['ORD', 'ATL'] .