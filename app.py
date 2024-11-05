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

