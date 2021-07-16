from flask import Flask, request, Response, json
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'database'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'people'

database = MySQL(app)

@app.route('/person', methods=['POST'])
def person():
    data = request.form
    firstname = data['firstname']
    lastname = data['lastname']
    cursor = database.connection.cursor()
    cursor.execute("INSERT INTO people_table(firstname, lastname) VALUES (%s, %s)", (firstname, lastname))
    database.connection.commit()
    cursor.close()
    return 'success'

@app.route('/persons')
def persons():
    cursor = database.connection.cursor()
    cursor.execute("SELECT * FROM people_table")
    response = []
    data = cursor.fetchall()
    cursor.close()
    for info in data:
        response.append(
            {
                "Firstname": info[1],
                "PersonID": info[0],
                "Lastname": info[2]
            }
        )
    return Response(json.dumps(response))

if __name__ == '__main__':
    app.run(host='0.0.0.0')