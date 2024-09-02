import yaml

def generate_endpoint_string(entity_name, operations):
    # Lowercase the first character of the entity name
    entity_lower = entity_name[0].lower() + entity_name[1:]

    operation_status_codes = {
        'POST': ['201'],
        'GET': ['200'],
        'DELETE': ['204'],
        'PATCH': ['200']
    }

    # Create a mapping for GET, DELETE, and PATCH with an ID
    id_operations = {
        'GET': f'GET /{entity_lower}/(id:string) -> 200',
        'DELETE': f'DELETE /{entity_lower}/(id:string) -> 204',
        'PATCH': f'PATCH /{entity_lower}/(id:string) -> 200'
    }

    results = []

    for operation, details in operations.items():
        if details.get('condition') == 'M':
            # Handle POST and GET without ID
            if operation in ['POST', 'GET']:
                results.append(f'{operation} /{entity_lower} -> {operation_status_codes[operation][0]}')
            # Handle GET, DELETE, and PATCH with ID
            if operation in id_operations:
                results.append(id_operations[operation])

    return ','.join(results)

def main():
    with open('./conformance.yaml', 'r') as file:
        data = yaml.safe_load(file)

    result_strings = []

    for entity_name, entity_details in data['conformance'].items():
        if 'operations' in entity_details:
            operations = entity_details['operations']
            result_string = generate_endpoint_string(entity_name, operations)
            if result_string:
                result_strings.append(result_string)

    # Combine all result strings for different entities
    final_output = ','.join(result_strings)

    # Print the final result
    print(final_output)

if __name__ == "__main__":
    main()