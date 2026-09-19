from flask import Flask, render_template_string, abort
import os

# ============================================================
# CONFIGURATION
# ============================================================

app = Flask(__name__, static_folder=".", static_url_path="")


# ============================================================
# CATALOGUE DES CORAUX
# ============================================================

produits = [
    # ==================== ACROPORA ====================
    {"nom": "Acropora MH Horrida", "image": "accroporaHorrida.jpg"},
    {"nom": "Acropora AK Bill Murray", "image": "acroporaBillMurray.jpg"},
    {"nom": "Acropora RAH Purple Haze", "image": "acroporaGhostTown.jpg"},
    {"nom": "Acropora RAH Hyacinthus", "image": "acroporaHaycinthus.jpg"},
    {"nom": "Acropora RAH Merlin'staff", "image": "acroporaMerlin.jpg"},
    {"nom": "Acropora MicroclaDos Rose", "image": "acroporaMicrocla-DosRose.jpg"},
    {"nom": "Acropora Nana Tricolor", "image": "acroporaNanaTricolor.jpg"},
    {"nom": "Acropora Pikachu", "image": "acroporaPurpleHaze.png"},
    {"nom": "Acropora Tenuis", "image": "acroporaTenuis.jpg"},
    {"nom": "Acropora MH Wicked Orchid", "image": "acroporaWickedOrchid.jpg"},
    {"nom": "Acropora MH Little Raimbow", "image": "acroporaMhLitlleRaimbow.jpg"},
    {"nom": "Acropora RAH Ghost Town", "image": "acroporaRahGhostTown.jpg"},
    {"nom": "Acropora RAH Purple Haze", "image": "acroporaRahPurpleHaze.jpg"},
    {"nom": "Acropora RAH Raimbow Mango", "image": "acroporaRahRaimbowMango.jpg"},

    # ==================== ANACROPORA ====================
    {"nom": "Anacropora JF TNT", "image": "anacropora.jpg"},
    {"nom": "Anacropora AK Goldenrod", "image": "anacroporaGoldenrod.jpg"},
    {"nom": "Anacropora JF Tropicana", "image": "anacroporaTropicana.jpg"},

    # ==================== MONTIPORA ====================
    {"nom": "Montipora Fire Forest", "image": "MontiporaFireForest.jpg"},
    {"nom": "Montipora MH Chili Pepper", "image": "montiporaChiliPepper.jpg"},
    {"nom": "Montipora Grafted", "image": "montiporaGrafted.jpg"},
    {"nom": "Montipora RAH Hulk", "image": "montiporaHulk.jpg"},
    {"nom": "Montipora MH Star Wars", "image": "montiporaStarWars.jpg"},
    {"nom": "Montipora RAH Beach Bum", "image": "montippraBeachBum.jpg"},

    # ==================== EUPHYLLIA ====================
    {"nom": "Euphyllia Parancora Gold", "image": "euphylliaParancoraGold.jpg"},
    {"nom": "Euphyllia Parancora Raimbow Holograme", "image": "euphylliaParancoraRainbowHologramme.jpg"},

    # ==================== ZOANTHUS ====================
    {"nom": "Zoanthus Armagedon", "image": "zoanthusArmagedon.jpeg"},
    {"nom": "Zoanthus Bam Bam", "image": "zoanthusBambam.jpeg"},
    {"nom": "Zoanthus Captain America", "image": "zoanthusCaptainAmerica.jpeg"},
    {"nom": "Zoanthus Eyes Of RAH", "image": "zoanthusEyesOfRah.jpeg"},
    {"nom": "Zoanthus Fairy Muncher", "image": "zoanthusFairyMuncher.jpeg"},
    {"nom": "Zoanthus Fake Lime Chili", "image": "zoanthusFakeLimeChili.jpeg"},
    {"nom": "Zoanthus Miami Vice", "image": "zoanthusMiamiVice.jpeg"},
    {"nom": "Zoanthus Nirvana", "image": "zoanthusNirvana.jpeg"},
    {"nom": "Zoanthus Oompalo Ompa", "image": "zoanthusoompaloompa.jpeg"},
    {"nom": "Zoanthus Red Magician", "image": "zoanthusRedMagician.jpeg"},
    {"nom": "Zoanthus Seduction", "image": "zoanthusSeduction.jpeg"},
    {"nom": "Zoanthus Sonic Flair", "image": "zoanthusSonicFlair.jpeg"},
    {"nom": "Zoanthus Stratosphere", "image": "zoanthusStratosphere.jpeg"},
    {"nom": "Zoanthus Sunyday", "image": "zoanthusSunyday.jpeg"},
    {"nom": "Zoanthus Utter Chaos", "image": "zoanthusUtterChaos.jpeg"},

    # ==================== AUTRES ====================
    {"nom": "Chalice Bugatti", "image": "ChaliceBugatti.jpg"},
    {"nom": "Clavularia Tri Color", "image": "ClavulariaTriColor.jpeg"},
    {"nom": "Sarcophyton Fidji Vert Long Polypes", "image": "sarcophytonFidjiVertongPolipes.jpg"},
]


# ============================================================
# TROUVER AUTOMATIQUEMENT LES IMAGES
# ============================================================

def chemin_image(nom_fichier):

    # Cherche d'abord à la racine
    if os.path.exists(nom_fichier):
        return "/" + nom_fichier

    # Puis dans static/images
    if os.path.exists(
        os.path.join("static", "images", nom_fichier)
    ):
        return "/static/images/" + nom_fichier

    # Si le fichier n'est trouvé nulle part
    return "/" + nom_fichier


# ============================================================
# PAGE PRINCIPALE
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

        body {
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
            color: white;

            background:
                radial-gradient(
                    circle at 15% 20%,
                    rgba(0, 210, 255, 0.20),
                    transparent 30%
                ),

                radial-gradient(
                    circle at 85% 70%,
                    rgba(0, 120, 255, 0.18),
                    transparent 35%
                ),

                linear-gradient(
                    135deg,
                    #02131f,
                    #06384d,
                    #021923
                );

            min-height: 100vh;
        }


        .hero {
            text-align: center;
            padding: 70px 20px 60px;

            background:
                linear-gradient(
                    rgba(0, 30, 45, 0.35),
                    rgba(0, 15, 30, 0.65)
                );

            border-bottom:
                1px solid
                rgba(255,255,255,0.12);

            position: relative;
            overflow: hidden;
        }


        .hero-content {
            position: relative;
            z-index: 2;
            max-width: 900px;
            margin: auto;
        }


        .coral-icon {
            font-size: 52px;
            margin-bottom: 15px;
        }


        .hero h1 {
            margin: 0;

            font-size:
                clamp(42px, 7vw, 76px);

            font-weight: 800;

            letter-spacing: -2px;

            background:
                linear-gradient(
                    90deg,
                    #ffffff,
                    #6ee7ff,
                    #ffffff
                );

            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }


        .hero p {
            margin-top: 18px;

            font-size: 20px;

            color: #c9edf5;
        }


        .container {
            max-width: 1250px;
            margin: auto;

            padding:
                50px 20px 80px;
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


        .grid {
            display: grid;

            grid-template-columns:
                repeat(
                    auto-fit,
                    minmax(260px, 1fr)
                );

            gap: 28px;
        }


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
                rgba(0,0,0,0.40);
        }


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
            transform:
                scale(1.06);
        }


        .card-content {
            padding: 22px;
        }


        .card h3 {
            margin: 0;
            font-size: 21px;
            color: #ffffff;
        }


        .description {
            margin-top: 10px;
            color: #a9cbd4;
            font-size: 14px;
        }


        .bottom {
            display: flex;
            justify-content: flex-end;
            align-items: center;

            margin-top: 20px;
        }


        .button {
            display: inline-block;

            padding:
                10px 18px;

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


        footer {
            text-align: center;

            padding:
                30px 20px;

            color: #8eb8c4;

            border-top:
                1px solid
                rgba(255,255,255,0.08);

            font-size: 14px;
        }


        @media (max-width: 600px) {

            .hero {
                padding:
                    55px 15px 45px;
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
                    35px 15px 60px;
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


<main class="container">

    <div class="section-title">

        <h2>
            Nos coraux
        </h2>

        <p>
            Découvrez notre collection
        </p>

    </div>


    <div class="grid">

        {% for produit in produits %}

        <div class="card">

            <div class="image-container">

                <img
                    src="{{ chemin_image(produit.image) }}"
                    alt="{{ produit.nom }}"
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

                    <a
                        class="button"
                        href="/produit/{{ loop.index0 }}"
                    >
                        Voir le corail
                    </a>

                </div>

            </div>

        </div>

        {% endfor %}

    </div>

</main>


<footer>

    Catalogue de Coraux

</footer>


</body>

</html>
"""


# ============================================================
# ACCUEIL
# ============================================================

@app.route("/")
def accueil():

    return render_template_string(
        HTML,
        produits=produits,
        chemin_image=chemin_image
    )


# ============================================================
# PAGE DETAIL
# ============================================================

@app.route("/produit/<int:produit_id>")
def produit_detail(produit_id):

    if produit_id < 0 or produit_id >= len(produits):
        abort(404)

    produit = produits[produit_id]


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

                font-family:
                    Arial,
                    sans-serif;

                color: white;

                background:
                    linear-gradient(
                        135deg,
                        #02131f,
                        #06384d,
                        #021923
                    );

                min-height: 100vh;

                padding:
                    30px 20px;
            }


            .page {

                max-width: 900px;

                margin: auto;
            }


            .back {

                display: inline-block;

                margin-bottom:
                    25px;

                color:
                    #8feaff;

                text-decoration:
                    none;

                font-weight:
                    bold;
            }


            .card {

                background:
                    rgba(255,255,255,0.08);

                border:
                    1px solid
                    rgba(255,255,255,0.15);

                border-radius:
                    25px;

                overflow:
                    hidden;

                backdrop-filter:
                    blur(12px);

                box-shadow:
                    0 20px 60px
                    rgba(0,0,0,0.35);
            }


            .image {

                width: 100%;

                max-height:
                    600px;

                object-fit:
                    cover;

                display:
                    block;
            }


            .content {

                padding:
                    30px;
            }


            h1 {

                margin-top:
                    0;

                font-size:
                    38px;
            }


            .description {

                color:
                    #b8dbe4;

                line-height:
                    1.6;
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
                    src="{{ chemin_image(produit.image) }}"
                    class="image"
                    alt="{{ produit.nom }}"
                >


                <div class="content">

                    <h1>
                        {{ produit.nom }}
                    </h1>


                    {% if produit.description %}

                    <p class="description">
                        {{ produit.description }}
                    </p>

                    {% endif %}

                </div>

            </div>

        </div>

    </body>

    </html>
    """


    return render_template_string(
        HTML_DETAIL,
        produit=produit,
        chemin_image=chemin_image
    )


# ============================================================
# LANCEMENT
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
