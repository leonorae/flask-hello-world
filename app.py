from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Leonora Goble in 3308!'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect('postgresql://leonorae_postgres_hello_user:ekwIlLb9DFxBgjvrnFH7IcgKvqHBYzGU@dpg-csl8eem8ii6s73c1e47g-a/leonorae_postgres_hello')
    conn.close()
    return 'Database Connection Successful'

@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect('postgresql://leonorae_postgres_hello_user:ekwIlLb9DFxBgjvrnFH7IcgKvqHBYzGU@dpg-csl8eem8ii6s73c1e47g-a/leonorae_postgres_hello')
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO Basketball (First, Last, City, Name, Number)
    Values
    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Populated"

@app.route('/db_select')
def selecting():
    conn = psycopg2.connect('postgresql://leonorae_postgres_hello_user:ekwIlLb9DFxBgjvrnFH7IcgKvqHBYzGU@dpg-csl8eem8ii6s73c1e47g-a/leonorae_postgres_hello')
    cur = conn.cursor()
    cur.execute('''
    SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.close
    response_string='<table>'
    for player in records:
        response_string+='<tr>'
        for info in player:
            response_string+='<td>{}</td>'.format(info)
        response_string+='</tr>'
    response_string+='</table>'
    return response_string
