import hashlib


def sha256_string(input_string: str) -> str:
    encoded_string = input_string.encode('utf-8')
    hash_object = hashlib.sha256(encoded_string)
    hex_digest = hash_object.hexdigest()
    return hex_digest
