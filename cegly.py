def odbicie():
    global pileczka_x, predkosc, predkosc
    pileczka_x = "prawo" if pileczka_x == "lewo" else "prawo"



def kolizja():
    global pileczka, belka, pileczka_y, pileczka_x, vely, predkosc, mysz, cegly
    global loop
    if pileczka.rect.colliderect(belka):

        pileczka_y = "gora"


    for n, cegla in enumerate(cegly):
        if pileczka.rect.colliderect(cegla):
            pygame.draw.rect(okienko, (0,0,0), (cegla.x, cegla.y, 50, 20))


            if pileczka_y == "gora":

                if pileczka.y == (cegla.y + 20 - predkosc) :
                    pileczka_y = "dol"

                else:
                    if pileczka_x == "lewo":
                        pileczka_x = "prawo"
                    else:
                        pileczka_x = "lewo"
            elif pileczka_y == "dol":
                if pileczka.y <= cegla.y - 1:
                    pileczka_y = "gora"
                else:
                    if pileczka_x == "lewo":
                        pileczka_x = "prawo"
                    else:
                        pileczka_x = "lewo"
            cegly.pop(n)
            if cegly == []:

                okienko.fill((0,0,0))
                pileczka.y = 300
                pileczka.x = 100
                cegly = tworzenie_cegiel(poziom())
                wyswietl_cegly()


    if pileczka.y > 510:
        pileczka.x, pileczka.y = 500, 300

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


