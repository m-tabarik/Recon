#removes subdomains in bulk that are not in scope

import sys

def read_subdomains(file_path):
    with open(file_path, 'r') as file:             
        return [line.strip() for line in file]

def remove_subdomains(subdomains, subdomains_to_remove):
    return [subdomain for subdomain in subdomains if subdomain not in subdomains_to_remove]
 
def write_subdomains(file_path, subdomains):
    with open(file_path, 'w') as file:
        file.write('\n'.join(subdomains))

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <file_path>")
        sys.exit(1)

    # File path of the original file containing subdomains
    original_file_path = sys.argv[1]

    # Subdomains to remove
    subdomains_to_remove = [
        'abc.abc.com',
        'adb.dsaf.com'
    ]

    # Read subdomains from the original file
    original_subdomains = read_subdomains(original_file_path)

    # Remove specified subdomains
    remaining_subdomains = remove_subdomains(original_subdomains, subdomains_to_remove)

    # Write the remaining subdomains back to the original file
    write_subdomains(original_file_path, remaining_subdomains)

if __name__ == "__main__":
    main()
                
