### Documentation: Validator list

Class Name                 Name                             Description 

Canton                      Nom de canton                    Vérifie que le nom de canton est un canton ou pseudo-canton français valide                                             
CodeCommuneInsee            Code commune INSEE               Vérifie que le code commune correspond bien à un code commune INSEE                                                     
CodeFantoir                 Code fantoir                     Vérifie les codes fantoirs valides                                                                                      
CodePaysISO2                Codes ISO2 Pays                  Code ISO 2 de pays selon COG2024                                                                                        
CodePaysISO3                Codes ISO3 Pays                  Code ISO 3 de pays selon COG2024                                                                                        
CodePostal                  Code postal                      Vérifie que le code postal est bien un code postal français                                                             
CodeRegion                  Code région                      Vérifie qu'il s'agit d'un code région selon le code officiel géographique 2024                                          
Commune                     Nom de commune                   Vérifie que le nom correspond à un nom de commune française (ne vérifie pas l'accentuation, la casse, la ponctuation)   
CoordonneesGPSFrancaises    Coordonnées GPS françaises       Check that GPS coordinates are in a bounding box approximating France (including DOM)                                   
Departement                 Nom de département               Vérifie les départements français valides (code officiel géographique 2020)                                             
NumeroDepartement           Numéro du département            Vérifie que le numéro de département correspond bien à un numéro de département français                                
Pays                        Pays et territoires étrangers    Nom de pays et territoires étrangers selon COG2024                                                                      
Region                      Nom de région                    Vérifie les régions françaises valides (code officiel géographique 2020)                                                
NomenclatureActe            Nomenclature des actes           
        Document de référence dans les spécifications SCDL :
        http://www.moselle.gouv.fr/content/download/1107/7994/file/nomenclature.pdf

        Dans la nomenclature Actes, les valeurs avant le '/' sont :

        Commande publique
        Urbanisme
        Domaine et patrimoine
        Fonction publique
        Institutions et vie politique
        Libertés publiques et pouvoirs de police
        Finances locales
        Domaines de compétences par thèmes
        Autres domaines de compétences

        La validation devra accepter minuscules et majuscules, accents et sans accents ...

Siren                       SIREN                            Check french SIREN number validity, but does not check if SIREN number exists.                                          
Siret                       SIRET                            Check french SIRET number validity, but does not check if SIRET number exists.                                          
