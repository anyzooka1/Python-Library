import hashlib

def sha512hash(input):
    return _hash('sha512', input)

def sha384hash(input):
    return _hash('sha384', input)

def sha256hash(input):
    return _hash('sha256', input)

def sha224hash(input):
    return _hash('sha224', input)

def sha1hash(input):
    return _hash('sha1', input)

def _hash(hashType, input):
    h = hashlib.new(hashType)
    h.update(input.encode())

    return h.hexdigest()

def main():
    print("\n--------------- HASHES TEST ---------------\n")
    print(f"SHA-512 hash of 'test': {sha512hash('test')}\n")
    print(f"SHA-384 hash of 'test': {sha384hash('test')}\n")
    print(f"SHA-256 hash of 'test': {sha256hash('test')}\n")
    print(f"SHA-224 hash of 'test': {sha224hash('test')}\n")
    print(f"SHA-1   hash of 'test': {sha1hash('test')}\n")

if __name__ == "__main__":
    main()