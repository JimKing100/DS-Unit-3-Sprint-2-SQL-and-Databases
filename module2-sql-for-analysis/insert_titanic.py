# Imports
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

# Load the data from .csv file and rename the columns
df = pd.read_csv('https://raw.githubusercontent.com/JimKing100/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv')
df = df.rename(columns={"Survived": "survived", "Pclass": "pclass", "Name": "name", "Sex": "sex",
                        "Age": "age", "Siblings/Spouses Aboard": "siblings",
                        "Parents/Children Aboard": "parents", "Fare": "fare"})
print(df.head())

# Initialize the DB connection parameters
host = 'salt.db.elephantsql.com'
user = 'wsatpgnz'
database = 'wsatpgnz'
password = 'XVEGRlubTrvmenIrmXs0323JX60OMe-Q'

# Connect to the Postgres DB
pg_conn = psycopg2.connect(database=database, user=user, password=password, host=host)
pg_cur = pg_conn.cursor()

# Drop the existing titanic table
pg_cur.execute('DROP TABLE "public"."titanic"')
pg_conn.commit()

# Create the SQL for the titanic table creation
create_titanic_table = """
CREATE TABLE titanic(
    survived SMALLINT NOT NULL,
    pclass SMALLINT NOT NULL,
    name VARCHAR (100) NOT NULL,
    sex VARCHAR (10) NOT NULL,
    age SMALLINT NOT NULL,
    siblings SMALLINT NOT NULL,
    parents SMALLINT NOT NULL,
    fare FLOAT NOT NULL
);
"""

# Create the titanic table
pg_cur.execute(create_titanic_table)
pg_conn.commit()

pg_conn.close()

# Connect to the postgres table using sqlalchemy
db_string = "postgres://wsatpgnz:XVEGRlubTrvmenIrmXs0323JX60OMe-Q@salt.db.elephantsql.com:5432/wsatpgnz"
engine = create_engine(db_string)

pg_conn_2 = engine.connect()

# Load the postgres data from the dataframe with no index and appending data
df.to_sql('titanic', pg_conn_2, index=False, if_exists='append')

pg_conn_2.close()
