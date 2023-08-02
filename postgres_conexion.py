import psycopg2

hostname = 'localhost'
username = 'postgres'
pwd = 'postgres'
port_id = 5433
database = 'pmc_admin_v2'

try:
    conn = psycopg2.connect(
        
        host = hostname,
        user = username,
        password = pwd,
        port = port_id,
        dbname = database
    )


    conn.close()
except Exception as error:
    
    print(error)
    
    
    
