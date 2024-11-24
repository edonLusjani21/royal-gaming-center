import pyodbc
conn = pyodbc.connect(
    "DRIVER={SQL Server};SERVER=EDONLUSJANI\\SQLEXPRESS;DATABASE=TicSys;UID=edon.lusjani;PWD=Ed23082003$"
)
print("Connection successful!")
