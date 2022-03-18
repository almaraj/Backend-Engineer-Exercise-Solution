# How many total number of days does the flights table cover?

def num_of_days():
    flights["date"] = flights['year'].apply(str) + '-' + flights["month"].apply(str) + '-' + flights["day"].apply(str)
    no_of_days = flights.date.nunique()
    return no_of_days

total_days = num_of_days()
print(total_days)

# Total number of days the flights table covers is 365 .