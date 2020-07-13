from database import cursor, db

def add_log(text, user):
    sql = ("INSERT INTO logs(text, user) VALUES (%s, %s)")
    cursor.execute(sql, (text,user,))

    db.commit()
    log_id = cursor.lastrowid

    print("Added log {}".format(log_id))


def get_logs():
    sql = ("SELECT * FROM logs ORDER BY created DESC")

    cursor.execute(sql)
    result = cursor.fetchall()
    
    for row in result:
        print(row[2])


def get_log(digit):
    sql = ("SELECT * FROM logs WHERE id = %s")

    cursor.execute(sql,(digit,))
    result = cursor.fetchone()
    
    for row in result:
        print(row)


# add_log("This is a new user", "Chukwu Ifeanyi")
# add_log("This is a new user being added", "Adimoha SAmuel")
# add_log("Another user is being added", "Ehumadu REginald")

#get_logs()

get_log(2)