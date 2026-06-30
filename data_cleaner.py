import pandas as pd
import logging


def clean_data(json_data, execution_results):
    """
    Convert Spotify JSON response into a cleaned DataFrame.
    """

    logging.info("Starting data cleaning.")

    artists = json_data["artists"]["items"]
    df = pd.DataFrame(artists)
    df.to_csv("output/raw_data.csv",index=False)

    # Keep only required columns
    required_columns = ["id", "name", "popularity", "genres", "followers"]
    existing_columns = [col for col in required_columns if col in df.columns]

    df = df[existing_columns].copy()

    # Extract follower count from dictionary
    if "followers" in df.columns:
        df["followers"] = df["followers"].apply(
            lambda x: x.get("total", 0) if isinstance(x, dict) else 0
        )
    if "genres" in df.columns:
        df["genres"]=df["genres"].apply(lambda x:",".join(x) if isinstance(x,list)  and len(x) > 0 else "UnKnown")

    if "name" in df.columns:
        df["name"]=df["name"].str.strip()


    df = df.reset_index(drop=True)

    logging.info("Data cleaning completed.")
    execution_results.append(f"Fetched {len(df)} artists from Spotify API.")

    return df


# -------------------------------------------------------------
# VALIDATIONS
# -------------------------------------------------------------

def validate_row_count(df, validation_results):

    row_count = len(df)

    validation_results.append({
        "Test Case ID": "TC_001",
        "Test Case": "Validate Row Count",
        "Expected Result": "Row count should be greater than 0",
        "Actual Result": f"{row_count} rows returned",
        "Status": "PASS" if row_count > 0 else "FAIL"
    })


def validate_required_columns(df, validation_results):

    expected_columns = [
        "id",
        "name",
        "popularity",
        "genres",
        "followers"
    ]

    missing_columns = [
        col for col in expected_columns
        if col not in df.columns
    ]

    validation_results.append({
        "Test Case ID": "TC_002",
        "Test Case": "Validate Required Columns",
        "Expected Result": "All required columns should exist",
        "Actual Result": (
            "All required columns are present"
            if not missing_columns
            else f"Missing columns: {missing_columns}"
        ),
        "Status": "PASS" if not missing_columns else "FAIL"
    })


def validate_nulls(df, validation_results):
    mandatory_columns=["id","name"]
    null_count = df[mandatory_columns].isnull().sum().sum()

    validation_results.append({
        "Test Case ID": "TC_003",
        "Test Case": "Validate Null Values",
        "Expected Result": "Mandatory columns should not contain null values",
        "Actual Result": (
            "No null values found"
            if null_count == 0
            else f"{null_count} null values found"
        ),
        "Status": "PASS" if null_count == 0 else "FAIL"
    })


def validate_duplicates(df, validation_results):

    duplicate_count = df.duplicated(subset=["id"]).sum()

    validation_results.append({
        "Test Case ID": "TC_004",
        "Test Case": "Validate Duplicate Artist IDs",
        "Expected Result": "No duplicate artist IDs should exist",
        "Actual Result": (
            "No duplicate records found"
            if duplicate_count == 0
            else f"{duplicate_count} duplicate records found"
        ),
        "Status": "PASS" if duplicate_count == 0 else "FAIL"
    })


def validate_popularity(df, validation_results):

    invalid_count = (
        (df["popularity"] < 0) |
        (df["popularity"] > 100)
    ).sum()

    validation_results.append({
        "Test Case ID": "TC_005",
        "Test Case": "Validate Popularity Range",
        "Expected Result": "Popularity should be between 0 and 100",
        "Actual Result": (
            "All popularity values are valid"
            if invalid_count == 0
            else f"{invalid_count} invalid popularity values found"
        ),
        "Status": "PASS" if invalid_count == 0 else "FAIL"
    })


def validate_followers(df, validation_results):

    invalid_count = (df["followers"] < 0).sum()

    validation_results.append({
        "Test Case ID": "TC_006",
        "Test Case": "Validate Followers Count",
        "Expected Result": "Followers count should be greater than or equal to 0",
        "Actual Result": (
            "All follower counts are valid"
            if invalid_count == 0
            else f"{invalid_count} invalid follower counts found"
        ),
        "Status": "PASS" if invalid_count == 0 else "FAIL"
    })


def validate_artist_name(df, validation_results):

    invalid_count = (
        df["name"].astype(str).str.strip() == ""
    ).sum()

    validation_results.append({
        "Test Case ID": "TC_007",
        "Test Case": "Validate Artist Name",
        "Expected Result": "Artist name should not be blank",
        "Actual Result": (
            "All artist names are valid"
            if invalid_count == 0
            else f"{invalid_count} blank artist names found"
        ),
        "Status": "PASS" if invalid_count == 0 else "FAIL"
    })