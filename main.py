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
        print(row[1])


def get_log(digit):
    sql = ("SELECT * FROM logs WHERE id = %s")

    cursor.execute(sql,(digit,))
    result = cursor.fetchone()
    
    for row in result:
        print(row)


def update_log(id, text):
    sql = ("UPDATE logs SET text = %s WHERE id = %s")
    cursor.execute(sql, (text,id))

    db.commit()

    print("Log {} updated".format(id))


def delete_log(id):
    sql = ("DELETE FROM logs WHERE id = %s")
    cursor.execute(sql, (id,))
    db.commit()

    print("Log Removed")



# add_log("This is a new user", "Chukwu Ifeanyi")
# add_log("This is a new user being added", "Adimoha SAmuel")
# add_log("Another user is being added", "Ehumadu REginald")

#get_logs()

# get_log(2)

# update_log(1, "Updated user data today")
delete_log(3)
get_logs()

