import pandas as pd
import comtradeapicall
from pathlib import Path
from tqdm import tqdm


BASE_DIR = Path(__file__).resolve().parent.parent.parent
EXTERNAL_DATA_DIR = BASE_DIR / "data" / "external"
EXTERNAL_DATA_DIR.mkdir(parents=True, exist_ok=True)


CHUNK_SIZE = 12


def get_un_trade_data(subscription_key, output_filename=None):
    periods = list(range(1988, 2025))
    chunks = [periods[i:i + CHUNK_SIZE] for i in range(0, len(periods), CHUNK_SIZE)]

    list_df = []
    for chunk in tqdm(chunks):
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
    df = pd.concat(list_df)
    if output_filename:
        file_path = EXTERNAL_DATA_DIR / output_filename
        print(f"Saving the dataset to: {file_path}")
        df.to_csv(file_path, index=False)
    return df
