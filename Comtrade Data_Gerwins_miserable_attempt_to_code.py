import pandas as pd

#Step 1:Importing the data

df_2001_raw = pd.read_csv(r"C:\Users\Gerwin\Documents\Tokyo university\1 Data Science\graspp-25S-trade\data\Comtrade 2001_2012.csv", encoding="latin1", index_col=False)

df_2013_raw = pd.read_csv(r"C:\Users\Gerwin\Documents\Tokyo university\1 Data Science\graspp-25S-trade\data\Comtrade 2012_2024.csv", encoding="latin1", index_col=False)

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