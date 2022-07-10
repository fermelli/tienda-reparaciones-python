from random import random
from hashlib import sha1


def generarId():
    return random().hex()[5:][:-3]


def encriptar(cadena):
    return sha1(cadena.encode('utf-8')).hexdigest()
