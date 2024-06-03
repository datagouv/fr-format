### Documentation: Validator list

| class name                   | name                   | decription                       |
| ---------------------------- | ---------------------- |--------------------------------- |
|  Nom de canton  |  Canton  |  Vérifie que le nom de canton est un canton ou pseudo-canton français valide   |
|  Code commune INSEE  |  CodeCommuneInsee  |  Vérifie que le code commune correspond bien à un code commune INSEE   |
|  Code fantoir  |  CodeFantoir  |  Vérifie les codes fantoirs valides   |
|  Codes ISO2 Pays  |  CodePaysISO2  |  Code ISO 2 de pays selon COG2024   |
|  Codes ISO3 Pays  |  CodePaysISO3  |  Code ISO 3 de pays selon COG2024   |
|  Code postal  |  CodePostal  |  Vérifie que le code postal est bien un code postal français   |
|  Code région  |  CodeRegion  |  Vérifie qu'il s'agit d'un code région selon le code officiel géographique 2024   |
|  Nom de commune  |  Commune  |  Vérifie que le nom correspond à un nom de commune française (ne vérifie pas l'accentuation, la casse, la ponctuation)   |
|  Coordonnées GPS françaises  |  CoordonneesGPSFrancaises  |  Check that GPS coordinates are in a bounding box approximating France (including DOM)   |
|  Nom de département  |  Departement  |  Vérifie les départements français valides (code officiel géographique 2020)   |
|  Numéro du département  |  NumeroDepartement  |  Vérifie que le numéro de département correspond bien à un numéro de département français   |
|  Pays et territoires étrangers  |  Pays  |  Nom de pays et territoires étrangers selon COG2024   |
|  Nom de région  |  Region  |  Vérifie les régions françaises valides (code officiel géographique 2020)   |
|  Nomenclature des actes  |  NomenclatureActe  |  Document de référence dans les spécifications SCDL :<br>        http://www.moselle.gouv.fr/content/download/1107/7994/file/nomenclature.pdf<br><br>        Dans la nomenclature Actes, les valeurs avant le '/' sont :<br><br>        Commande publique<br>        Urbanisme<br>        Domaine et patrimoine<br>        Fonction publique<br>        Institutions et vie politique<br>        Libertés publiques et pouvoirs de police<br>        Finances locales<br>        Domaines de compétences par thèmes<br>        Autres domaines de compétences<br><br>        La validation devra accepter minuscules et majuscules, accents et sans accents ...   |
|  SIREN  |  Siren  |  Check french SIREN number validity, but does not check if SIREN number exists.   |
|  SIRET  |  Siret  |  Check french SIRET number validity, but does not check if SIRET number exists.   |
