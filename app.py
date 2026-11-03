from flask import Flask
import mysql.connector

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="viikko2user",
        password="Week2StrongPass123!",
        database="viikko2"
    )

@app.route("/")
def home():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("UPDATE counter SET count = count + 1 WHERE id = 1")
    connection.commit()

    cursor.execute("SELECT count FROM counter WHERE id = 1")
    count = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return f"""
    <!DOCTYPE html>
    <html lang="fi">
    <head>
        <meta charset="UTF-8">
        <title>Viikko 2 - Python-verkkosovellus</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 700px;
                margin: 50px auto;
                background: #f3f5f7;
                color: #222;
            }}
            .card {{
                background: white;
                padding: 30px;
                border-radius: 12px;
            }}
            h1 {{
                color: #245b8a;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Viikko 2: Python-verkkosovellus</h1>

            <p>Tämä sivu toimii Flaskilla Nginxin takana.</p>

            <p><strong>Sivun latauksia: {count}</strong></p>

            <p>
                Kävijälaskurin arvo tallennetaan MariaDB-tietokantaan.
                Jokainen sivun lataus kasvattaa laskurin arvoa yhdellä.
            </p>

            <h2>Uudelleenkäynnistystesti</h2>
            <p>Testi tehdään, kun sovellus on julkaistu.</p>

            <p><a href="/">Viikon 1 etusivulle</a></p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
