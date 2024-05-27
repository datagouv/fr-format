def generate_validators_documentation(all_validators):
    documentation = []
    for validator in all_validators:
        doc = {
            'class_name': validator,
            'name': validator.name(),
            'description': validator.description()
        }
        documentation.append(doc)
    return documentation
