from flask import Flask, render_template_string, abort
import os

# ============================================================
# CONFIGURATION
# ============================================================

# Les photos sont directement à la racine de ton GitHub
app = Flask(__name__, static_folder=".", static_url_path="")

# ============================================================
# TES 22 CORAUX
# ============================================================

produits = [

    {
        "id": 1,
        "nom": "Chalice Bugatti",
        "prix": 15.00,
        "description": "",
        "image": "/ChaliceBugatti.jpg"
    },

    {
        "id": 2,
        "nom": "Montipora Fire Forest",
        "prix": 0.00,
        "description": "",
        "image": "/MontiporaFireForest.jpg"
    },

    {
        "id": 3,
        "nom": "Acropora Horrida",
        "prix": 0.00,
        "description": "",
        "image": "/accroporaHorrida.jpg"
    },

    {
        "id": 4,
        "nom": "Acropora Bill Murray",
        "prix": 0.00,
        "description": "",
        "image": "/acroporaBillMurray.jpg"
    },

    {
        "id": 5,
        "nom": "Acropora Ghost Town",
        "prix": 0.00,
        "description": "",
        "image": "/acroporaGhostTown.jpg"
    },

    {
        "id": 6,
        "nom": "Acropora Hacinthus",
        "prix": 0.00,
        "description": "",
        "image": "/acroporaHaycinthus.jpg"
    },

    {
        "id": 7,
        "nom": "Acropora Merlin",
        "prix": 0.00,
        "description": "",
        "image": "/acroporaMerlin.jpg"
    },

    {
        "id": 8,
        "nom": "Acropora Microcla-Dos Rose",
        "prix": 0.00,
        "description": "",
        "image": "/acroporaMicrocla-DosRose.jpg"
    },

    {
        "id": 9,
        "nom": "Acropora Nana Tricolor",
        "prix": 0.00,
        "description": "",
        "image": "/acroporaNanaTricolor.jpg"
    },

    {
        "id": 10,
        "nom": "Acropora Purple Haze",
        "prix": 0.00,
        "description": "",
        "image": "/acroporaPurpleHaze.png"
    },

    {
        "id": 11,
        "nom": "Acropora Tenuis",
        "prix": 0.00,
        "description": "",
        "image": "/acroporaTenuis.jpg"
    },

    {
        "id": 12,
        "nom": "Acropora Wicked Orchid",
        "prix": 0.00,
        "description": "",
        "image": "/acroporaWickedOrchid.jpg"
    },

    {
        "id": 13,
        "nom": "Anacropora",
        "prix": 0.00,
        "description": "",
        "image": "/anacropora.jpg"
    },

    {
        "id": 14,
        "nom": "Anacropora Goldenrod",
        "prix": 0.00,
        "description": "",
        "image": "/anacroporaGoldenrod.jpg"
    },

    {
        "id": 15,
        "nom": "Anacropora Tropicana",
        "prix": 0.00,
        "description": "",
        "image": "/anacroporaTropicana.jpg"
    },

    {
        "id": 16,
        "nom": "Euphyllia Parancora Gold",
        "prix": 0.00,
        "description": "",
        "image": "/euphylliaParancoraGold.jpg"
    },

    {
        "id": 17,
        "nom": "Euphyllia Parancora Rainbow Hologramme",
        "prix": 0.00,
        "description": "",
        "image": "/euphylliaParancoraRainbowHologramme.jpg"
    },

    {
        "id": 18,
        "nom": "Montipora Chili Pepper",
        "prix": 0.00,
        "description": "",
        "image": "/montiporaChiliPepper.jpg"
    },

    {
        "id": 19,
        "nom": "Montipora Grafted",
        "prix": 0.00,
        "description": "",
        "image": "/montiporaGrafted.jpg"
    },

    {
        "id": 20,
        "nom": "Montipora Hulk",
        "prix": 0.00,
        "description": "",
        "image": "/montiporaHulk.jpg"
    },

    {
        "id": 21,
        "nom": "Montipora Star Wars",
        "prix": 0.00,
        "description": "",
        "image": "/montiporaStarWars.jpg"
    },

    {
        "id": 22,
        "nom": "Montipora Beach Bum",
        "prix": 0.00,
        "description": "",
        "image": "/montippraBeachBum.jpg"
    }

]


# ============================================================
# DESIGN DU SITE
# ============================================================

HTML = """
<!DOCTYPE html>

<html lang="fr">

<head>

    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>Catalogue de Coraux</title>

    <style>

        * {
            box-sizing: border-box;
        }


        /* ================================
           FOND DU SITE
        ================================= */

        body {

            margin: 0;

            font-family:
                Arial,
                Helvetica,
                sans-serif;

            color: #ffffff;

            background:

                radial-gradient(
                    circle at 20% 20%,
                    rgba(0, 190, 220, 0.25),
                    transparent 30%
                ),

                radial-gradient(
                    circle at 80% 70%,
                    rgba(0, 120, 180, 0.25),
                    transparent 35%
                ),

                linear-gradient(
                    135deg,
                    #031b2b,
                    #063b52,
                    #02131f
                );

            min-height: 100vh;

        }


        /* ================================
           HEADER
        ================================= */

        .hero {

            text-align: center;

            padding:
                70px
                20px
                60px;

            background:

                linear-gradient(
                    rgba(0, 30, 45, 0.45),
                    rgba(0, 20, 35, 0.75)
                );

            border-bottom:
                1px solid
                rgba(255,255,255,0.12);

            position: relative;

            overflow: hidden;

        }


        .hero::before {

            content: "";

            position: absolute;

            width: 500px;
            height: 500px;

            background:
                rgba(0, 210, 255, 0.10);

            border-radius: 50%;

            top: -300px;
            left: -100px;

            filter: blur(20px);

        }


        .hero::after {

            content: "";

            position: absolute;

            width: 400px;
            height: 400px;

            background:
                rgba(0, 120, 255, 0.10);

            border-radius: 50%;

            bottom: -250px;
            right: -100px;

            filter: blur(20px);

        }


        .hero-content {

            position: relative;

            z-index: 2;

            max-width: 900px;

            margin: auto;

        }


        .coral-icon {

            font-size: 48px;

            margin-bottom: 15px;

        }


        .hero h1 {

            margin: 0;

            font-size: clamp(42px, 7vw, 76px);

            font-weight: 800;

            letter-spacing: -2px;

            background:
                linear-gradient(
                    90deg,
                    #ffffff,
                    #71e5ff,
                    #ffffff
                );

            -webkit-background-clip: text;

            -webkit-text-fill-color: transparent;

        }


        .hero p {

            margin-top: 18px;

            font-size: 20px;

            color: #c9edf5;

            letter-spacing: 0.5px;

        }


        /* ================================
           CONTENU
        ================================= */

        .container {

            max-width: 1250px;

            margin: auto;

            padding:
                50px
                20px
                80px;

        }


        .section-title {

            text-align: center;

            margin-bottom: 40px;

        }


        .section-title h2 {

            font-size: 32px;

            margin: 0;

        }


        .section-title p {

            color: #a8d4df;

            margin-top: 10px;

        }


        /* ================================
           GRILLE
        ================================= */

        .grid {

            display: grid;

            grid-template-columns:
                repeat(
                    auto-fit,
                    minmax(260px, 1fr)
                );

            gap: 28px;

        }


        /* ================================
           CARTE
        ================================= */

        .card {

            background:
                rgba(255,255,255,0.075);

            border:
                1px solid
                rgba(255,255,255,0.13);

            border-radius: 22px;

            overflow: hidden;

            backdrop-filter: blur(12px);

            box-shadow:
                0 15px 40px
                rgba(0,0,0,0.25);

            transition:
                transform 0.25s ease,
                box-shadow 0.25s ease;

        }


        .card:hover {

            transform:
                translateY(-8px);

            box-shadow:
                0 25px 55px
                rgba(0,0,0,0.4);

        }


        /* ================================
           IMAGE
        ================================= */

        .image-container {

            width: 100%;

            height: 270px;

            overflow: hidden;

            background: #061b27;

        }


        .image-container img {

            width: 100%;

            height: 100%;

            object-fit: cover;

            display: block;

            transition:
                transform 0.4s ease;

        }


        .card:hover
        .image-container img {

            transform: scale(1.06);

        }


        /* ================================
           INFOS
        ================================= */

        .card-content {

            padding: 22px;

        }


        .card h3 {

            margin:
                0
                0
                12px;

            font-size: 22px;

            color: #ffffff;

        }


        .description {

            min-height: 20px;

            color: #a9cbd4;

            font-size: 14px;

        }


        .bottom {

            display: flex;

            justify-content: space-between;

            align-items: center;

            margin-top: 22px;

        }


        .price {

            font-size: 21px;

            font-weight: bold;

            color: #65e6ff;

        }


        .button {

            display: inline-block;

            padding:
                10px
                16px;

            border-radius: 10px;

            background:
                linear-gradient(
                    135deg,
                    #00a8cc,
                    #007ea3
                );

            color: white;

            text-decoration: none;

            font-weight: bold;

            font-size: 14px;

            transition:
                transform 0.2s ease,
                opacity 0.2s ease;

        }


        .button:hover {

            transform:
                translateY(-2px);

            opacity: 0.9;

        }


        /* ================================
           FOOTER
        ================================= */

        footer {

            text-align: center;

            padding: 30px 20px;

            color: #8eb8c4;

            border-top:
                1px solid
                rgba(255,255,255,0.08);

            font-size: 14px;

        }


        /* ================================
           MOBILE
        ================================= */

        @media
        (max-width: 600px) {

            .hero {

                padding:
                    55px
                    15px
                    45px;

            }

            .hero h1 {

                letter-spacing:
                    -1px;

            }

            .hero p {

                font-size: 16px;

            }

            .container {

                padding:
                    35px
                    15px
                    60px;

            }

            .grid {

                gap: 20px;

            }

            .image-container {

                height: 250px;

            }

        }

    </style>

</head>


<body>


    <!-- ================================
         HEADER
    ================================= -->

    <header class="hero">

        <div class="hero-content">

            <div class="coral-icon">
                🪸
            </div>

            <h1>
                Catalogue de Coraux
            </h1>

            <p>
                Découvrez notre sélection de coraux
            </p>

        </div>

    </header>


    <!-- ================================
         PRODUITS
    ================================= -->

    <main class="container">

        <div class="section-title">

            <h2>
                Nos coraux
            </h2>

            <p>
                Explorez notre catalogue
            </p>

        </div>


        <div class="grid">

            {% for produit in produits %}

            <div class="card">

                <div class="image-container">

                    <img
                        src="{{ produit.image }}"
                        alt="{{ produit.nom }}"
                        onerror="this.style.display='none';"
                    >

                </div>


                <div class="card-content">

                    <h3>
                        {{ produit.nom }}
                    </h3>


                    {% if produit.description %}

                    <div class="description">
                        {{ produit.description }}
                    </div>

                    {% endif %}


                    <div class="bottom">

                        <div class="price">

                            {{ "%.2f"|format(produit.prix) }} €

                        </div>


                        <a
                            class="button"
                            href="/produit/{{ produit.id }}"
                        >
                            Voir
                        </a>

                    </div>

                </div>

            </div>

            {% endfor %}

        </div>

    </main>


    <!-- ================================
         FOOTER
    ================================= -->

    <footer>

        Catalogue de Coraux

    </footer>


</body>

</html>
"""


# ============================================================
# PAGE PRINCIPALE
# ============================================================

@app.route("/")
def accueil():

    return render_template_string(
        HTML,
        produits=produits
    )


# ============================================================
# PAGE D'UN CORAIL
# ============================================================

@app.route("/produit/<int:produit_id>")
def produit_detail(produit_id):

    produit = next(
        (
            p for p in produits
            if p["id"] == produit_id
        ),
        None
    )

    if produit is None:
        abort(404)

    HTML_DETAIL = """
    <!DOCTYPE html>

    <html lang="fr">

    <head>

        <meta charset="UTF-8">

        <meta name="viewport"
              content="width=device-width, initial-scale=1.0">

        <title>{{ produit.nom }}</title>

        <style>

            * {
                box-sizing: border-box;
            }

            body {

                margin: 0;

                font-family: Arial, sans-serif;

                color: white;

                background:
                    linear-gradient(
                        135deg,
                        #031b2b,
                        #063b52,
                        #02131f
                    );

                min-height: 100vh;

                padding: 30px 20px;

            }

            .page {

                max-width: 900px;

                margin: auto;

            }

            .back {

                display: inline-block;

                margin-bottom: 25px;

                color: #8feaff;

                text-decoration: none;

                font-weight: bold;

            }

            .card {

                background:
                    rgba(255,255,255,0.08);

                border:
                    1px solid
                    rgba(255,255,255,0.15);

                border-radius: 25px;

                overflow: hidden;

                backdrop-filter: blur(12px);

                box-shadow:
                    0 20px 60px
                    rgba(0,0,0,0.35);

            }

            .image {

                width: 100%;

                max-height: 600px;

                object-fit: cover;

                display: block;

            }

            .content {

                padding: 30px;

            }

            h1 {

                margin-top: 0;

                font-size: 38px;

            }

            .price {

                color: #65e6ff;

                font-size: 28px;

                font-weight: bold;

                margin-top: 20px;

            }

        </style>

    </head>

    <body>

        <div class="page">

            <a
                href="/"
                class="back"
            >
                ← Retour au catalogue
            </a>

            <div class="card">

                <img
                    src="{{ produit.image }}"
                    class="image"
                    alt="{{ produit.nom }}"
                >

                <div class="content">

                    <h1>
                        {{ produit.nom }}
                    </h1>

                    {% if produit.description %}

                    <p>
                        {{ produit.description }}
                    </p>

                    {% endif %}

                    <div class="price">

                        {{ "%.2f"|format(produit.prix) }} €

                    </div>

                </div>

            </div>

        </div>

    </body>

    </html>
    """

    return render_template_string(
        HTML_DETAIL,
        produit=produit
    )


# ============================================================
# LANCEMENT LOCAL
# ============================================================

if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            5000
        )
    )

    app.run(
        host="0.0.0.0",
        port=port,
        debug=True
    )
