"""Module for general utils"""

from hashlib import sha1

def generate_key(str_input):
    """Generate a sha1 from the str_input to be stored as the Film key"""
    return sha1(str.encode(str_input.lower().strip())).hexdigest()
