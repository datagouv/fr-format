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


def text_formatting(text):
    new_text = text.strip()
    formatted_description = ""
    text_array = new_text.splitlines()

    if len(text_array) == 1:
        formatted_description = text_array[0]
        return formatted_description

    for line in text_array:
        if line is text_array[0] and line != "":
            formatted_description = line
        else:
            formatted_description = formatted_description + "<br>" + line

    return formatted_description


def generate_validators_documentation(all_validators):
    documentation = []
    for validator in all_validators:
        doc = {
            "class_name": validator.__name__,
            "name": validator.metadata.name,
            "description": text_formatting(validator.metadata.description),
        }
        documentation.append(doc)
    return documentation


if __name__ == "__main__":
    TEMPLATE_FILE = "formats_template.md.jinja"
    OUTPUT_FILE = "./docs/formats.md"

    documentation = generate_validators_documentation(all_validators)

    template_loader = jinja2.FileSystemLoader(searchpath="./utils/")
    template_env = jinja2.Environment(loader=template_loader, trim_blocks=True)
    template = template_env.get_template(TEMPLATE_FILE)

    output_markdown = template.render(validators=documentation)

    with open(OUTPUT_FILE, "w") as f:
        f.write(output_markdown)
