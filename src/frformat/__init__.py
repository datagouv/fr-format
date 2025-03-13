# flake8: noqa
from .custom_format import *  # isort:skip
from .formats.canton import Canton as Canton
from .formats.code_commune_insee import CodeCommuneInsee as CodeCommuneInsee
from .formats.code_fantoir import CodeFantoir as CodeFantoir
from .formats.code_pays import CodePaysISO2 as CodePaysISO2
from .formats.code_pays import CodePaysISO3 as CodePaysISO3
from .formats.code_postal import CodePostal as CodePostal
from .formats.code_region import CodeRegion as CodeRegion
from .formats.code_rna import CodeRNA as CodeRNA
from .formats.commune import Commune as Commune
from .formats.coordonnees_gps_francaises import (
    CoordonneesGPSFrancaises as CoordonneesGPSFrancaises,
)
from .formats.departement import Departement as Departement
from .formats.latitude_l93 import LatitudeL93 as LatitudeL93
from .formats.longitude_l93 import LongitudeL93 as LongitudeL93
from .formats.nomenclature_acte_format import NomenclatureActe as NomenclatureActe
from .formats.numero_departement import NumeroDepartement as NumeroDepartement
from .formats.pays import Pays as Pays
from .formats.region import Region as Region
from .formats.siren import Siren as Siren
from .formats.siret import Siret as Siret
from .options import Options as Options
from .versions import Millesime as Millesime

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
