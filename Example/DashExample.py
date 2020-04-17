import pandas as pd


# Define the regions and the full name
regions = {'CA': 'Canada', 'GB': 'Great Britain', 'HK': 'Hong Kong',
           'JP': 'Japan', 'KR': 'South Korea', 'US': 'United States',
           'WorldWide': 'World Wide'}

# Read multiple data set
filepath = 'Data/Console_share_'
df = []
for region in regions:
	filepath_curr = filepath + region + '.csv'
	df_temp = pd.read_csv(filepath_curr)
	rows = df_temp.shape[0]
	df_temp['Region'] = [regions[region] for _ in range(rows)]
	df.append(df_temp)

df = pd.concat(df)
df['Other'] = df['Other'].fillna(0)
print(df)
