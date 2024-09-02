import re

def extractIdentifiers(file):
    identifiers = set()

    with open(file, 'r') as f:
        for l in f:
            foundIdentifiers = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', l)
            identifiers.update(foundIdentifiers)

    return identifiers

def main():
    file = 'hello.c'
    uniqueIdentifiers = extractIdentifiers(file)

    print("Unique Identifiers:")
    for i in sorted(uniqueIdentifiers):
        print(i)

if __name__ == '__main__':
    main()
