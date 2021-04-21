import psycopg2

def insert_password(user_name, passw, user_email, app_name, url):
    try:
        conn = connect()
        cur = conn.cursor()
        postgres_query_to_insert = """ INSERT INTO passwords(user_name, passw, user_email, app_name, url) VALUES (%s, %s, %s, %s, %s)"""
        records_to_insert = (user_name, passw, user_email, app_name, url)
        cur.execute(postgres_query_to_insert, records_to_insert)
        conn.commit()
        print("  "*50)
        print("--"*50)
        print("Your Password and details related to password is Successfully saved in database")
        print("--"*50)
        print("  "*50)
    except (Exception, psycopg2.Error) as error:
        print(error)


def connect():
    try:
        conn = psycopg2.connect(host="localhost", port = 5432, database = 'passwordmanager', user= "postgres", password="tejasm")
        return conn
    except (Exception, psycopg2.Error) as error:
        print(error)


def find_password(app_name):
    try:
        conn = connect()
        cur = conn.cursor()
        postgres_query_find_password = """ SELECT passw FROM passwords WHERE app_name = '""" + app_name + "'"
        cur.execute(postgres_query_find_password, app_name)
        conn.commit()
        result = cur.fetchone()
        print("  "*50)
        print("--"*50)
        print("Password for the " + app_name + " is : ")
        print(result[0])

    except (Exception, psycopg2.Error) as error:
        print(error)

def find_users(user_email):
    data = ('User Name : ', 'Password : ', 'User Email : ', 'App Name : ', 'URL : ' )
    try:
        conn = connect()
        cur = conn.cursor()
        postgres_query_find_user = """ SELECT * FROM passwords WHERE user_email = '""" + user_email + "'"
        cur.execute(postgres_query_find_user, user_email)
        conn.commit()
        result = cur.fetchall()
        print("  "*50)
        print("--"*50)
        print("  "*25 + "RESULT" + "  "*25)
        for row in result:
            for i in range(0, len(row)-1):
                print(data[i] + row[i])
        print("--"*50)
        print("  "*50)
    except (Exception, psycopg2.Error) as error:
        print(error)

