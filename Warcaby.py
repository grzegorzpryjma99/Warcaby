import time
import pygame

# Definiuje
brick = (156,102,31)
burlywood1 = (255,211,155)
black = (0, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
dark_red = (139 , 0, 0)
grey = (128, 128, 128)
gold = (255, 215, 0)
empty = 0
rows = 8
columns = 8
gracz1 = {'pionek': 1, 'krolowka': 3}
gracz2 = {'pionek': 2, 'krolowka': 4}



#tworze plansze
def create_board():
    board = [[empty for column in range(columns)] for row in range(rows)]
    return board

def poczatkowe_rozmieszczenie():
    #przydzielanie elementow i lokalizacji dla bialych
    for current_row in range(5, 8, 2):
        for current_column in range(0, 8, 2):
            board[current_row][current_column] = gracz1['pionek']
    for current_row in range(6, 7):
        for current_column in range(1, 8, 2):
            board[current_row][current_column] = gracz1['pionek']

    #przydzielanie lokalizacji planszy dla czarnych
    for current_row in range(0, 3, 2):
        for current_column in range(1, 8, 2):
            board[current_row][current_column] = gracz2['pionek']
    for current_row in range(1, 2):
        for current_column in range(0, 8, 2):
            board[current_row][current_column] = gracz2['pionek']


def draw_board(board):
    font_obj = pygame.font.Font('freesansbold.ttf', 20)
    for row in range(8):
        for column in range(8):
        #wypelniam siatke jako ciemny lub jasny
            if (row + column) % 2 == 0:
                color = burlywood1
            else:
                color = brick
            rect = pygame.draw.rect(screen, color, [width * column, height * row, width, height])
            rect_center = rect.center
            if board[row][column] == 1:
                circle_white = pygame.draw.circle(screen, white, rect_center, radius)
                circle_white_center = circle_white.center
                text_surface_obj = font_obj.render('B', True, black)
                text_rect_obj = text_surface_obj.get_rect()
                text_rect_obj.center = circle_white_center
                screen.blit(text_surface_obj, text_rect_obj)
            if board[row][column] == 2:
                circle_black = pygame.draw.circle(screen, black, rect_center, radius)
                circle_black_center = circle_black.center
                text_surface_obj = font_obj.render('C', True, white)
                text_rect_obj = text_surface_obj.get_rect()
                text_rect_obj.center = circle_black_center
                screen.blit(text_surface_obj, text_rect_obj)
            #krolowki
        #ZROBIC TU JESZCZE DLA KROLOWEK TEKST Cd Bd
            if board[row][column] == 3:
                pygame.draw.circle(screen, white, rect_center, radius)
                pygame.draw.circle(screen, gold, rect_center, radius, granica)
            if board[row][column] == 4:
                pygame.draw.circle(screen, gold, rect_center, radius, granica)
    """
    rect2 = pygame.draw.rect(screen, green, [650, 50, 300, 100])
    rect2_center = rect2.center #       srodek prostokatu(na tekst o turze)
    text_surface_obj = font_obj.render('Hello World!', True, black)     #tu bedzie tekst z tura
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = rect2_center
    screen.blit(text_surface_obj, text_rect_obj)
    """

def tura(gracz):
    font_obj = pygame.font.Font('freesansbold.ttf', 20)
    rect2 = pygame.draw.rect(screen, green, [650, 50, 300, 100])
    rect2_center = rect2.center  # srodek prostokatu(na tekst o turze)
    if gracz == 1:
        tekst = "Tura Gracza 1 "
    if gracz == 2:
        tekst = "Tura Gracza 2"
    text_surface_obj = font_obj.render(tekst, True, black)     #tu bedzie tekst z tura
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = rect2_center
    screen.blit(text_surface_obj, text_rect_obj)

def wybor(board, gracz, x, y): #Gracz nie moze wybrac pustego pola lub nie swojego pionka
    wybor_tab = board[y][x]
    if wybor_tab == gracz1['pionek']: # TU BEDZIE JESZCZE OR i dla krolowki
        return True
    elif wybor_tab == gracz2['pionek']: #tu tez
        print("To nie twoje")
        return False
    else:
        print("Tu nawet nie ma pionka")
        return False


def ruch(gracz, board, x, y, nowy_x, nowy_y):
    #Czy cos tam jest?
    if board[nowy_y][nowy_x] != 0:
        print("Cos tu jest mordo")
        return False
    ##Obsluga bicia pionkow (mozliwosci bicia)
    # Ruch gracz1
    if board[y][x] == 1:
        if (nowy_y - y) == -1 and (nowy_x - x) == 1:
            return True
        elif (nowy_y - y) == -1 and (nowy_x - x) == -1:
            return True
        elif (nowy_y - y) == -2 and (nowy_x - x) == 2:
            if board[nowy_y + 1][nowy_x - 1] == gracz2['pionek']:
                board[nowy_y + 1][nowy_x - 1] = 0
                return True
            else:
                return False
        elif (nowy_y - y) == -2 and (nowy_x - x) == -2:
            if board[nowy_y + 1][nowy_x + 1] == gracz2['pionek']:
                board[nowy_y + 1][nowy_x + 1] = 0
                return True
            else:
                return False

    #ruch gracz2
    elif board[y][x] == 2:
        if (nowy_y - y) == 1 and (nowy_x - x) == 1:
            return True
        elif (nowy_y - y) == 1 and (nowy_x - x) == -1:
            return True
        elif (nowy_y - y) == 2 and (nowy_x - x) == 2:
            if board[nowy_y - 1][nowy_x - 1] == gracz2['pionek']:
                board[nowy_y - 1][nowy_x - 1] = 0
                return True
            else:
                return False
        elif (nowy_y - y) == 2 and (nowy_x - x) == -2:
            if board[nowy_y - 1][nowy_x + 1] == gracz2['pionek']:
                board[nowy_y - 1][nowy_x + 1] = 0
                return True
            else:
                return False

def czy_ktos_wygral(gracz, board):
    lista = []
    for row in board:
        lista.append(row.count(gracz2['pionek']))
        #Jeszcze dla krolowek zrobiccccc
    if sum(lista) == 0:
        print("Wygrał gracz: ", gracz)
        return True

def podwojne_bicie(board, nowy_x, nowy_y):
    #w ktora strone mozna bic(mozliwe ruchy)
    if gracz == 1:
        #dodac krolowki!!!!!!!!!!!!!!!!!!!!
        try:
            if board[nowy_y - 2][nowy_x + 2] == 0:
                if board[nowy_y - 1][nowy_x + 1] == gracz2['pionek']:
                    return True
            elif board[nowy_y - 2][nowy_x - 2] == 0:
                if board[nowy_y - 1][nowy_x + 1] == gracz2['pionek']:
                    return True
        except IndexError:
            pass
    if gracz == 2:
        try:
            if board[nowy_y + 2][nowy_x + 2] == 0:
                if board[nowy_y - 1][nowy_x + 1] == gracz2['pionek']:
                    return True
            elif board[nowy_y + 2][nowy_x - 2] == 0:
                if board[nowy_y - 1][nowy_x + 1] == gracz2['pionek']:
                    return True
        except IndexError:
            pass
   #zrobic jeszcze z krolem [if krolowka....]
    else:
        return False

#Ustalam ze gra sie nie skonczyla
game_over = False

board = create_board()
poczatkowe_rozmieszczenie()

# Inicjuje pygame
pygame.init()
# Rozdzielczosc
window_size = [1000, 600]
screen = pygame.display.set_mode(window_size)
#tytul
pygame.display.set_caption("Warcaby")
#fps
clock = pygame.time.Clock()
#Ustawia rozmiary komórek tablicy
window_width = 600
window_height = 600
total_rows = 8
total_columns = 8
width = (window_width // total_columns)#75
height = (window_height // total_rows)#75

#Ustaw promień i ramkę graniczną każdego elementu szachownicy
radius = (window_width // 20)#30
granica = (window_width // 200)#3

#Domyslnie bedzie zaczynal gracz 1 (bialy)
gracz = 1

print("Tura gracza: " , gracz)
tura(gracz)

#Gra
while game_over == False:
    #print("NUUUUUUUUUUUUEEEEMR", numer)
   # tura(gracz)
    #print("cos")
    #umozliwiam zamkniecie okna i tworze pozycje myszy
    for event in pygame.event.get():  # User did something
        pozycja_myszy = pygame.mouse.get_pos()
        pozycja_myszy_kordy = ((pozycja_myszy[0] // width), (pozycja_myszy[1] // height))
        print(pozycja_myszy_kordy)#to jest sprawdzenie dzialania ! ZAKOMENTOWAC POTEM
        #zdarzenia
        if event.type == pygame.QUIT:  #exit?
            game_over = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pozycja = pygame.mouse.get_pos() #w pikselach
            print("kliknales ", pozycja)
            x = round(pozycja[0]//width,0) #zaokrąglam do 0 miejsa po przecinku
            y = round(pozycja[1]//height,0)
            print("kliknales ", (x,y)) #w kordach

            suma_wczesniej = sum([sum(row) for row in board])

            #Tu sobie sprawdzam czy wybrany pionek jest gracza ktory ma ture w danym monencie
            if wybor(board, gracz, x, y) == True:
                pass
            else:
                continue

            #jesli tak to ustalam nowa pozycja za pomoca przeciagniecia
            while True:
                ###TO NIE DZIALA TAK JAKBYM CHCIAL!!!!!!!!!(DODALEM // ZAMIAST /, POWINNO BYC OK?)
                event = pygame.event.wait()
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    nowa_pozycja = pygame.mouse.get_pos()
                    print("pos",nowa_pozycja)
                    nowy_x = round((nowa_pozycja[0] // width),0)
                    nowy_y = round((nowa_pozycja[1] // height),0)
                    print("nowa pozycja ", (nowy_x, nowy_y))  # w kordach

                    print(gracz)

                    if board[y][x] == gracz1['pionek']:
                        if ruch(gracz, board, x, y, nowy_x, nowy_y) is True:
                            board[nowy_y][nowy_x] = gracz1['pionek']
                            board[y][x] = 0
                           # tura(gracz)

                            if czy_ktos_wygral(gracz, board) is True:
                                game_over = True

                            suma_teraz = sum([sum(row) for row in board])

                            #zmiana gracza
                            
                            #tu sobie sprawdzam czy suma pionkow ulegla zmianie i dokonuje zmiany lub nie
                            if suma_wczesniej > suma_teraz:
                                #i czy gracz bedzie mial kolejny ruch(zasada ze po biciu drugi ruch)
                                if podwojne_bicie(board,nowy_x,nowy_y) is True:
                                    pass
                                else:
                                    #jesli nie to zmieniam gracza
                                    if gracz == 1:
                                        gracz = 2
                                        tura(gracz)
                                        # i tu zrobic wypisanie na okno czyja tura
                                    else:
                                        gracz = 1
                                        tura(gracz)
                                        # i tu tez zrobic!
                                    gracz1, gracz2 = gracz2, gracz1
                            else:
                                if gracz == 1:
                                    gracz = 2
                                    tura(gracz)
                                    #i tu zrobic wypisanie na okno czyja tura
                                else:
                                    gracz = 1
                                    tura(gracz)
                                    #i tu tez zrobic!
                                gracz1, gracz2 = gracz2, gracz1
                    break

    # Limit 60fps
    clock.tick(60)
    draw_board(board)
    # Update screen with what we drew
    pygame.display.flip()
# Exit the game
pygame.quit()