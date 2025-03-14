REGIONS_REPETES = frozenset(
    {
        "Guadeloupe",
        "Martinique",
        "Guyane",
        "La Réunion",
        "Mayotte",
        "Île-de-France",
        "Pays de la Loire",
        "Bretagne",
        "Provence-Alpes-Côte d'Azur",
        "Corse",
    }
)
REGIONS_COG_2015 = REGIONS_REPETES.union(
    frozenset(
        {
            "Champagne-Ardenne",
            "Picardie",
            "Haute-Normandie",
            "Centre",
            "Basse-Normandie",
            "Bourgogne",
            "Nord-Pas-de-Calais",
            "Lorraine",
            "Alsace",
            "Franche-Comté",
            "Poitou-Charentes",
            "Aquitaine",
            "Midi-Pyrénées",
            "Limousin",
            "Rhône-Alpes",
            "Auvergne",
            "Languedoc-Roussillon",
        }
    )
)
REGIONS_COG_2016 = REGIONS_REPETES.union(
    frozenset(
        {
            "Centre-Val de Loire",
            "Bourgogne-Franche-Comté",
            "Normandie",
            "Nord-Pas-de-Calais-Picardie",
            "Alsace-Champagne-Ardenne-Lorraine",
            "Aquitaine-Limousin-Poitou-Charentes",
            "Languedoc-Roussillon-Midi-Pyrénées",
            "Auvergne-Rhône-Alpes",
        }
    )
)
REGIONS_SINCE_2017 = REGIONS_REPETES.union(
    frozenset(
        {
            "Centre-Val de Loire",
            "Bourgogne-Franche-Comté",
            "Normandie",
            "Hauts-de-France",
            "Grand Est",
            "Nouvelle-Aquitaine",
            "Occitanie",
            "Auvergne-Rhône-Alpes",
        }
    )
)
