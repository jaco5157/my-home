from flask import Flask, request, Response, json
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'database'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'products'

database = MySQL(app)

@app.route('/product', methods=['POST'])
def product():
    data = request.form
    varekode = data['varekode']
    varenummer = data['varenummer']
    antal = data['antal']
    cursor = database.connection.cursor()
    cursor.execute("INSERT INTO inventory(varekode, varenummer, antal) VALUES (%s, %s, %s)", (varekode, varenummer, antal))
    database.connection.commit()
    cursor.close()
    return 'success'

@app.route('/products')
def products():
    cursor = database.connection.cursor()
    cursor.execute("SELECT * FROM inventory")
    response = []
    data = cursor.fetchall()
    cursor.close()
    for info in data:
        response.append(
            {
                "varekode": info[0],
                "varenummer": info[1],
                "antal": info[2]
            }
        )
    return Response(json.dumps(response))

if __name__ == '__main__':
    app.run(host='0.0.0.0')