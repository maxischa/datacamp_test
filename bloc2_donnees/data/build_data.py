"""Construit les jeux de donnees du bloc 2 a partir d'une source publique.

Source : UCI Machine Learning Repository, "Online Retail II"
https://archive.ics.uci.edu/dataset/502/online+retail+ii
Transactions d'un detaillant en ligne britannique, 12/2010 - 12/2011.

Produit quatre fichiers :
    ventes.csv       table de faits, propre         (~45 000 lignes)
    clients.csv      une ligne par client
    produits.csv     une ligne par produit
    ventes_sale.csv  extrait volontairement sale, pour la seance 2

Ce script n'est PAS execute par les etudiants : les CSV sont commites dans le
depot et lus par URL. Il est versionne pour que la construction reste
reproductible.

Usage :
    python build_data.py
"""

import io
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd
import urllib.request

URL_SOURCE = "https://archive.ics.uci.edu/static/public/502/online+retail+ii.zip"
FEUILLE = "Year 2010-2011"
ICI = Path(__file__).parent
CIBLE_LIGNES = 45_000
GRAINE = 42

# Les pays sont renommes en francais et sans accent : les etudiants les tapent
# dans des filtres (pays == "Norvege").
PAYS_FR = {
    "United Kingdom": "Royaume-Uni",
    "Germany": "Allemagne",
    "France": "France",
    "EIRE": "Irlande",
    "Spain": "Espagne",
    "Netherlands": "Pays-Bas",
    "Belgium": "Belgique",
    "Switzerland": "Suisse",
    "Portugal": "Portugal",
    "Australia": "Australie",
    "Norway": "Norvege",
    "Italy": "Italie",
    "Finland": "Finlande",
    "Sweden": "Suede",
    "Austria": "Autriche",
    "Denmark": "Danemark",
    "Japan": "Japon",
    "Poland": "Pologne",
    "USA": "Etats-Unis",
    "Greece": "Grece",
    "Canada": "Canada",
    "Cyprus": "Chypre",
    "Channel Islands": "Royaume-Uni",  # rattache au marche britannique
}

# Mots-cles -> categorie produit. L'ordre compte : la premiere categorie qui
# correspond gagne (ex. "CAKE CASES" doit tomber dans cuisine, pas dans jouet).
CATEGORIES = [
    ("sac", ["BAG", "HANDBAG", "SHOPPER", "PURSE", "WALLET", "SUITCASE"]),
    ("papeterie", ["CARD", "PEN ", "PENCIL", "NOTEBOOK", "PAPER", "WRAP",
                   "STICKER", "CHALK", "ENVELOPE", "JOURNAL", "GIFT TAG"]),
    ("cuisine", ["CAKE", "MUG", "TEACUP", "JAR", "BOWL", "PLATE", "CUTLERY",
                 "BAKING", "KITCHEN", "TEA ", "COFFEE", "BOTTLE", "GLASS",
                 "PANTRY", "APRON", "NAPKIN", "EGG", "SPOON", "TIN", "CUP"]),
    ("jouet", ["TOY", "GAME", "PLAY", "DOLL", "PUZZLE", "SPACEBOY", "BALLOON",
               "SKIPPING", "SOLDIER", "TEDDY", "BUNTING", "JIGSAW", "RABBIT",
               "BUNNY", "ANIMAL", "MONSTER", "HORSE", "GNOME", "DUCK"]),
    ("bijou", ["NECKLACE", "BRACELET", "EARRING", "RING", "JEWEL", "BEAD",
               "CLIPS", "HAIR", "BANGLE"]),
    ("jardin", ["GARDEN", "PLANT", "FLOWER", "BIRD", "WATERING", "SEED",
               "PARASOL", "UMBRELLA", "WINDMILL", "DAISY", "ROSE", "TREE"]),
    ("deco", ["LIGHT", "CANDLE", "HOLDER", "DECORATION", "HEART", "MIRROR",
              "FRAME", "SIGN", "HANGING", "ORNAMENT", "LANTERN", "WREATH",
              "STAR", "CUSHION", "CLOCK", "VINTAGE", "LAMP", "KNOB", "HOOK",
              "DOORMAT", "GARLAND", "BAUBLE", "SHELF", "BOX", "BASKET"]),
]


def charger_source() -> pd.DataFrame:
    """Telecharge l'archive UCI et renvoie la feuille 2010-2011."""
    cache = ICI / "_source_online_retail_ii.xlsx"
    if not cache.exists():
        print("Telechargement depuis UCI (~45 Mo)...")
        with urllib.request.urlopen(URL_SOURCE) as reponse:
            archive = zipfile.ZipFile(io.BytesIO(reponse.read()))
        nom = archive.namelist()[0]
        cache.write_bytes(archive.read(nom))
    print("Lecture du classeur...")
    return pd.read_excel(cache, sheet_name=FEUILLE)


def categoriser(libelle: str) -> str:
    """Deduit une categorie a partir du libelle produit."""
    texte = str(libelle).upper()
    for categorie, mots in CATEGORIES:
        if any(mot in texte for mot in mots):
            return categorie
    return "divers"


def _tirer_clients(bloc: pd.DataFrame, cible: int, rng) -> list:
    """Tire des clients au hasard jusqu'a atteindre ~`cible` lignes.

    On echantillonne par CLIENT et non par ligne : couper au milieu d'une
    commande donnerait des paniers incoherents et fausserait tous les
    exercices de groupby.
    """
    clients = bloc["client_id"].unique()
    rng.shuffle(clients)
    tailles = bloc.groupby("client_id").size()
    cumul, retenus = 0, []
    for client in clients:
        if cumul >= cible:
            break
        retenus.append(client)
        cumul += tailles[client]
    return retenus


def echantillonner(df: pd.DataFrame) -> pd.DataFrame:
    """Reduit a ~CIBLE_LIGNES en equilibrant marche domestique et export.

    Le jeu brut est a 91 % britannique, ce qui rend tout groupby("pays")
    ininteressant. On vise environ 40 % de Royaume-Uni : assez pour qu'il
    reste le premier marche (c'est la realite du detaillant), assez peu
    pour que les autres pays pesent quelque chose.
    """
    rng = np.random.default_rng(GRAINE)
    est_uk = df["pays"] == "Royaume-Uni"

    retenus = (
        _tirer_clients(df[est_uk], int(0.40 * CIBLE_LIGNES), rng)
        + _tirer_clients(df[~est_uk], int(0.60 * CIBLE_LIGNES), rng)
    )
    return df[df["client_id"].isin(retenus)]


def salir(df: pd.DataFrame, produits: pd.DataFrame, retours: pd.DataFrame) -> pd.DataFrame:
    """Fabrique l'extrait sale de la seance 2.

    Chaque defaut correspond a une technique enseignee :
      dates en deux formats      -> pd.to_datetime
      prix en texte              -> pd.to_numeric(errors="coerce")
      espaces et casse variables -> .str.strip() / .str.lower()
      doublons                   -> .duplicated()
      quantites negatives        -> filtrage booleen (ce sont des retours)
      quantite aberrante         -> detection par quantile
      client_id manquant         -> .isna() / .fillna()
    """
    rng = np.random.default_rng(GRAINE)
    sale = df.sample(5000, random_state=GRAINE).copy()

    # On rajoute le pays pour que le fichier soit autonome (pas de jointure
    # avant la seance 3).
    sale = sale.merge(produits[["prod_id", "categorie"]], on="prod_id", how="left")

    # 1. Deux separateurs de date melanges, tous deux au format francais
    #    jour/mois/annee. Deux pieges d'un coup : pd.to_datetime echoue sur
    #    des formats melanges (-> format="mixed"), puis lit le mois en
    #    premier (-> dayfirst=True, sinon 01/12 devient le 12 janvier).
    dates = pd.to_datetime(sale["date"])
    masque = rng.random(len(sale)) < 0.4
    sale["date"] = np.where(
        masque,
        dates.dt.strftime("%d-%m-%Y"),
        dates.dt.strftime("%d/%m/%Y"),
    )

    # 2. Prix en texte, virgule decimale, parfois suffixe " EUR".
    prix_txt = sale["prix"].map(lambda p: f"{p:.2f}".replace(".", ","))
    suffixe = rng.random(len(sale)) < 0.15
    sale["prix"] = np.where(suffixe, prix_txt + " EUR", prix_txt)

    # 3. Espaces parasites et casse incoherente sur la categorie.
    bruit = rng.integers(0, 3, len(sale))
    sale["categorie"] = np.select(
        [bruit == 0, bruit == 1],
        [" " + sale["categorie"], sale["categorie"].str.upper()],
        default=sale["categorie"],
    )

    # 4. Quelques retours (quantites negatives) repris du jeu brut, remis au
    #    meme format texte que le reste du fichier.
    ret = retours.head(120)[["date", "cmd_id", "prod_id", "qte", "prix", "client_id"]].copy()
    ret["date"] = pd.to_datetime(ret["date"]).dt.strftime("%d/%m/%Y")
    ret["prix"] = ret["prix"].map(lambda p: f"{p:.2f}".replace(".", ","))
    ret["categorie"] = "divers"
    sale = pd.concat([sale, ret])

    # 5. Une poignee de quantites aberrantes.
    idx = sale.sample(15, random_state=GRAINE).index
    sale.loc[idx, "qte"] = 99999

    # 6. Des client_id manquants.
    idx = sale.sample(400, random_state=GRAINE + 1).index
    sale.loc[idx, "client_id"] = np.nan

    # 7. Des doublons exacts.
    sale = pd.concat([sale, sale.sample(250, random_state=GRAINE + 2)])

    return sale.sample(frac=1, random_state=GRAINE).reset_index(drop=True)


def main() -> None:
    brut = charger_source()

    df = brut.rename(
        columns={
            "Invoice": "cmd_id",
            "StockCode": "prod_id",
            "Description": "libelle",
            "Quantity": "qte",
            "InvoiceDate": "date",
            "Price": "prix",
            "Customer ID": "client_id",
            "Country": "pays",
        }
    )

    df["pays"] = df["pays"].map(PAYS_FR).fillna("Autre")
    df = df.dropna(subset=["client_id", "libelle"])
    df["client_id"] = df["client_id"].astype(int)
    df["libelle"] = df["libelle"].str.strip().str.title()

    # Les retours (qte < 0) sont mis de cote : ils partiront dans le fichier
    # sale de la seance 2. La table propre reste predictible.
    retours = df[df["qte"] < 0].copy()
    df = df[(df["qte"] > 0) & (df["prix"] > 0)]

    df = echantillonner(df)
    print(f"{len(df)} lignes retenues, {df['pays'].nunique()} pays")

    # --- produits.csv : un libelle et une categorie par reference ---------
    produits = (
        df.groupby("prod_id", as_index=False)
        .agg(libelle=("libelle", "first"))
    )
    produits["categorie"] = produits["libelle"].map(categoriser)

    # --- clients.csv : pays, segment de valeur, date d'inscription -------
    df["ca_ligne"] = df["qte"] * df["prix"]
    clients = df.groupby("client_id", as_index=False).agg(
        pays=("pays", "first"),
        ca=("ca_ligne", "sum"),
        premiere=("date", "min"),
    )
    clients["segment"] = pd.qcut(
        clients["ca"], [0, 1 / 3, 2 / 3, 1.0],
        labels=["occasionnel", "standard", "premium"],
    )
    rng = np.random.default_rng(GRAINE)
    decalage = pd.to_timedelta(rng.integers(1, 400, len(clients)), unit="D")
    clients["date_insc"] = (clients["premiere"] - decalage).dt.date
    clients = clients[["client_id", "pays", "segment", "date_insc"]]

    # --- ventes.csv : la table de faits, sans pays ni libelle ------------
    # (les etudiants devront joindre en seance 3 pour les recuperer)
    ventes = df[["date", "cmd_id", "prod_id", "qte", "prix", "client_id"]].copy()
    ventes["date"] = pd.to_datetime(ventes["date"]).dt.strftime("%Y-%m-%d %H:%M")
    ventes["prix"] = ventes["prix"].round(2)
    ventes = ventes.sort_values("date").reset_index(drop=True)

    sale = salir(ventes, produits, retours)

    for nom, table in [
        ("ventes.csv", ventes),
        ("clients.csv", clients),
        ("produits.csv", produits),
        ("ventes_sale.csv", sale),
    ]:
        chemin = ICI / nom
        table.to_csv(chemin, index=False)
        taille = chemin.stat().st_size / 1e6
        print(f"{nom:<16} {len(table):>7} lignes  {taille:5.2f} Mo")


if __name__ == "__main__":
    main()
