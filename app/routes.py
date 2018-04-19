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
from flask import render_template, request, redirect, flash, url_for, session
from app import app, mysql
from app.admin import auth
'''
@app.route('/')
def index():
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute('show tables;')
    data = cur.fetchall()
    cur.close()
    print (data)
    return 'HELLO'
'''
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        if session.get('auth'):
            return render_template('index.html')
        else:
            return redirect(url_for('login'))
    else:
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute('desc pokemon_mv;')
        data =cur.fetchmany(3)
        attrs = []
        for d in data:
            attrs.append(d[0])

        cur.execute('select * from pokemons;')
        data1 = cur.fetchmany(5)

        cur.execute('select * from pokemons;')
        data2 = cur.fetchmany(5)
        
        cur.close()
        print(len(data1),len(data2))
        return render_template('relation.html', attrs=attrs,data1=data1, data2=data2, data=data1)


@app.route('/insert', methods=['POST'])
def insert():
    conn = mysql.connect()
    cursor = conn.cursor()
    row = []
    data = request.form
    for d in data:
        row.append(data[d])
    print(row)
    #insert some values into pokemon_stats and some in pokemon__details
    x = 'INSERT INTO pokemons VALUES( NULL, %a, %a, %a, % d, % d, % d, % d, % d, % d, % d,%d, % r)' % (row[1], row[2], row[3], int(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), int(row[9]), int(row[10]),int(row[11]) ,bool(row[12]))
    print(x)
    '''cursor.execute(x)
    conn.commit()
    cursor.close()'''
    return redirect('/')


'''
login to the site to view/edit rest of the file
'''
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'GET':
        if not session.get('auth'):
            return render_template('login.html')
        else:
            flash('Already logged in')
            return redirect(url_for('index'))
    else:    
        if auth(request.form['username'],request.form['password']):
            flash('Successfully logged in')
            return redirect(url_for('index'))
        else:
            flash('Wrong credentials')
            return redirect(url_for('login'))

@app.route('/table/1')
def table1():
    #for table 1
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('desc pokemons')
    data = cursor.fetchall()
    #table headers are in attrs
    attrs = []
    for d in data:
        attrs.append(d[0])
    x = 'select * from pokemons;'
    cursor.execute(x)
    #table content is in data
    data = cursor.fetchall()
    cursor.close()
    return render_template('relation.html',attrs=attrs,data=data)

@app.route('/table/2')
def table2():
    #for table 2
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('desc pokemons')
    data = cursor.fetchall()
    #table headers are in attrs
    attrs = []
    for d in data:
        attrs.append(d[0])
    x = 'select * from pokemons;'
    cursor.execute(x)
    #table content is in data
    data = cursor.fetchall()
    cursor.close()
    return render_template('relation.html',attrs=attrs,data=data)


    '''
    name name
    type1 type1
    type2 type2
    hp hp
    attack attack
    defense defense
    sp_attack
    sp_defense
    speed
    gen
    leg
    '''