import psycopg2

def create_tables(table_name, **kwargs):
    cur.execute("""
                CREATE TABLE IF NOT EXISTS %s (
                id SERIAL PRIMARY KEY);
                """ % (table_name,))
    conn.commit()
    for key, value in kwargs.items():
        cur.execute("""
                    ALTER TABLE %s 
                    ADD COLUMN %s %s;
                    """ % (table_name, key, value))
        conn.commit()
    return print("DONE!")

def add_user(first_name, last_name, email):
    cur.execute("""
                INSERT INTO users(first_name, last_name, email)
                VALUES ('%s', '%s', '%s');
                """ % (first_name, last_name, email))
    conn.commit()
    return print("DONE!")

def add_phone(user_id, number):
    cur.execute("""
                INSERT INTO phones(user_id, number)
                VALUES ('%s', '%s');
                """ % (user_id, number))
    conn.commit()
    return print("DONE!")

def change_user_data(table_name, column_name, new_data, id):
    cur.execute("""
                UPDATE %s
                   SET %s = '%s'
                 WHERE id = %s;
                """ % (table_name, column_name, new_data, id))
    conn.commit()
    return print("DONE!")

def delete_phone(id):
    cur.execute("""
                DELETE FROM phones
                 WHERE id = %s;
                """ % (id))
    conn.commit()
    return print("DONE!")

def delete_user(id):
    cur.execute("""
                DELETE FROM users
                 WHERE id = %s;
                """ % (id))
    conn.commit()
    return print("DONE!")

def find_user(data):
    cur.execute("""
                SELECT u.id, u.first_name, u.last_name, u.email, p.number FROM users u
                  JOIN phones p ON p.user_id = u.id
                 WHERE u.first_name IN ('%s') 
                    OR u.last_name IN ('%s') 
                    OR u.email IN ('%s') 
                    OR p.number IN ('%s');
                """ % (data, data, data, data))
    return print(cur.fetchall())

conn = psycopg2.connect(database = 'SQL5', user = 'postgres', password = 'U152433')
with conn.cursor() as cur:
    # create_tables('users', first_name='VARCHAR(20) NOT NULL',
    #                              last_name='VARCHAR(20) NOT NULL',
    #                              email='VARCHAR(40) NOT NULL UNIQUE')
    # create_tables('phones', user_id='INTEGER NOT NULL REFERENCES users(id)',
    #                               number='VARCHAR(20) UNIQUE')
    # add_user('Alex', 'Hirsh', 'alex1134@gmail.com')
    # add_user('Pavel', 'Ololoshovich', 'pavlusha9223@gmail.com')
    # add_phone('1', '8-929-234-34-11')
    # change_user_data('phones', 'number', '8-999-222-22-22', '1')
    # change_user_data('users', 'last_name', 'Pupckin', '2')
    # delete_phone('1')
    # delete_user('2')
    # find_user('Alex')
# conn.close()

