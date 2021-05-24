import mysql.connector
from flask import Flask, render_template, request
from display_tables import run_sql_file
conn = mysql.connector.connect(host="localhost", user="root", passwd="Lokshon1!", database="ISGOV3")
cursor = conn.cursor()
website = Flask(__name__)

# Home Page
@website.route('/')
def home_page():
    return render_template("homepage.html")

# Search Page
@website.route('/search')
def search():
    return render_template("searchPage.html")

@website.route('/search/party_position')
def party_position():
    run_sql_file("/Users/esteebrooks/Documents/DatabaseSystems/FinalProject/select_party_position.sql", conn, "H")
    return render_template("1.html")

@website.route('/search/party_ideology')
def party_ideology():
    run_sql_file("/Users/esteebrooks/Documents/DatabaseSystems/FinalProject/select_party_ideology.sql", conn, "H")
    return render_template("1.html")

@website.route('/search/government_recommendation')
def government_recommendation():
    run_sql_file("/Users/esteebrooks/Documents/DatabaseSystems/FinalProject/select_government_recommendation.sql", conn, "H")
    return render_template("1.html")

@website.route('/search/government')
def government():
    run_sql_file("/Users/esteebrooks/Documents/DatabaseSystems/FinalProject/select_government.sql", conn, "H")
    return render_template("1.html")

@website.route('/search/ideology')
def ideology():
    run_sql_file("/Users/esteebrooks/Documents/DatabaseSystems/FinalProject/select_ideology.sql", conn, "H")
    return render_template("1.html")

@website.route('/search/party')
def party():
    run_sql_file("/Users/esteebrooks/Documents/DatabaseSystems/FinalProject/select_party.sql", conn, "H")
    return render_template("1.html")


@website.route('/search/politician')
def politician():
    run_sql_file("/Users/esteebrooks/Documents/DatabaseSystems/FinalProject/select_politician.sql", conn, "H")
    return render_template("1.html")

@website.route('/search/position')
def position():
    run_sql_file("/Users/esteebrooks/Documents/DatabaseSystems/FinalProject/select_position.sql", conn, "H")
    return render_template("1.html")

@website.route('/search/recommendation')
def recommendation():
    run_sql_file("/Users/esteebrooks/Documents/DatabaseSystems/FinalProject/select_recommendation.sql", conn, "H")
    return render_template("1.html")

@website.route('/search/recommendation_party')
def recommendation_party():
    run_sql_file("/Users/esteebrooks/Documents/DatabaseSystems/FinalProject/select_recommendation_party.sql", conn, "H")
    return render_template("1.html")

# Create Page
@website.route('/create', methods=['GET', 'POST'])
def create():
    render_template('create.html')

    msg = ''
    if request.method == 'POST' and 'gov_number' in request.form and 'prime_min' in request.form and 'start_date' in request.form and 'recommendation_id' in request.form:
        gov_number = request.form['gov_number']
        prime_min = request.form['prime_min']
        start_date = request.form['start_date']
        recommendation_id = request.form['recommendation_id']

        print(gov_number, prime_min, start_date, recommendation_id)

        cursor.execute('SELECT * FROM government WHERE gov_number = %s', (gov_number,))
        g_number = cursor.fetchone()
        if g_number:
            msg = 'Government already exists!'
        else:
            cursor.execute('INSERT INTO government (gov_number, prime_min, start_date, recommendation_id) VALUES (%s, %s, %s, %s)',
                           (gov_number, prime_min, start_date, recommendation_id))
            conn.commit()
            msg = 'You have successfully created a new government!'

    elif request.method == 'POST':
        print('in post method')
        msg = 'Please fill out the form to create a new government!'

    return render_template('create.html', msg=msg)

# Update Page
@website.route('/update', methods=['GET', 'POST'])
def update():
    render_template('update.html')

    msg = ''
    if request.method == 'POST' and 'gov_number' in request.form and 'prime_min' in request.form and 'start_date' in request.form and 'recommendation_id' in request.form:
        gov_number = request.form['gov_number']
        prime_min = request.form['prime_min']
        start_date = request.form['start_date']
        recommendation_id = request.form['recommendation_id']

        cursor.execute('SELECT * FROM government WHERE gov_number = %s', (gov_number,))
        g_number = cursor.fetchone()
        print(g_number)
        if not g_number:
            msg = 'Government does not exist!'
        else:
            cursor.execute('UPDATE government SET prime_min =%s, start_date =%s, recommendation_id =%s WHERE gov_number =%s',
                           (prime_min, start_date, recommendation_id, gov_number))
            conn.commit()
            msg = 'You have successfully updated a government!'

    elif request.method == 'POST':
        msg = 'Please fill out the form to update!'
    return render_template('update.html', msg=msg)

# Delete Page
@website.route('/delete', methods=['GET', 'POST'])
def delete():
    render_template('delete.html')

    msg = ''
    if request.method == 'POST' and 'gov_number' in request.form:
        gov_number = request.form['gov_number']

        cursor.execute('SELECT * FROM government WHERE gov_number = %s', (gov_number,))
        g_number = cursor.fetchone()

        if not g_number:
            msg = 'Government does not exist already!'
        else:
            cursor.execute('DELETE FROM government WHERE gov_number = %s',
                           (gov_number,))
            conn.commit()
            msg = 'You have successfully deleted government ' + gov_number + '!'

    elif request.method == 'POST':
        msg = 'Please fill out the form to delete!'
    return render_template('delete.html', msg=msg)

# Select page
@website.route('/select', methods=['GET', 'POST'])
def select():
    render_template('select.html')

    msg = ''
    if request.method == 'POST' and 'gov_number' in request.form:
        gov_number = request.form['gov_number']

        cursor.execute('SELECT * FROM government WHERE gov_number = %s', (gov_number,))
        g_number = cursor.fetchone()

        if not g_number:
            msg = 'Government does not exist already!'

        else:
            f = open('/Users/esteebrooks/Documents/DatabaseSystems/FinalProject/select.sql', 'w')
            f.write('SELECT * FROM government WHERE gov_number = '+ gov_number)
            f.close()

            run_sql_file("/Users/esteebrooks/Documents/DatabaseSystems/FinalProject/select.sql", conn,
                         "H")
            return render_template("1.html")

    elif request.method == 'POST':
        msg = 'Please fill out the form to select!'
    return render_template('select.html', msg=msg)

if __name__ == '__main__':
    website.config['TEMPLATES_AUTO_RELOAD'] = True
    website.run()

conn.close()
