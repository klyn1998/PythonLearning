import hashlib


def encrypt_password(password, x='21fsadv'):
    h = hashlib.sha256()
    h.update(password.encode('utf8'))
    h.update(x.encode('utf8'))
    return h.hexdigest()
