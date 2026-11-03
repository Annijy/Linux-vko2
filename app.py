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
                    radial-gradient(circle at top right, #143d59 0%, transparent 35%),
                    radial-gradient(circle at bottom left, #1b5e4b 0%, transparent 30%),
                    #07111c;
                color: #e8f1f7;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 40px 20px;
            }}

            .container {{
                width: 100%;
                max-width: 850px;
            }}

            .eyebrow {{
                color: #62f5bf;
                text-transform: uppercase;
                letter-spacing: 4px;
                font-size: 12px;
                font-weight: bold;
                margin-bottom: 12px;
            }}

            h1 {{
                font-size: 48px;
                margin: 0 0 12px 0;
                line-height: 1.05;
            }}

            .intro {{
                color: #9eb5c6;
                font-size: 18px;
                margin-bottom: 30px;
            }}

            .counter-card {{
                background: rgba(255,255,255,0.07);
                border: 1px solid rgba(255,255,255,0.12);
                border-radius: 20px;
                padding: 32px;
                margin-bottom: 22px;
                backdrop-filter: blur(10px);
            }}

            .counter-label {{
                color: #9eb5c6;
                font-size: 14px;
                text-transform: uppercase;
                letter-spacing: 2px;
            }}

            .counter {{
                font-size: 76px;
                font-weight: bold;
                color: #62f5bf;
                margin: 4px 0;
                line-height: 1;
            }}

            .counter-text {{
                color: #c7d6e0;
            }}

            .grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
                gap: 16px;
                margin-bottom: 22px;
            }}

            .card {{
                background: rgba(255,255,255,0.055);
                border: 1px solid rgba(255,255,255,0.1);
                border-radius: 16px;
                padding: 22px;
            }}

            .status {{
                display: inline-block;
                background: rgba(98,245,191,0.12);
                color: #62f5bf;
                border: 1px solid rgba(98,245,191,0.35);
                border-radius: 999px;
                padding: 6px 11px;
                font-size: 12px;
                font-weight: bold;
                margin-bottom: 10px;
            }}

            h2 {{
                font-size: 19px;
                margin: 5px 0 10px;
            }}

            p {{
                line-height: 1.65;
            }}

            .card p {{
                color: #aebfcb;
                margin-bottom: 0;
            }}

            .links {{
                display: flex;
                flex-wrap: wrap;
                gap: 12px;
            }}

            a {{
                text-decoration: none;
                color: #07111c;
                background: #62f5bf;
                padding: 12px 18px;
                border-radius: 10px;
                font-weight: bold;
                transition: 0.2s;
            }}

            a:hover {{
                transform: translateY(-2px);
                background: #8affd2;
            }}

            a.secondary {{
                color: #e8f1f7;
                background: rgba(255,255,255,0.08);
                border: 1px solid rgba(255,255,255,0.15);
            }}

            footer {{
                margin-top: 30px;
                color: #587083;
                font-size: 13px;
            }}

            @media (max-width: 600px) {{
                h1 {{
                    font-size: 36px;
                }}

                .counter {{
                    font-size: 60px;
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
                    <h2>Tietokanta</h2>
                    <p>
                        Kävijälaskuri tallennetaan MariaDB-tietokantaan.
                        Flask päivittää tietokannan arvoa jokaisella sivulatauksella,
                        joten laskurin arvo ei ole sidottu sovelluksen muistiin.
                    </p>
                </div>

                <div class="card">
                    <div class="status">● PERSISTENT</div>
                    <h2>Uudelleenkäynnistystesti</h2>
                    <p>
                        Palvelimen uudelleenkäynnistystesti tehdään lopuksi.
                        Tavoitteena on varmistaa, että kävijälaskurin arvo säilyy
                        ja Flask-sovellus käynnistyy automaattisesti uudelleen.
                    </p>
                </div>

                <div class="card">
                    <div class="status">● STACK</div>
                    <h2>Tekniikat</h2>
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
