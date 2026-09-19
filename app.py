# Créé par natan, le 19/09/2026 en Python 3.7
from flask import Flask, render_template_string, abort
import qrcode
import os

app = Flask(__name__)


# ==========================================================
# CONFIGURATION
# ==========================================================

# Cette adresse sera remplacée par l'adresse de ton site
# après l'hébergement.
PUBLIC_URL = "https://TON-SITE.onrender.com"


# ==========================================================
# PRODUITS
# ==========================================================

produits = [
    {"id": 1, "nom": "Chalice Bugatti", "prix": 0.00, "description": "", "image": "/ChaliceBugatti.jpg"},
    {"id": 2, "nom": "Montipora Fire Forest", "prix": 0.00, "description": "", "image": "/MontiporaFireForest.jpg"},
    {"id": 3, "nom": "Acropora Horrida", "prix": 0.00, "description": "", "image": "/acroporaHorrida.jpg"},
    {"id": 4, "nom": "Acropora Bill Murray", "prix": 0.00, "description": "", "image": "/acroporaBillMurray.jpg"},
    {"id": 5, "nom": "Acropora Ghost Town", "prix": 0.00, "description": "", "image": "/acroporaGhostTown.jpg"},
    {"id": 6, "nom": "Acropora Hacinthus", "prix": 0.00, "description": "", "image": "/acroporaHacinthus.jpg"},
    {"id": 7, "nom": "Acropora Merlin", "prix": 0.00, "description": "", "image": "/acroporaMerlin.jpg"},
    {"id": 8, "nom": "Acropora Microcla-Dos Rose", "prix": 0.00, "description": "", "image": "/acroporaMicrocla-DosRose.jpg"},
    {"id": 9, "nom": "Acropora Nana Tricolor", "prix": 0.00, "description": "", "image": "/acroporaNanaTricolor.jpg"},
    {"id": 10, "nom": "Acropora Purple Haze", "prix": 0.00, "description": "", "image": "/acroporaPurpleHaze.png"},
    {"id": 11, "nom": "Acropora Tenuis", "prix": 0.00, "description": "", "image": "/acroporaTenuis.jpg"},
    {"id": 12, "nom": "Acropora Wicked Orchid", "prix": 0.00, "description": "", "image": "/acroporaWickedOrchid.jpg"},
    {"id": 13, "nom": "Anacropora", "prix": 0.00, "description": "", "image": "/anacropora.jpg"},
    {"id": 14, "nom": "Anacropora Goldenrod", "prix": 0.00, "description": "", "image": "/anacroporaGoldenrod.jpg"},
    {"id": 15, "nom": "Anacropora Tropicana", "prix": 0.00, "description": "", "image": "/anacroporaTropicana.jpg"},
    {"id": 16, "nom": "Euphyllia Parancora Gold", "prix": 0.00, "description": "", "image": "/euphylliaParancoraGold.jpg"},
    {"id": 17, "nom": "Euphyllia Parancora Rainbow Hologramme", "prix": 0.00, "description": "", "image": "/euphylliaParancoraRainbowHologramme.jpg"},
    {"id": 18, "nom": "Montipora Chili Pepper", "prix": 0.00, "description": "", "image": "/montiporaChiliPepper.jpg"},
    {"id": 19, "nom": "Montipora Grafted", "prix": 0.00, "description": "", "image": "/montiporaGrafted.jpg"},
    {"id": 20, "nom": "Montipora Hulk", "prix": 0.00, "description": "", "image": "/montiporaHulk.jpg"},
    {"id": 21, "nom": "Montipora Star Wars", "prix": 0.00, "description": "", "image": "/montiporaStarWars.jpg"},
    {"id": 22, "nom": "Montipora Beach Bum", "prix": 0.00, "description": "", "image": "/montippraBeachBum.jpg"}
]

# ==========================================================
# PAGE PRINCIPALE
# ==========================================================

PAGE_ACCUEIL = """

<!DOCTYPE html>

<html lang="fr">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>Mon Catalogue</title>


<style>

/* ------------------------------ */
/* GENERAL */
/* ------------------------------ */

* {
    box-sizing: border-box;
}

body {

    margin: 0;

    font-family:
        Arial,
        Helvetica,
        sans-serif;

    background: #f5f6f8;

    color: #171717;
}


/* ------------------------------ */
/* HEADER */
/* ------------------------------ */

header {

    background:
        linear-gradient(
            135deg,
            #111827,
            #26364d
        );

    color: white;

    text-align: center;

    padding: 55px 20px;
}


header h1 {

    margin: 0;

    font-size: 42px;
}


header p {

    margin-top: 12px;

    font-size: 18px;

    color: #d7dce5;
}


/* ------------------------------ */
/* CONTENEUR */
/* ------------------------------ */

.container {

    max-width: 1100px;

    margin: auto;

    padding: 30px 20px 60px;
}


/* ------------------------------ */
/* QR CODE */
/* ------------------------------ */

.qr-box {

    background: white;

    border-radius: 20px;

    padding: 25px;

    text-align: center;

    margin-bottom: 35px;

    box-shadow:
        0 8px 30px rgba(0,0,0,0.07);
}


.qr-box h2 {

    margin-top: 0;
}


.qr-box img {

    width: 180px;

    max-width: 70%;

    margin-top: 10px;
}


/* ------------------------------ */
/* PRODUITS */
/* ------------------------------ */

.produits {

    display: grid;

    grid-template-columns:
        repeat(
            auto-fit,
            minmax(250px, 1fr)
        );

    gap: 25px;
}


/* ------------------------------ */
/* CARTE */
/* ------------------------------ */

.produit {

    background: white;

    border-radius: 20px;

    overflow: hidden;

    box-shadow:
        0 8px 25px rgba(0,0,0,0.08);

    transition:
        transform 0.2s,
        box-shadow 0.2s;
}


.produit:hover {

    transform: translateY(-5px);

    box-shadow:
        0 15px 35px rgba(0,0,0,0.12);
}


.produit img {

    width: 100%;

    height: 240px;

    object-fit: cover;

    display: block;
}


/* ------------------------------ */
/* INFORMATIONS */
/* ------------------------------ */

.infos {

    padding: 22px;
}


.infos h2 {

    margin: 0 0 10px;

    font-size: 22px;
}


.description {

    color: #6b7280;

    line-height: 1.5;

    min-height: 45px;
}


.prix {

    font-size: 26px;

    font-weight: bold;

    margin:
        20px 0;
}


/* ------------------------------ */
/* BOUTON */
/* ------------------------------ */

.bouton {

    display: block;

    text-align: center;

    text-decoration: none;

    background: #111827;

    color: white;

    padding: 14px;

    border-radius: 12px;

    font-weight: bold;

    transition:
        background 0.2s;
}


.bouton:hover {

    background: #374151;
}


/* ------------------------------ */
/* FOOTER */
/* ------------------------------ */

footer {

    text-align: center;

    color: #777;

    padding: 30px;

    font-size: 14px;
}


/* ------------------------------ */
/* TELEPHONE */
/* ------------------------------ */

@media (max-width: 600px) {

    header {

        padding: 45px 20px;
    }

    header h1 {

        font-size: 32px;
    }

    .container {

        padding:
            20px 15px 45px;
    }

    .produit img {

        height: 220px;
    }
}

</style>

</head>


<body>


<header>

    <h1>Mon Catalogue</h1>

    <p>
        Découvrez nos produits
    </p>

</header>


<div class="container">


    <!-- QR CODE -->

    <div class="qr-box">

        <h2>
            📱 Scannez pour accéder au catalogue
        </h2>

        <p>
            Scannez ce QR code avec votre téléphone.
        </p>

        <img
            src="/static/qrcode/catalogue.png"
            alt="QR Code"
        >

    </div>


    <!-- PRODUITS -->

    <div class="produits">

        {% for produit in produits %}

        <div class="produit">

            <img
                src="{{ produit.image }}"
                alt="{{ produit.nom }}"
            >

            <div class="infos">

                <h2>
                    {{ produit.nom }}
                </h2>

                <p class="description">
                    {{ produit.description }}
                </p>

                <div class="prix">

                    {{ "%.2f"|format(produit.prix) }} €

                </div>

                <a
                    class="bouton"
                    href="/produit/{{ produit.id }}"
                >
                    Voir le produit →
                </a>

            </div>

        </div>

        {% endfor %}

    </div>


</div>


<footer>

    © 2026 — Mon Catalogue

</footer>


</body>

</html>

"""


# ==========================================================
# PAGE D'UN PRODUIT
# ==========================================================

PAGE_PRODUIT = """

<!DOCTYPE html>

<html lang="fr">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>{{ produit.nom }}</title>


<style>

body {

    margin: 0;

    font-family: Arial, sans-serif;

    background: #f5f6f8;
}


.container {

    max-width: 700px;

    margin: 40px auto;

    padding: 20px;
}


.carte {

    background: white;

    border-radius: 20px;

    overflow: hidden;

    box-shadow:
        0 10px 35px rgba(0,0,0,0.1);
}


.carte img {

    width: 100%;

    max-height: 450px;

    object-fit: cover;
}


.infos {

    padding: 30px;
}


h1 {

    margin-top: 0;

    font-size: 32px;
}


.description {

    color: #666;

    line-height: 1.6;
}


.prix {

    font-size: 30px;

    font-weight: bold;

    margin: 25px 0;
}


.retour {

    display: inline-block;

    padding: 13px 20px;

    background: #111827;

    color: white;

    text-decoration: none;

    border-radius: 12px;
}

</style>

</head>


<body>


<div class="container">

    <div class="carte">

        <img
            src="{{ produit.image }}"
            alt="{{ produit.nom }}"
        >

        <div class="infos">

            <h1>
                {{ produit.nom }}
            </h1>

            <p class="description">
                {{ produit.description }}
            </p>

            <div class="prix">

                {{ "%.2f"|format(produit.prix) }} €

            </div>

            <a
                class="retour"
                href="/"
            >
                ← Retour au catalogue
            </a>

        </div>

    </div>

</div>


</body>

</html>

"""


# ==========================================================
# ROUTES
# ==========================================================

@app.route("/")
def accueil():

    return render_template_string(
        PAGE_ACCUEIL,
        produits=produits
    )


@app.route("/produit/<int:id>")
def afficher_produit(id):

    produit = next(
        (
            p for p in produits
            if p["id"] == id
        ),
        None
    )

    if produit is None:

        abort(404)

    return render_template_string(
        PAGE_PRODUIT,
        produit=produit
    )


# ==========================================================
# QR CODE
# ==========================================================

def generer_qr_code():

    os.makedirs(
        "static/qrcode",
        exist_ok=True
    )

    qr = qrcode.QRCode(

        version=None,

        error_correction=
            qrcode.constants.ERROR_CORRECT_H,

        box_size=10,

        border=4

    )

    qr.add_data(
        PUBLIC_URL
    )

    qr.make(
        fit=True
    )

    image = qr.make_image()

    image.save(
        "static/qrcode/catalogue.png"
    )

    print()
    print("QR CODE CREE !")
    print()
    print(
        "Adresse :",
        PUBLIC_URL
    )
    print()
    print(
        "Fichier :",
        "static/qrcode/catalogue.png"
    )


# ==========================================================
# LANCEMENT
# ==========================================================

if __name__ == "__main__":

    generer_qr_code()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
