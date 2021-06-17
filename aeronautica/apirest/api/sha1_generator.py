import hashlib

def get_hash(password):
    pass_to_sha1 = hashlib.new("sha1",password.encode())
    pass_to_upper_case = pass_to_sha1.hexdigest().upper()
    return pass_to_upper_case
