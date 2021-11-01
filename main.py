### Integrate HTML With Flask
### HTTP verb GET And POST
from flask import Flask,redirect,url_for,render_template,request
import mysql.connector as sql

connection = sql.connect(
    host = 'localhost',
    user = 'root',
    password='admin',
    database='data'
)

print(connection)
mycursor = connection.cursor()


def search_qurey(q1,q2):
    qury = f"SELECT * FROM student WHERE {q1} = '{q2}'"
    mycursor.execute(qury)
    result = mycursor.fetchall()
    return render_template("result.html", len = len(result), Pokemons = result)


app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"

    return render_template('result.html',result=res)


### Result checker submit html page
@app.route('/submit',methods=['POST','GET'])
def submit():
   
    if request.method=='POST':
        q1=str(request.form['select'])

        q2=str(request.form['serchq'])
        
        qury = f"SELECT * FROM student WHERE {q1} = '{q2}'"
        mycursor.execute(qury)
        result = mycursor.fetchall()
        return render_template("result.html", len = len(result), Pokemons = result)


    



if __name__=='__main__':
    app.run(debug=True)