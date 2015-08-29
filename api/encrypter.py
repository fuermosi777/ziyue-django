from hashids import Hashids

# DON'T CHANGE THIS
hashids = Hashids(salt='Ziyue is an IT reading app', min_length=7)

def encode(id):
    return hashids.encode(id)

def decode(code):
    return hashids.decode(code)[0]