# Imports
import pandas as pd
import sqlite3

# Load the data in df and convert to sqlite3
df = pd.read_csv('buddymove_holidayiq.csv')
df = df.rename(columns={'User Id': 'User_Id'})
print(df.shape)
print(df.head())

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
df.to_sql('review', con=conn)

# Queries
query1 = 'SELECT COUNT() \
          FROM  review;'

query2 = 'SELECT COUNT(User_Id) \
          FROM review \
          WHERE Nature > 99 AND Shopping > 99;'

query3 = 'SELECT AVG(Sports), AVG(Religious), AVG(Nature), \
                 AVG(Theatre), AVG(Shopping), AVG(Picnic) \
          FROM review'

# Execute queries
curs1 = conn.cursor()
print('Total rows =',
      curs1.execute(query1).fetchall())

curs2 = conn.cursor()
print('Total reviewed 100+ Nature and 100+ Shopping =',
      curs2.execute(query2).fetchall())

curs3 = conn.cursor()
print('Average review in each category =',
      curs3.execute(query3).fetchall())

# Close cursors and commit
curs1.close()
curs2.close()
curs3.close()
conn.commit()
