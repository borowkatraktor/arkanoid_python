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

def poziom():
    lista = []
    for n in range(5):
        wiersz = [str(choice([0, 1])) for x in range(5)]
        wiersz2 = wiersz[::-1]
        wiersz = wiersz + wiersz2
        print(wiersz)
        lista.append("".join(wiersz))
    return lista




lista = poziom()
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PINK = (255, 204, 204)
YELLOW = (255, 255, 0)
BLUE_pastel = (80, 145, 200)
GREY = (128, 128, 128)
pileczka_x = 'lewo'
pileczka_y = 'dol'
predkosc = 1



ekran = pygame.time.Clock()
okienko = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Arkanoid")
startx = 0
belka =Belka(10, 480)
pileczka = Pilka(100, 300)
cegly = tworzenie_cegiel(lista)
pygame.mouse.set_visible(False)
mysz = "stop"


wyswietl_cegly()

ruch_belka = ""
def mainloop():
    global startx, mysz, ruch_belka

    loop = 1
    while loop:

        pygame.draw.rect(okienko, (0,0,0), (belka.x, belka.y, 60, 10))
        gfxdraw.filled_circle(okienko, pileczka.x, pileczka.y, 6, (0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0



        mysz_x= pygame.mouse.get_pos()[0]

        if pygame.mouse.get_pos()[1] > 400:
            belka.y = pygame.mouse.get_pos()[1]
            pygame.mouse.set_pos(belka.x, belka.y)
        if mysz_x > 10 and mysz_x < 430:
            belka.x = mysz_x


        pileczka.update()
        belka.update()
        kolizja()
        if startx > mysz_x:
            mysz = "lewo"
        elif startx < mysz_x:
            mysz = "prawo"
        else:
            mysz = "stop"
        startx = mysz_x


        pygame.display.update()
        ekran.tick(300)


mainloop()

pygame.quit()

sys.exit()
