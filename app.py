from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="viikko2user",
        password=os.environ.get("DB_PASSWORD"),
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
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Week 2 // Python Server</title>

        <style>
            * {{
                box-sizing: border-box;
            }}

            body {{
                margin: 0;
                min-height: 100vh;
                font-family: Arial, Helvetica, sans-serif;
                background:
                    radial-gradient(circle at top right, #6a00ff 0%, transparent 35%),
                    radial-gradient(circle at bottom left, #00d4ff 0%, transparent 30%),
                    #101018;
                color: white;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 40px 20px;
            }}

            .container {{
                width: 100%;
                max-width: 900px;
            }}

            .eyebrow {{
                color: #ffe600;
                text-transform: uppercase;
                letter-spacing: 4px;
                font-size: 13px;
                font-weight: 900;
                margin-bottom: 12px;
            }}

            h1 {{
                font-size: 52px;
                margin: 0 0 12px 0;
                line-height: 1.05;
                color: #ffffff;
                text-shadow: 4px 4px 0 #ff1744;
            }}

            .intro {{
                color: #d6e4ee;
                font-size: 18px;
                margin-bottom: 30px;
            }}

            .counter-card {{
                background: #70ff94;
                color: #111;
                border: 5px solid white;
                border-radius: 20px;
                padding: 32px;
                margin-bottom: 30px;
                box-shadow: 9px 9px 0 #000;
                transform: rotate(1deg);
            }}

            .counter-label {{
                color: #111;
                font-size: 14px;
                text-transform: uppercase;
                letter-spacing: 2px;
                font-weight: 900;
            }}

            .counter {{
                font-size: 90px;
                font-weight: 900;
                color: #ff1744;
                text-shadow: 4px 4px 0 white;
                margin: 5px 0;
                line-height: 1;
            }}

            .counter-text {{
                color: #111;
                font-weight: bold;
            }}

            .grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
                gap: 20px;
                margin-bottom: 30px;
            }}

            .card {{
                border-radius: 18px;
                padding: 22px;
                color: #111;
                border: 5px solid white;
                box-shadow: 7px 7px 0 #000;
                transform: rotate(-1deg);
            }}

            .card:nth-child(1) {{
                background: #ffea00;
            }}

            .card:nth-child(2) {{
                background: #ff70a6;
                transform: rotate(1deg);
            }}

            .card:nth-child(3) {{
                background: #70d6ff;
                transform: rotate(-2deg);
            }}

            .card h2 {{
                font-size: 22px;
                color: #111;
                margin-top: 5px;
            }}

            .card p {{
                color: #111;
                font-weight: 500;
                line-height: 1.6;
            }}

            .status {{
                display: inline-block;
                background: #111;
                color: #fff;
                border: 3px solid #fff;
                border-radius: 0;
                padding: 7px 12px;
                font-size: 12px;
                font-weight: 900;
                transform: rotate(-2deg);
            }}

            .links {{
                display: flex;
                flex-wrap: wrap;
                gap: 14px;
            }}

            a {{
                text-decoration: none;
                color: #111;
                background: #ffe600;
                padding: 13px 20px;
                border-radius: 10px;
                font-weight: 900;
                border: 4px solid white;
                box-shadow: 5px 5px 0 #000;
                transition: 0.2s;
            }}

            a:hover {{
                transform: translateY(-3px) rotate(-1deg);
                background: #ff9f1c;
            }}

            a.secondary {{
                background: #c77dff;
                color: #111;
            }}

            footer {{
                margin-top: 35px;
                color: #aab7c4;
                font-size: 13px;
                text-align: center;
            }}

            @media (max-width: 600px) {{
                h1 {{
                    font-size: 36px;
                }}

                .counter {{
                    font-size: 64px;
                }}
            }}
        </style>
    </head>

    <body>
        <main class="container">

            <div class="eyebrow">Linux Course // Week 02</div>

            <h1>Python meets the server.</h1>

            <p class="intro">
                Flask-verkkosovellus pyörii Gunicornilla Nginxin takana
                CSC cPoutan Ubuntu-palvelimella.
            </p>

            <section class="counter-card">
                <div class="counter-label">Sivun latauksia</div>
                <div class="counter">{count}</div>
                <div class="counter-text">
                    Jokainen tämän sivun lataus kasvattaa laskuria yhdellä.
                </div>
            </section>

            <section class="grid">

                <div class="card">
                    <div class="status">● LIVE</div>
                    <h2>TIETOKANTA EI UNOHDA 🧠</h2>
                    <p>
                        Kävijälaskuri tallennetaan MariaDB-tietokantaan.
                        Flask päivittää tietokannan arvoa jokaisella sivulatauksella,
                        joten laskurin arvo ei ole sidottu sovelluksen muistiin.
                    </p>
                </div>

                <div class="card">
                    <div class="status">● VERIFIED</div>
                    <h2>REBOOT SURVIVED ✅</h2>
                    <p>
                        Palvelin on käynnistetty uudelleen onnistuneesti.
                        Flask-sovellus käynnistyi automaattisesti systemd-palveluna
                        ja MariaDB:hen tallennettu kävijälaskuri säilytti arvonsa
                        uudelleenkäynnistyksen jälkeen.
                    </p>
                </div>

                <div class="card">
                    <div class="status">● STACK</div>
                    <h2>TEKNIIKKAPINO 🥞</h2>
                    <p>
                        Ubuntu 24.04 · Nginx · Python · Flask · Gunicorn · MariaDB
                    </p>
                </div>

            </section>

            <div class="links">
                <a href="https://github.com/Annijy/Linux-vko2"
                   target="_blank">
                    GitHub → lähdekoodi
                </a>

                <a class="secondary" href="/">
                    ← Viikon 1 sivulle
                </a>
            </div>

            <footer>
                Week 2 · Python-verkkosovellus ja tietokanta
            </footer>

        </main>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
