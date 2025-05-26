import pandas as pd
from pathlib import Path
from tqdm import tqdm
import comtradeapicall


BASE_DIR = Path(__file__).resolve().parent.parent.parent

EXTERNAL_DATA_DIR = BASE_DIR / "data" / "external"
EXTERNAL_DATA_DIR.mkdir(parents=True, exist_ok=True)
INTERIM_DATA_DIR = BASE_DIR / "data" / "interim"
INTERIM_DATA_DIR.mkdir(parents=True, exist_ok=True)

EMPLOYMENT_BASE_NAME = "employment"
TRADE_BASE_NAME = "trade"


CHUNK_SIZE = 12  # The UN Comtrade API limits the number of years we can download to 12


def ilo_api_wrapper(dataset_id, file_path=None, **kwargs):
    option_expression = "&".join(
        ["{}={}".format(param, val) for param, val in kwargs.items() if val is not None]
    )
    url = "https://rplumber.ilo.org/data/indicator/?id={}&{}".format(
        dataset_id, option_expression
    )
    print(f"Fetching ILO data from: {url}")
    df = pd.read_csv(url)
    if file_path:
        print(f"Saving the dataset to: {file_path}")
        df.to_csv(file_path, index=False)
    return df


def get_industry_employment_data(start_year, end_year, countries=None, file_path=None):
    expression_countries = "+".join(countries) if countries else None
    df = ilo_api_wrapper(
        dataset_id="EMP_TEMP_ECO_OCU_NB_A",
        ref_area=expression_countries,
        timefrom=start_year,
        timeto=end_year,
        classif1="ECO_SECTOR_IND",
        classif2="OCU_SKILL_TOTAL",
        format=".csv",
        file_path=file_path,
    )
    return df


def clean_industry_employment_data(df_raw, file_path=None):
    df_extract = df_raw.loc[:, ["ref_area", "time", "obs_value"]]
    def_renamed = df_extract.rename(
        {"ref_area": "country", "time": "year", "obs_value": "ILO"}, axis="columns"
    )
    df_clean = def_renamed.set_index(["country", "year"])
    if file_path:
        print(f"Saving the dataset to: {file_path}")
        df_clean.to_csv(file_path, index=True)
    return df_clean


def get_un_trade_data(subscription_key, file_path=None):
    periods = list(range(1988, 2025))
    chunks = [periods[i : i + CHUNK_SIZE] for i in range(0, len(periods), CHUNK_SIZE)]

    list_df = []
    for chunk in tqdm(chunks):
        period_string = ",".join([str(year) for year in chunk])
        list_df.append(
            comtradeapicall.getFinalData(
                subscription_key,
                typeCode="C",
                freqCode="A",
                clCode="HS",
                period=period_string,
                reporterCode=None,
                cmdCode="TOTAL",
                flowCode="M,X",
                partnerCode=0,
                partner2Code=0,
                customsCode="C00",
                motCode=None,
                maxRecords=5000,
                format_output="JSON",
                aggregateBy=None,
                breakdownMode="classic",
                countOnly=None,
                includeDesc=True,
            )
        )
    df = pd.concat(list_df)
    if file_path:
        print(f"Saving the dataset to: {file_path}")
        df.to_csv(file_path, index=False)
    return df


def clean_trade_data(df_raw, file_path=None):
    df_extract = df_raw[["reporterISO", "refYear", "primaryValue", "flowDesc"]].dropna()
    df_rename = df_extract.rename(
        {
            "reporterISO": "country",
            "refYear": "year",
            "primaryValue": "total trade value",
            "flowDesc": "import or export",
        },
        axis=1,
    )
    df_clean = df_rename.pivot(
        index=["country", "year"],
        columns="import or export",
        values="total trade value",
    )
    if file_path:
        print(f"Saving the dataset to: {file_path}")
        df_clean.to_csv(file_path, index=True)
    return df_clean


def merge_data(df_1, df_2, file_path=None):
    df_merge = pd.merge(df_1, df_2, right_index=True, left_index=True, how="inner")
    if file_path:
        print(f"Saving the dataset to: {file_path}")
        df_merge.to_csv(file_path, index=True)
    return df_merge


class DataImporter:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.employment_raw = None
        self.trade_raw = None
        self.employment_clean = None
        self.trade_clean = None
        self.merge = None

    def get_employment_data(self):
        file_path_raw = EXTERNAL_DATA_DIR / (EMPLOYMENT_BASE_NAME + "_raw.csv")
        if file_path_raw.exists():
            print(f"Reading raw data from: {file_path_raw}")
            self.employment_raw = pd.read_csv(file_path_raw)
        else:
            self.employment_raw = get_industry_employment_data(
                start_year=2000, end_year=2024, file_path=file_path_raw
            )

        file_path_clean = INTERIM_DATA_DIR / (EMPLOYMENT_BASE_NAME + "_clean.csv")
        if file_path_clean.exists():
            print(f"Reading clean data from: {file_path_clean}")
            df = pd.read_csv(file_path_clean)
            self.employment_clean = df.set_index(["country", "year"])
        else:
            self.employment_clean = clean_industry_employment_data(
                self.employment_raw, file_path=file_path_clean
            )

        return self.employment_clean

    def get_trade_data(self):
        file_path_raw = EXTERNAL_DATA_DIR / (TRADE_BASE_NAME + "_raw.csv")
        if file_path_raw.exists():
            print(f"Reading raw data from: {file_path_raw}")
            self.trade_raw = pd.read_csv(file_path_raw)
        else:
            self.trade_raw = get_un_trade_data(
                subscription_key=self.api_key, file_path=file_path_raw
            )

        file_path_clean = INTERIM_DATA_DIR / (TRADE_BASE_NAME + "_clean.csv")
        if file_path_clean.exists():
            print(f"Reading clean data from: {file_path_clean}")
            df = pd.read_csv(file_path_clean)
            self.trade_clean = df.set_index(["country", "year"])
        else:
            self.trade_clean = clean_trade_data(
                self.trade_raw, file_path=file_path_clean
            )

        return self.trade_clean

    def get_merged_data(self):
        file_path_merge = INTERIM_DATA_DIR / "merge.csv"
        if file_path_merge.exists():
            print(f"Reading merged data from: {file_path_merge}")
            df = pd.read_csv(file_path_merge)
            self.merge = df.set_index(["country", "year"])
        else:
            df_trade = self.get_trade_data()
            df_employment = self.get_employment_data()
            self.merge = merge_data(df_trade, df_employment, file_path=file_path_merge)
        return self.merge
