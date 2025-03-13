# List of all available formats

| class name                   | name                   | decription                    |
| ---------------------------- | ---------------------- | ----------------------------- |
| Canton | Nom de canton | Vérifie que le nom de canton est un canton ou pseudo-canton français valide pour un Code Officiel Géographique donné |
| CodeCommuneInsee | Code commune INSEE | Vérifie que le code commune correspond bien à un code commune INSEE pour un Code Officiel Géographique donné |
| CodeFantoir | Code fantoir | Vérifie les codes fantoirs valides |
| CodePaysISO2 | Codes ISO2 Pays | Code ISO 2 de pays pour un Code Officiel Géographique donné |
| CodePaysISO3 | Codes ISO3 Pays | Code ISO 3 de pays pour un Code Officiel Géographique donné |
| CodePostal | Code postal | Vérifie que le code postal est bien un code postal français. La dernière mise à jour date du 8 février 2025 |
| CodeRegion | Code région | Vérifie qu'il s'agit d'un code région selon le Code Officiel Géographique (cog) donné |
| Commune | Nom de commune | Vérifie que le nom correspond à un nom de commune française pour un Code Officiel Géographique donné(ne vérifie pas l'accentuation, la casse, la ponctuation) |
| CoordonneesGPSFrancaises | Coordonnées GPS françaises | Check that GPS coordinates are in a bounding box approximating France (including DOM) |
| Departement | Nom de département | Vérifie les départements français, collectivités et territoires d'outre-mer valides pour un Code Officiel Géographique donné |
| NomenclatureActe | Nomenclature des actes | Document de référence dans les spécifications SCDL :<br>        http://www.moselle.gouv.fr/content/download/1107/7994/file/nomenclature.pdf<br><br>        Dans la nomenclature Actes, les valeurs avant le '/' sont :<br><br>        Commande publique<br>        Urbanisme<br>        Domaine et patrimoine<br>        Fonction publique<br>        Institutions et vie politique<br>        Libertés publiques et pouvoirs de police<br>        Finances locales<br>        Domaines de compétences par thèmes<br>        Autres domaines de compétences<br><br>        La validation devra accepter minuscules et majuscules, accents et sans accents ... |
| NumeroDepartement | Numéro du département | Vérifie que le numéro de département correspond bien à un numéro de département français, collectivités et territoires d'outre-mer pour un Code Officiel Géographique donné |
| Pays | Pays et territoires étrangers | Nom de pays et territoires étrangers pour un Code Officiel Géographique donné |
| Region | Nom de région | Vérifie les régions françaises valides pour un Code Officiel Géographique donné |
| Siren | SIREN | Check french SIREN number validity, but does not check if SIREN number exists. |
| Siret | SIRET | Check french SIRET number validity, but does not check if SIRET number exists. |

[If you want to add a new French Format, click here!](../CONTRIBUTING.md#implementing-a-new-french-format)