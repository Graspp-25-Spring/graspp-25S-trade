import pandas as pd

#Step 1:Importing the data

df_2001_raw = pd.read_csv("data/Comtrade 2001_2012.csv", encoding="latin1", index_col=False)

df_2013_raw = pd.read_csv("data/Comtrade 2012_2024.csv", encoding="latin1", index_col=False)

# #print check if you want to prove that import works
# #print(df_2001_raw.head(2))
# #print(df_2013_raw.head(2))


# #Step 2: filter rows
df_2001 = df_2001_raw[['reporterDesc', 'refYear', 'primaryValue']].dropna()
df_2013 = df_2013_raw[['reporterDesc', 'refYear', 'primaryValue']].dropna()


# #Step 3: rename rows
df_2001 = df_2001.rename({"reporterDesc":'country', "refYear":'date', "primaryValue":'total trade value'}, axis=1)
df_2013 = df_2013.rename({"reporterDesc":'country', "refYear":'date', "primaryValue":'total trade value'}, axis=1)

# print(df_2001.tail(2))
# print(df_2013.tail(2))

#Step 4: merge data sets
df_merge = pd.merge(
    df_2001,
    df_2013,
    right_index = True,
    left_index = True,
    how = 'inner'
    )

print(df_merge.tail(2))



#Gerwins miserable attempt to write a funciton 
# import pandas as pd
# def load_and_clean_trade_data(filepath):
#     # Step 1: Load the data
#     df_raw = pd.read_csv(filepath, encoding="latin1", index_col=False)
    
#     # Step 2: Filter necessary columns
#     df_filtered = df_raw[['reporterDesc', 'refYear', 'primaryValue']].dropna()
    
#     # Step 3: Rename columns
#     df_cleaned = df_filtered.rename({
#         'reporterDesc': 'country',
#         'refYear': 'date',
#         'primaryValue': 'total trade value'
#     }, axis=1)
    
#     # Step 4: Add Filepaths
#     #I need help here
#     file_2001 = "data/Comtrade 2001_2012.csv"
#     file_2013 = "data/Comtrade 2012_2024.csv"
#     df_2001 = load_and_clean_trade_data(file_2001)
#     df_2013 = load_and_clean_trade_data(file_2013)

#     return df_cleaned

# print(load_and_clean_trade_data(filepath))
