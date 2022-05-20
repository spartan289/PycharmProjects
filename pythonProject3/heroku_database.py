import psycopg2, os

cmd_create_table = """CREATE TABLE Analytics (
                        Name VARCHAR(255) NOT NULL,
                        TIME TIMESTAMP NOT NULL
                        )
                    """
try:
    con = psycopg2.connect(database='db5lge65r9fjqt',
                           user='fqcfjtiyfevdea',
                           password='bc7496a3821e1ab88cce35b73ce3f032c5502609eadb5bcb18c698661fa99862',
                           host='ec2-18-214-134-226.compute-1.amazonaws.com',
                           port='5432')
    cur = con.cursor()
    cur.execute(cmd_create_table)
    con.commit()
    print('Table created successfully in PostgreSQL')
except Exception as e:
    print("I am unable to connect to the database")
    print("Cause: ", e)
finally:
    if con is not None:
        con.close()
        print("Database connection closed.")
