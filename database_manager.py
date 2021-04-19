import psycopg2

def insert_password(user_name, password, user_email, app_name, url):
    try:
        conn = connect()
        cur = conn.cursor()
        postgres_query_to_insert = """ INSERT INTO passwords(user_name, password, user_email, app_name, url) VALUES (%s, %s, %s, %s, %s)"""
        records_to_insert = (user_name, password, user_email, app_name, url)
        cur.execute(postgres_query_to_insert, records_to_insert)
        conn.commit()
    except (Exception, psycog2.Error) as error:
        print(error)


def connect():
    try:
        conn = psycopg2.connect(host="localhost", port = 5432, database = 'passwordmanager', user= "postgres", password="tejasm")
        return conn
    except (Exception, psycog2.Error) as error:
        print(error)





