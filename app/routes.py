"""cursor.execute(
            'INSERT INTO pokemon VALUES(%d, "%s", "%s","%s", %d, %d,%d, %d, %d,%d, %d, %d,%r)', int(row[0]), row[1], row[2], row[3], int(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), int(row[9]), int(row[10]), bool(row[11]))"""
'''
conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message':'User created successfully !'})
            else:
return json.dumps({'error':str(data[0])})
'''
from flask import render_template, request, redirect
from app import app, mysql
from app.models import db, Pokemon


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        conn = mysql.connect()
        cur = conn.cursor()
        cur.callproc('refresh_mv_now')
        cur.execute('select * from pokemon_mv;')
        data = cur.fetchall()
        cur.close()
        return render_template('index.html', data=data)


@app.route('/insert')
def insert():
    conn = mysql.connect()
    cursor = conn.cursor()
    csv_data = csv.reader(open('pokemon_copy.csv'))
    for row in csv_data:
        x = 'INSERT INTO pokemons VALUES( NULL, %a, %a, %a, % d, % d, % d, % d, % d, % d, % d,%d, % r)' % (row[1], row[2], row[3], int(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), int(row[9]), int(row[10]),int(row[11]) ,bool(row[12]))
        
        cursor.execute(x)
        print(type (row[0]))
    # close the connection to the database.
    conn.commit()
    cursor.close()
    return redirect('/')
