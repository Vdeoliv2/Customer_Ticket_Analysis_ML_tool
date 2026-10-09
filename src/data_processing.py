import pandas as pd


def load_data(file_path):
    """
    Load a CSV file and return it as a Pandas DataFrame.
    """
    df = pd.read_csv(file_path)
    return df


def validate_data(df):
    """
    Validate the fields required by the application.

    Returns a dictionary containing validation results.
    """

    duplicate_count = df.duplicated().sum()

    invalid_ticket_types = (
        df["Ticket Type"]
        .fillna("")
        .str.strip()
        .eq("")
        .sum()
    )

    invalid_descriptions = (
        df["Ticket Description"]
        .fillna("")
        .str.strip()
        .eq("")
        .sum()
    )

    validation_results = {
        "duplicate_count": duplicate_count,
        "invalid_ticket_types": invalid_ticket_types,
        "invalid_descriptions": invalid_descriptions,
        "is_valid": (
            duplicate_count == 0
            and invalid_ticket_types == 0
            and invalid_descriptions == 0
        )
    }

    return validation_results