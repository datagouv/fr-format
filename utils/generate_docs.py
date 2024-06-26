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


def generate_formats_documentation(all_formats):
    documentation = []
    for format in all_formats:
        doc = {
            "class_name": format.__name__,
            "name": format.metadata.name,
            "description": description_formatting(format.metadata.description),
        }
        documentation.append(doc)
    return documentation


def description_formatting(description):
    text_array = description.strip().splitlines()

    formatted_description = text_array[0] if len(text_array) > 0 else ""

    for line in text_array[1:]:
        formatted_description = formatted_description + "<br>" + line

    return formatted_description


if __name__ == "__main__":
    TEMPLATE_FILE = "formats_template.md.jinja"
    OUTPUT_FILE = "./docs/formats.md"

    documentation = generate_formats_documentation(all_validators)

    template_loader = jinja2.FileSystemLoader(searchpath="./utils/")
    template_env = jinja2.Environment(loader=template_loader, trim_blocks=True)
    template = template_env.get_template(TEMPLATE_FILE)

    output_markdown = template.render(validators=documentation)

    with open(OUTPUT_FILE, "w") as f:
        f.write(output_markdown)
