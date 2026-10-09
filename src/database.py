import sqlite3
import pandas as pd


def get_connection(database_path):
    """
    Create and return a SQLite database connection.
    """
    connection = sqlite3.connect(database_path)
    return connection


def load_tickets_from_database(database_path):
    """
    Load the tickets table from SQLite into a DataFrame.
    """
    connection = get_connection(database_path)

    query = """
    SELECT *
    FROM tickets
    """

    df = pd.read_sql_query(
        query,
        connection
    )

    connection.close()

    return df


def save_tickets_to_database(df, database_path):
    """
    Save a ticket DataFrame to the SQLite tickets table.
    """
    connection = get_connection(database_path)

    df.to_sql(
        "tickets",
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()