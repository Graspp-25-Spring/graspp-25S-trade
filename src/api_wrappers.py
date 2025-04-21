import pandas as pd
import requests
import io
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
EXTERNAL_DATA_DIR = BASE_DIR / "data" / "external"
EXTERNAL_DATA_DIR.parent.mkdir(parents=True, exist_ok=True)


def oecd_api_wrapper(
    agency_id, dataflow_id, dataflow_ver, dimensions, output_filename=None, **kwargs
):
    filter_expression = ".".join(["" if val == "all" else val for val in dimensions])
    option_expression = "&".join(
        ["{}={}".format(param, val) for param, val in kwargs.items()]
    )
    url = "https://sdmx.oecd.org/public/rest/data/{},{},{}/{}?{}".format(
        agency_id, dataflow_id, dataflow_ver, filter_expression, option_expression
    )
    print(f"Fetching OECD data from: {url}")
    response = requests.get(url)
    data = io.StringIO(response.text)
    df = pd.read_csv(data)
    if output_filename:
        print(f"Saving the dataset to: {output_filename}")
        df.to_csv(EXTERNAL_DATA_DIR / output_filename, index=False)
    return df


def ilo_api_wrapper(dataset_id, output_filename=None, **kwargs):
    option_expression = "&".join(
        ["{}={}".format(param, val) for param, val in kwargs.items() if val is not None]
    )
    url = "https://rplumber.ilo.org/data/indicator/?id={}&{}".format(
        dataset_id, option_expression
    )
    print(f"Fetching ILO data from: {url}")
    df = pd.read_csv(url)
    if output_filename:
        print(f"Saving the dataset to: {output_filename}")
        df.to_csv(EXTERNAL_DATA_DIR / output_filename, index=False)
    return df


def get_industry_employment_data(
    start_year, end_year, countries=None, output_filename=None
):
    expression_countries = "+".join(countries) if countries else None
    df = ilo_api_wrapper(
        dataset_id="EMP_TEMP_ECO_OCU_NB_A",
        ref_area=expression_countries,
        timefrom=start_year,
        timeto=end_year,
        classif1="ECO_SECTOR_IND",
        classif2="OCU_SKILL_TOTAL",
        format=".csv",
        output_filename=output_filename,
    )
    return df


if __name__ == "__main__":
    df_oecd = oecd_api_wrapper(
        agency_id="OECD.SDD.TPS",
        dataflow_id="DSD_ALFS%40DF_SUMTAB",
        dataflow_ver="1.0",
        dimensions=["all", "all", "all", "all", "_T", "all", "all", "BTE", "A"],
        startPeriod=1955,
        endPeriod=2023,
        dimensionAtObservation="AllDimensions",
        format="csv",
        output_filename="oecd_data_raw.csv",
    )

    df_ilo = get_industry_employment_data(
        start_year=2020, end_year=2024, output_filename="ilo_data_raw.csv"
    )
