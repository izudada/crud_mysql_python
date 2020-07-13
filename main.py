from database import cursor, db

def add_log(text, user):
    sql = ("INSERT INTO logs(text, user) VALUES (%s, %s)")
    cursor.execute(sql, (text,user,))

    db.commit()
    log_id = cursor.lastrowid

    print("Added log {}".format(log_id))

add_log("This is a new user", "Chukwu Ifeanyi")
add_log("This is a new user being added", "Adimoha SAmuel")
add_log("Another user is being added", "Ehumadu REginald")