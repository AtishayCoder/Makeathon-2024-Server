import microbiology as m


def do_stuff(text):
    r = ortho()
    if r is None:
        r1 = m.micro(text)
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


def derma():
    pass
