from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from config import Config
 
app = Flask(__name__)
app.config.from_object(Config)
mysql = MySQL(app)
 
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO guestbook (name, message) VALUES (%s, %s)", (name, message))
        mysql.connection.commit()
        cur.close()
        return redirect('/')
    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT name, message FROM guestbook ORDER BY id DESC")
        entries = cur.fetchall()
        cur.close()
        return render_template('index.html', entries=entries)
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
