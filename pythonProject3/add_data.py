import psycopg2, platform, datetime
date =  str(datetime.datetime.now()) # get current date and time
print(date)
pname = str(platform.platform()) # get current platform
print(pname)
# Connect to the database
cmd_insert_table = f"""
INSERT INTO public.Analytics (name, time) values('{pname}', '{date}');
                    """
# Execute the query only adding system name and date
try:
    #connect to the PostgreSQL database
    con = psycopg2.connect(database='db5lge65r9fjqt',
                           user='fqcfjtiyfevdea',
                           password='bc7496a3821e1ab88cce35b73ce3f032c5502609eadb5bcb18c698661fa99862',
                           host='ec2-18-214-134-226.compute-1.amazonaws.com',
                           port='5432')
    cur = con.cursor()
    cur.execute(cmd_insert_table)
    con.commit()
    # print('Value inserted successfully in PostgreSQL')
except Exception as e:
    print("I am unable to connect to the database")
    print("Cause: ", e)
finally:
    if con is not None:
        con.close()
        # print("Database connection closed.")