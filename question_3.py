# Which airplane manufacturer incurred the most delays in the analysis period?
import pandas as pd

def most_delay():
    flights["total_delay"] = flights['dep_delay'] + flights["arr_delay"]
    new_df = pd.merge(flights,planes,on='tailnum')
    mean_delay_df = new_df.groupby(['manufacturer'])['total_delay'].mean()
    return mean_delay_df.idxmax()

most_delay_mfr = most_delay()
print(most_delay_mfr)

# manufacturer incurred the most delays is AGUSTA SPA .