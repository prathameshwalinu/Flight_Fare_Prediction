# %%
import pandas as pd

# %%
q1 = pd.read_csv('/Users/himanshutalele/Desktop/DS/Project/RAW_DATA/Origin_and_Destination_Survey_DB1BMarket_2021_1/Origin_and_Destination_Survey_DB1BMarket_2021_1.csv')
#print(q1.head())
print("Number of rows:", len(q1))

# %%
print("Number of rows:", len(q1))

# %%
q2 = pd.read_csv('/Users/himanshutalele/Desktop/DS/Project/RAW_DATA/Origin_and_Destination_Survey_DB1BMarket_2021_2/Origin_and_Destination_Survey_DB1BMarket_2021_2.csv')
#print(q2.head())
print("Number of rows:", len(q2))

# %%
q3 = pd.read_csv('/Users/himanshutalele/Desktop/DS/Project/RAW_DATA/Origin_and_Destination_Survey_DB1BMarket_2021_3/Origin_and_Destination_Survey_DB1BMarket_2021_3.csv')
#print(q3.head())
print("Number of rows:", len(q3))

# %%
q4 = pd.read_csv('/Users/himanshutalele/Desktop/DS/Project/RAW_DATA/Origin_and_Destination_Survey_DB1BMarket_2021_4/Origin_and_Destination_Survey_DB1BMarket_2021_4.csv')
#print(q4.head())
print("Number of rows:", len(q4))

# %%
concatenated_df = pd.concat([q1, q2, q3, q4], axis=0)
#print(concatenated_df.head())
print("Number of columns:", len(concatenated_df.columns))
print("Number of rows:", len(concatenated_df))

# %%
unnecessary_columns = ['Year', 'OriginAirportID',
                       'OriginAirportSeqID', 'OriginCityMarketID', 'OriginCountry',
                       'OriginStateFips', 'OriginState', 'OriginStateName',
                       'DestAirportID', 'DestAirportSeqID', 'DestCityMarketID', 
                       'DestCountry', 'DestStateFips', 'DestState', 'DestStateName', 
                       'AirportGroup', 'WacGroup', 'TkCarrierGroup', 'OpCarrierGroup',
                       'MktDistanceGroup', 'ItinGeoType', 'Unnamed: 41']
correct_Data = concatenated_df.drop(unnecessary_columns, axis=1)

# %%
print("Number of columns:", len(correct_Data.columns))
print(correct_Data.columns)
print("Number of rows:", len(correct_Data))


# %%
correct_Data.to_csv('/Users/himanshutalele/Desktop/DS/Project/RAW_DATA/new_flights_data.csv', index=False)

# %%
flights = pd.read_csv('/Users/himanshutalele/Desktop/DS/Project/RAW_DATA/new_flights_data.csv')

# %%
print("Number of columns:", len(flights.columns))
print(flights.columns)
print("Number of rows:", len(flights))
print(flights.head())

# %%
flights = flights[flights['TkCarrierChange'] == 0]
flights = flights.drop(['TkCarrierChange'], axis=1)


# %%
flights = flights[flights['OpCarrierChange'] == 0]
flights = flights.drop(['OpCarrierChange'], axis=1)

# %%
flights = flights[(flights['RPCarrier'] == flights['TkCarrier']) & (flights['RPCarrier'] == flights['OpCarrier'])]
flights = flights.drop(['RPCarrier', 'OpCarrier'], axis=1)

# %%
flights = flights[flights['MktMilesFlown'] == flights['NonStopMiles']]
flights = flights.drop(['NonStopMiles'], axis=1)

# %%
flights = flights[(flights['MktDistance'] == flights['MktMilesFlown'])]
flights = flights.drop(['MktDistance'], axis=1)

# %%
flights = flights[(flights['MktFare'] >= 50) & (flights['MktFare'] <= 1000)]

# %%
flights = flights[(flights['TkCarrier'] != 'QX') & (flights['TkCarrier'] != 'OO') & (flights['TkCarrier'] != 'EV')]

# %%
flights = flights.drop(['BulkFare'], axis=1)

# %%
flights = flights[flights['Passengers'] <= 20]

# %%
flights

# %%
flights['Miles'] = flights['MktMilesFlown']
flights = flights.drop(['MktMilesFlown'], axis=1)

# %%
flights['ContiguousUSA'] = flights['MktGeoType']
flights = flights.drop(['MktGeoType'], axis=1)

# %%
flights['NumTicketsOrdered'] = flights['Passengers']
flights = flights.drop(['Passengers'], axis=1)

# %%
flights['AirlineCompany'] = flights['TkCarrier']
flights = flights.drop(['TkCarrier'], axis=1)

# %%
flights['PricePerTicket'] = flights['MktFare']
flights = flights.drop(['MktFare'], axis=1)

# %%
flights

# %%
flights = flights.reset_index(drop=True)
flights

# %%
flights.to_csv('/Users/himanshutalele/Desktop/DS/Project/RAW_DATA/flights_data.csv', index=False)

# %%
flights_data = pd.read_csv('/Users/himanshutalele/Desktop/DS/Project/RAW_DATA/flights_data.csv')

# %%
print("Number of columns:", len(flights_data.columns))
print(flights_data.columns)
print("Number of rows:", len(flights_data))
print(flights_data.head())

# %%
flights_data

# %%
flights_data.to_csv('/Users/himanshutalele/Desktop/DS/Project/RAW_DATA/Cleaned_data.csv', index=False)

# %%
Cleaned_data = pd.read_csv('/Users/himanshutalele/Desktop/DS/Project/Data_Cleaning_And_Wrangling/Cleaned_data.csv')

# %%
Cleaned_data


