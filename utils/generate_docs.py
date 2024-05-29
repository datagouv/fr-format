import jinja2

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
    NumeroDepartement,
    Pays,
    Region,
    NomenclatureActe,
    Siren,
    Siret
)
from validators import generate_validators_documentation

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
    Siret
]
documentation = generate_validators_documentation(all_validators)

template_loader = jinja2.FileSystemLoader(searchpath="./utils/")
template_env = jinja2.Environment(loader=template_loader, trim_blocks=True)
template_file = "validator_template.md.jinja"
template = template_env.get_template(template_file)

output_markdown = template.render(validators=documentation)

with open("./docs/output_validators.md", "w") as f:
    f.write(output_markdown)
