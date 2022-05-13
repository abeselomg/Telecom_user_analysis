import psycopg2
import urllib.parse as urlparse
import os
import pandas as pd
import sys
import streamlit as st

dbname = "dbbsa7ga8r2kiv"
user = "osksxcygvoyyll"
password = "11c1a3de0735f724773ef130a106766cfb15d6a2b5cbb5c8898012cae47ec287"
host = "ec2-44-196-223-128.compute-1.amazonaws.com"
port = "5432"


def DBConnect():
    con = psycopg2.connect(
    dbname=dbname, user=user, password=password, host=host, port=port
)
    cur = con.cursor()
    
    return con,cur



def createTables(dbName: str) -> None:
    conn, cur = DBConnect(dbName)
    cur.execute(
    "CREATE TABLE TELEUSER (id SERIAL PRIMARY KEY,user_id VARCHAR ,engagement_score VARCHAR, experience_score VARCHAR, satisfaction_score VARCHAR);"
)
    conn.commit()
    cur.close()


def insert_to_table(dbName: str, df: pd.DataFrame, table_name: str) -> None:

    conn, cur = DBConnect(dbName)
    for _, row in df.iterrows():

        sqlQuery = f"""INSERT INTO {table_name} (user_id, engagement_score, experience_score, satisfaction_score )
             VALUES(%s, %s, %s, %s);"""
        data = (
            row[0],
            row[1],
            row[2],
            row[3]
        )

        try:
            cur.execute(sqlQuery, data)
            conn.commit()
            print("Data Inserted Successfully")
        except Exception as e:
            conn.rollback()
            print("Error: ", e)
    return


def db_execute_fetch(
    *args, many=False, tablename="", rdf=True, **kwargs
) -> pd.DataFrame:
    connection, cursor1 = DBConnect(**kwargs)
    if many:
        cursor1.executemany(*args)
    else:
        cursor1.execute(*args)
    field_names = [i[0] for i in cursor1.description]
    res = cursor1.fetchall()
    nrow = cursor1.rowcount
    if tablename:
        print(f"{nrow} recrods fetched from {tablename} table")
    cursor1.close()
    connection.close()
    if rdf:
        return pd.DataFrame(res, columns=field_names)
    else:
        return res


if __name__ == "__main__":
    createTables(dbName="tweet_db")
    df = pd.read_csv("data/cleaned_economic_data.csv")
    df.info()
    insert_to_table(dbName=dbname, df=df, table_name="TELEUSER")
