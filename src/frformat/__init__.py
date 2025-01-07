# flake8: noqa
from .custom_format import *  # isort:skip
from .code_rna import CodeRNA as CodeRNA
from .geo.canton import Canton as Canton
from .geo.code_commune_insee import CodeCommuneInsee as CodeCommuneInsee
from .geo.code_fantoir import CodeFantoir as CodeFantoir
from .geo.code_pays import CodePaysISO2 as CodePaysISO2
from .geo.code_pays import CodePaysISO3 as CodePaysISO3
from .geo.code_postal import CodePostal as CodePostal
from .geo.code_region import CodeRegion as CodeRegion
from .geo.commune import Commune as Commune
from .geo.coordonnees_gps_francaises import (
    CoordonneesGPSFrancaises as CoordonneesGPSFrancaises,
)
from .geo.departement import Departement as Departement
from .geo.latitude_l93 import LatitudeL93 as LatitudeL93
from .geo.longitude_l93 import LongitudeL93 as LongitudeL93
from .geo.numero_departement import NumeroDepartement as NumeroDepartement
from .geo.pays import Pays as Pays
from .geo.region import Region as Region
from .geo_format import Millesime as Millesime
from .nomenclature_acte_format import NomenclatureActe as NomenclatureActe
from .options import Options as Options
from .siren import Siren as Siren
from .siret import Siret as Siret

all_formats = [
    Canton,
    CodeCommuneInsee,
    CodeFantoir,
    CodePaysISO2,
    CodePaysISO3,
    CodePostal,
    CodeRegion,
    Commune,
    CoordonneesGPSFrancaises,
    Departement,
    NumeroDepartement,
    Pays,
    Region,
    NomenclatureActe,
    Siren,
    Siret,
]
