def wrapper(func):
    def fun(l):
        out = []
        for telnum in l:
            barenum = telnum[-10:]
            telnum = '+91 ' + barenum[:5] + ' ' + barenum[5:]
            out.append(telnum)
        func(out)
    return fun