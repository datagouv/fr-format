from frformat import Canton, CodeFantoir, CodeRegion, CodeCommuneInsee, CodePaysISO2, CodePaysISO3, CodePostal, Commune, CoordonneesGPSFrancaises
import jinja2
from validators import generate_validators_documentation


all_validators = [CodeFantoir, CodeRegion, Canton, CodeCommuneInsee, CodePaysISO2, CodePaysISO3, CodePostal, Commune, CoordonneesGPSFrancaises]
documentation = generate_validators_documentation(all_validators)

template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env = jinja2.Environment(loader=template_loader)
template_file = "validator_template.md.jinja"
template = template_env.get_template(template_file)

output_markdown = template.render(validators=documentation)

with open("out_put_validator_template.md", "w") as f:
    f.write(output_markdown)
