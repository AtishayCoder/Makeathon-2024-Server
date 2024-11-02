from nltk import *
from main import process_recording


def do_stuff():
    r = ortho()
    if r is None:
        r1 = micro()
        if r1 is None:
            r2 = derma()
            if r2 is None:
                return "Unsupported"
            else:
                return str(r2)
        else:
            return str(r1)
    else:
        return r


def ortho():
    pass


def micro():
    pass


def derma():
    pass
