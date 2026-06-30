import pandas as pd
import logging
import os
import sys
from spotify_auth import fetch_data_api
from spotify_api import search_artist
from data_cleaner import clean_data,validate_row_count,validate_duplicates,validate_nulls,\
    validate_required_columns,validate_popularity,validate_followers,validate_artist_name


def main(artist_name=None):
    execution_results=[]
    validation_results=[]
    if len(sys.argv) < 2:
        print('Usage: python main.py "artist name"')
        sys.exit(1)

    artist_name = " ".join(sys.argv[1:])
    token=fetch_data_api(execution_results)

    json_data=search_artist(token,execution_results,artist_name,limit=50,offset=100)
    df=clean_data(json_data,execution_results)
    validate_row_count(df, validation_results)
    validate_required_columns(df,validation_results)
    validate_nulls(df,validation_results)
    validate_duplicates(df,validation_results)
    validate_popularity(df,validation_results)
    validate_artist_name(df,validation_results)
    validate_followers(df,validation_results)
    os.makedirs("output",exist_ok=True)
    df.to_csv("output/spotify_artists.csv",index=False)
    logging.info("Artists cleaned and stored in csv file")
    report=pd.DataFrame(validation_results)
    report.to_csv("output/validation_reports.csv")
    logging.info("Validation results stored in csv file")

if __name__== "__main__":
    main()
