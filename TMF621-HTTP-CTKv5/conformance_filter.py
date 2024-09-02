import yaml
import sys
import re

def load_openapi_spec(filepath):
    with open(filepath, 'r') as file:
        return yaml.safe_load(file)

def get_status_code(openapi_spec, method, path):
    # Convert method to lowercase
    method = method.lower()
    path = re.sub(r'\(id:string\)', '{id}', path)
    
    # Check if the path and method exist in the spec
    if path in openapi_spec['paths'] and method in openapi_spec['paths'][path]:
        responses = openapi_spec['paths'][path][method]['responses']
        # Filter 2xx status codes, excluding 202
        status_codes = [int(code) for code in responses if code.startswith('2') and code != '202']

        if not status_codes:
            return None

        if len(status_codes) > 1:
            print(f"Multiple 2xx status codes found for {method.upper()} {path}: {status_codes}. Exiting.")
            sys.exit(1)

        # Return the last remaining status code
        return status_codes[-1]

    return None

def generate_endpoint_string(entity_name, operations, openapi_spec):
    # Lowercase the first character of the entity name
    entity_lower = entity_name[0].lower() + entity_name[1:]

    results = []

    for operation, details in operations.items():
        if details.get('condition') == 'M':
            if operation == 'POST':
                path = f'/{entity_lower}'
                status_code = get_status_code(openapi_spec, operation, path)
                if status_code:
                    results.append(f'{operation} {path} -> {status_code}')

            if operation == 'GET':
                path = f'/{entity_lower}'
                status_code = get_status_code(openapi_spec, operation, path)
                if status_code:
                    results.append(f'{operation} {path} -> {status_code}')

                path_with_id = f'/{entity_lower}/(id:string)'
                status_code = get_status_code(openapi_spec, operation, path_with_id)
                if status_code:
                    results.append(f'{operation} {path_with_id} -> {status_code}')

            if operation == 'DELETE':
                path_with_id = f'/{entity_lower}/(id:string)'
                status_code = get_status_code(openapi_spec, operation, path_with_id)
                if status_code:
                    results.append(f'{operation} {path_with_id} -> {status_code}')

            if operation == 'PATCH':
                path_with_id = f'/{entity_lower}/(id:string)'
                status_code = get_status_code(openapi_spec, operation, path_with_id)
                if status_code:
                    results.append(f'{operation} {path_with_id} -> {status_code}')

    return ','.join(results)

def main(conformance_file, openapi_file):
    with open(conformance_file, 'r') as file:
        data = yaml.safe_load(file)

    openapi_spec = load_openapi_spec(openapi_file)

    result_strings = []

    for entity_name, entity_details in data['conformance'].items():
        if 'operations' in entity_details:
            operations = entity_details['operations']
            result_string = generate_endpoint_string(entity_name, operations, openapi_spec)
            if result_string:
                result_strings.append(result_string)

    # Combine all result strings for different entities
    final_output = ','.join(result_strings)

    # Print the final result
    print(final_output)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <conformance.yaml> <openapi.yaml>")
        sys.exit(1)
    
    conformance_file = sys.argv[1]
    openapi_file = sys.argv[2]
    main(conformance_file, openapi_file)