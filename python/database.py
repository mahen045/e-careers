import mysql.connector, db_config
config = db_config.config
try:
    db_connection = mysql.connector.connect(**config)
    cursor=db_connection.cursor()
    #sql_select_query = "select * from employee"
    sql_select_query = """select * from employee where emp_id=%s"""
    cursor.execute(sql_select_query, params=[102])
    data = cursor.fetchall()   #fetchone(), fetchmany(SIZE)
    for row in data:
        print('EmpId= ',row[0], )
        print('EmpName= ',row[1], )
        print('EmpDept= ',row[2], )
        print('EmpSalary= ',row[3], )
        print("---------------------")
    #Commit the changes
    db_connection.commit()
#Close the cursor and the connection
except mysql.connector.Error as e:
    print("Error reading data")
finally:
    if db_connection.is_connected():
        db_connection.close
        cursor.close()

