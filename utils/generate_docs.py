import jinja2
from validators import generate_validators_documentation

from frformat import (
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
    NomenclatureActe,
    NumeroDepartement,
    Pays,
    Region,
    Siren,
    Siret,
)

all_validators = [
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

TEMPLATE_FILE = "formats_template.md.jinja"
OUTPUT_FILE = "./docs/formats.md"

documentation = generate_validators_documentation(all_validators)

template_loader = jinja2.FileSystemLoader(searchpath="./utils/")
template_env = jinja2.Environment(loader=template_loader, trim_blocks=True)
template = template_env.get_template(TEMPLATE_FILE)

output_markdown = template.render(validators=documentation)

with open(OUTPUT_FILE, "w") as f:
    f.write(output_markdown)
