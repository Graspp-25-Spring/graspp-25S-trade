import pandas as pd
import comtradeapicall


CHUNK_SIZE = 12


def get_un_trade_data(subscription_key):
    periods = list(range(1988, 2025))
    chunks = [periods[i:i + CHUNK_SIZE] for i in range(0, len(periods), CHUNK_SIZE)]

    list_df = []
    for chunk in chunks:
        period_string = ",".join([str(year) for year in chunk])
        list_df.append(
            comtradeapicall.getFinalData(
                subscription_key, typeCode='C', freqCode='A', clCode='HS', period=period_string,
                reporterCode=None, cmdCode="TOTAL", flowCode='M,X', partnerCode=0,
                partner2Code=0,
                customsCode="C00", motCode=None, maxRecords=5000, format_output='JSON',
                aggregateBy=None, breakdownMode='classic', countOnly=None, includeDesc=True
            )
        )
    return pd.concat(list_df)