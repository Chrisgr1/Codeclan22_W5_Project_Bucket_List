import psycopg2  
import psycopg2.extras as ext
from os import environ

def run_sql(sql, values = None):
    conn = None
    results = []
    
    if 'POSTGRES_HOST' in environ:
        pg_host = environ['POSTGRES_HOST']

    if 'POSTGRES_PASSWORD_FILE' in environ:
        with open(environ['POSTGRES_PASSWORD_FILE']) as f:
            pg_password = f.read()
            f.close()

    if 'POSTGRES_USER' in environ:
        pg_user = environ['POSTGRES_USER']

    pg_dbname = 'bucket_list'



    try:
        conn=psycopg2.connect(
            host = pg_host,
            password = pg_password,
            dbname = pg_dbname,
            user = pg_user,
        )
        
        cur = conn.cursor(cursor_factory=ext.DictCursor)   
        cur.execute(sql, values)
        conn.commit()
        results = cur.fetchall()
        cur.close()           
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return results