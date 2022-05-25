import pygame


#kolory z rgb:
BLACK = (0, 0, 0)
BLUE_pastel = (80, 145, 200)
GREY = (128, 128, 128)

#współrzędne początkowe:
x1 = 490
y1 = 490 #platformy
xb = 500
yb = 300 #piłki

os_x = 'lewo' #oś x
os_y = 'dół' #oś y

predkosc = 1.5 #prędkość piłki

ekran = pygame.time.Clock() #odświeżanie ekranu
okienko = pygame.display.set_mode((500, 500)) #tworzymy okienko o wymiarach 500x500
pygame.display.set_caption("Arkanoid") #okienko się nazywa Arkanoid

pygame.init()

def pileczka():

	global xb, yb
	pygame.draw.ellipse(okienko, BLUE_pastel, (xb, yb, 10, 10)) #rysujemy piłkę

def belka(x,y):

	pygame.draw.rect(okienko, GREY, (x, y, 50, 10)) #rysujemy prostokącik


def ruch_pileczki(x,y):
	#odbijamy piłeczkę
	global xb, yb, os_x, os_y
	if os_x == "lewo": #jeśli piłeczka leci w lewo to
		xb -= predkosc #współrzędna x się zmniejsza
		if xb < 10: #a jak jest mniejsza od 10 (średnica) to zawraca
			os_x = "prawo" #w prawo
	if os_y == 'dół': #jak piłeczka leci w dół
		yb += predkosc #to współrzędna y się zwiększa
	if os_y == 'góra': #jak piłeczka leci w górę
		yb -= predkosc #to współrzędna y maleje
		if yb < 10: #a jak jest mniejsza od 10
			os_y = 'dół' #to zawraca
	if os_x == "prawo": #jak piłeczka leci w prawo
		xb += predkosc #to współrzędna x się zwiększa
		if xb > 480: #a kiedy jest większa od 480
			os_x = "lewo" #to zawraca

def odbicie_pileczki():
	global x1, y1
	global xb, yb
	global x, y
	global os_x, os_y, predkosc

	if os_x == "lewo":
		if yb > 480:
			if xb >= x and  xb < x + 50: #odbicie piłeczki od platformy
				os_y = "góra"
				odbicie_pileczki = 1.5

			else: #jeśli się nie odbije:
				pygame.draw.ellipse(okienko, BLACK, (xb, yb, 10, 10)) #rysujemy piłeczkę od nowa
				pygame.display.update() #update okienka
				xb, yb = 500, 300 #współrzędne skąd ma wypaść piłka



pygame.mouse.set_visible(False) #chowamy kursor żeby nie przeszkadzał
loop=1
while loop:

	for event in pygame.event.get(): #z dokumentacji pygame:
		if event.type == pygame.QUIT: #kończy działanie programu, kiedy kliknie się krzyżyk
			loop = 0 #pętla while się kończy
	x, y = pygame.mouse.get_pos() #sterowanie myszką

	#wywołujemy te funkcje:
	ruch_pileczki(xb, yb)
	pileczka()
	belka(x,y1)
	odbicie_pileczki()
	pygame.display.update()
	okienko.fill((250, 204, 204))
	ekran.tick(120)



pygame.quit()

