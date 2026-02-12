import pyodbc

def get_connection():
    """
    Connects to the DigitalTwinDB database on your local SQL Server instance.
    Make sure SQL Server is running and DigitalTwinDB exists.
    """
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=BXNSXL\\SQLEXPRESS;'   # Your SQL Server instance
            'DATABASE=DigitalTwinDB;'      # Database name
            'Trusted_Connection=yes;'       # Windows Authentication
        )
        print("Connected to SQL Server successfully!")
        return conn
    except Exception as e:
        print("Error connecting to SQL Server:", e)
        raise
