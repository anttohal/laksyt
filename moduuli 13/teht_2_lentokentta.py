import mysql.connector
from flask import Flask

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='lentopeli',
    user='kayttaja1',
    password='Munpiha',
    autocommit=True,
    collation='utf8mb4_general_ci'
    )

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
@app.route('/kenttä/<koodi>')

def kenttä(koodi):
    sql = f"select name, municipality from airport where ident = '{koodi}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)

    tulos = kursori.fetchall()[0]
    #print(f"Kenttä: {tulos[0]} Paikkakunta: {tulos[1]}")

    vastaus = {"ICAO": koodi, "Name": tulos[0], "Municipality": tulos[1]}

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)