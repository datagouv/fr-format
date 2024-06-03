def text_formatting(text):
    new_text = text.strip()
    formatted_description = ""
    text_array = new_text.splitlines()
        
    if len(text_array) == 1:
        formatted_description = text_array[0]
        return formatted_description
        
    for line in text_array:
        if line is text_array[0] and line != '':
            formatted_description =line
        else:
            formatted_description = formatted_description+"<br>"+line
        
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
