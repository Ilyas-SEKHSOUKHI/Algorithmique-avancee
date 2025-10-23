def aplatir(L):
    AP=[]
    for l in L:
        if not isinstance (l.list):
            AP.append(l)
        else:
            return aplatir(l)
    return AP
