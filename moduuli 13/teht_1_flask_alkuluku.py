from flask import Flask

app = Flask(__name__)
@app.route('/alkuluku/<luku>')

# Tarkistaa, onko luku alkuluku
def alkuluku(luku):
    luku = int(luku)
    on_alkuluku = True
    for i in range(2, int(pow(luku, 0.5)) + 1):
        if (luku <= 0) or (luku % i == 0):
            on_alkuluku = False
            break

    vastaus = {
        "Number": luku,
        "isPrime": on_alkuluku}

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)