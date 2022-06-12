def tworzenie_cegiel(lista):

    cegly = []
    h = 30
    w = 0
    for line in lista:
        for cegla in line:
            if cegla == "1":
                cegly.append(Cegla(50 + w * 51, h))
            w += 1
            if w == 8:
                w = 0
                h += 21
    return cegly


def wyswietl_cegly():
    for cegla in cegly:
        cegla.update()
