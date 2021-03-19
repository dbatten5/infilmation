from hashlib import sha1

def generate_key(str_input):
    """Generate a sha1 from a sanitized str_input"""
    return sha1(str.encode(str_input.lower().strip())).hexdigest()
