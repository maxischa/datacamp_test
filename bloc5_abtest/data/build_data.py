"""Construit les jeux de donnees du bloc 5 a partir de deux sources publiques.

    hillstrom.csv          une ligne par client   (64 000 lignes)
    online_classroom.csv   un etudiant par ligne  (   323 lignes)

`hillstrom.csv` est la vraie experience du MineThatData E-Mail Analytics
Challenge : 64 000 clients d'un site de e-commerce repartis AU HASARD en trois
bras (pas d'email / email produits hommes / email produits femmes), avec leurs
caracteristiques pre-traitement et leurs achats des deux semaines suivantes.
C'est une experience randomisee reelle, pas une simulation : c'est ce qui
permet a l'etude de cas de parler d'effet causal sans tricher.

`online_classroom.csv` est le petit ECR « cours en ligne » du Causal Inference
for the Brave and True (MIT). Il sert au cours a montrer un deuxieme mecanisme
d'attribution aleatoire, et surtout le test d'equilibre sur un echantillon
assez petit pour qu'une variable pre-traitement s'ecarte visiblement — ce que
64 000 lignes ne montrent jamais.

Les colonnes des deux fichiers sont reprises TELLES QUELLES de leur source.
Deux consequences a connaitre :

  - `history_segment` fait 15 caracteres et depasse donc la limite de 10 de la
    regle 5 du CLAUDE.md. La violation est inerte : aucun exercice ne touche
    cette colonne, elle n'apparait que dans le dictionnaire des variables que
    l'etudiant LIT. La renommer couperait le lien avec le jeu public, que les
    etudiants curieux retrouveront sur minethatdata.com ;
  - les valeurs de `segment` ("No E-Mail", "Mens E-Mail", "Womens E-Mail")
    sont cheres a taper sur tablette. La feuille d'exercices les declare une
    fois en constantes AUCUN / HOMME / FEMME, dans sa cellule de preparation.

Aucun reequilibrage, aucun echantillonnage : sur une experience randomisee,
toucher aux proportions detruirait precisement ce qu'on veut enseigner.

Ce script n'est PAS execute par les etudiants : les CSV sont commites dans le
depot et lus par URL. Il est versionne pour que la construction reste
reproductible.

Usage :
    python bloc5_abtest/data/build_data.py
"""

import urllib.request
from pathlib import Path

import pandas as pd

ICI = Path(__file__).parent

# Miroir S3 (gzip, ~430 Ko) puis la source d'origine de Kevin Hillstrom.
# Les deux servent le meme fichier ; le miroir est simplement plus rapide.
HILLSTROM = [
    "https://hillstorm1.s3.us-east-2.amazonaws.com/hillstorm_no_indices.csv.gz",
    "http://www.minethatdata.com/Kevin_Hillstrom_MineThatData"
    "_E-MailAnalytics_DataMiningChallenge_2008.03.csv",
]

CLASSE = (
    "https://raw.githubusercontent.com/matheusfacure/python-causality-handbook"
    "/master/causal-inference-for-the-brave-and-true/data/online_classroom.csv"
)

PLAFOND_MO = 5.0


def telecharger(urls, destination: Path) -> Path:
    """Recupere la premiere URL qui repond, et garde la copie brute.

    Le fichier `_source_*` est dans le .gitignore : on ne commite jamais la
    source, seulement le CSV qu'on en derive. Le garder sur disque evite de
    retelecharger a chaque relance du script.
    """
    if destination.exists():
        print(f"{destination.name:<28} deja present")
        return destination
    for url in urls if isinstance(urls, list) else [urls]:
        try:
            urllib.request.urlretrieve(url, destination)
            print(f"{destination.name:<28} telecharge depuis {url[:60]}...")
            return destination
        except Exception as erreur:            # noqa: BLE001 - on essaie la suivante
            print(f"  echec sur {url[:60]}... : {erreur}")
    raise SystemExit("aucune source n'a repondu")


def ecrire(table: pd.DataFrame, nom: str) -> None:
    chemin = ICI / nom
    table.to_csv(chemin, index=False)
    taille = chemin.stat().st_size / 1e6
    print(f"{nom:<28} {len(table):>6} lignes  {taille:5.2f} Mo")
    assert taille < PLAFOND_MO, f"{nom} depasse {PLAFOND_MO} Mo"


def main() -> None:
    source = telecharger(HILLSTROM, ICI / "_source_hillstrom.csv.gz")
    emails = pd.read_csv(source)
    ecrire(emails, "hillstrom.csv")

    classe = pd.read_csv(telecharger(CLASSE, ICI / "_source_online_classroom.csv"))
    ecrire(classe, "online_classroom.csv")

    controler(emails, classe)


def controler(emails: pd.DataFrame, classe: pd.DataFrame) -> None:
    """Verrouille les asperites pedagogiques du bloc.

    Toute l'etude de cas est construite sur ces chiffres : ils sont recopies
    dans les `verifier(...)` de la partie 1 et dans les commentaires des
    solutions. Si la source change un jour, l'enonce devient faux en silence —
    d'ou ces controles, qui font echouer la construction plutot que la seance.
    """
    assert len(emails) == 64000, "le fichier Hillstrom n'a plus 64 000 lignes"
    assert emails.isna().sum().sum() == 0, "des valeurs manquantes sont apparues"

    bras = emails["segment"].value_counts()
    assert set(bras.index) == {"No E-Mail", "Mens E-Mail", "Womens E-Mail"}
    assert bras.min() > 21000, "un bras de l'experience a fondu"

    depense = emails.groupby("segment")["spend"].mean()
    assert abs(depense["Mens E-Mail"] - 1.4226) < 1e-3
    assert abs(depense["No E-Mail"] - 0.6528) < 1e-3

    # L'equilibre pre-traitement est LE point du cours : les trois bras doivent
    # etre indiscernables sur `history`. Si cet ecart se creusait, la partie 3
    # de l'etude de cas ne demontrerait plus rien.
    passe = emails.groupby("segment")["history"].mean()
    assert passe.max() - passe.min() < 5, "les bras ne sont plus equilibres"

    # A l'inverse, le petit ECR « cours en ligne » doit garder son desequilibre
    # visible sur `black` : c'est lui qui montre qu'en petit echantillon, le
    # hasard laisse des ecarts meme sous randomisation parfaite.
    format_ligne = classe["format_ol"].astype(bool)
    ecart = abs(classe.loc[format_ligne, "black"].mean()
                - classe.loc[~format_ligne, "black"].mean())
    assert ecart > 0.02, "le desequilibre pedagogique sur `black` a disparu"

    print("\ncontroles pedagogiques : OK")
    print(f"  depense moyenne par bras : {depense.round(3).to_dict()}")
    print(f"  ecart max sur `history`  : {passe.max() - passe.min():.2f} $")
    print(f"  ecart sur `black` (ECR)  : {ecart:.3f}")


if __name__ == "__main__":
    main()
