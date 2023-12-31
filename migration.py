import psycopg2
import numpy as np
import psycopg2.extras as extras
import pandas as pd


def execute_values(conn, df, table):
    tuples = [tuple(x) for x in df.to_numpy()]

    # cols = ', '.join(list(df.columns))
    cols = ', '.join(list(df.columns))

    # SQL query to execute
    query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
    cursor = conn.cursor()
    try:
        extras.execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("****** the dataframe is inserted *******")
    cursor.close()


conn = psycopg2.connect(
    database="dbezl1uquldojv", user='uhgpgzxv2hhak', password='700Flower!', host='abogadoericprice.com', port='5432'
)

# Data migration - Account table
# df = pd.read_csv('Account.csv', encoding='utf-8')
# execute_values(conn, df, 'accounts')
# df = pd.read_csv('Account.csv', encoding='latin-1')

# Data migration for Case table
# df = pd.read_csv('Case.csv', encoding='latin-1')
# execute_values(conn, df, 'cases')

# Data migration - Month report
df = pd.read_csv('month_stat.csv', encoding='utf-8')
execute_values(conn, df, 'month_stat')
