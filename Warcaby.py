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
rows = 13
columns = 13
gracz1 = {'pionek': 1, 'krolowka': 3}
gracz2 = {'pionek': 2, 'krolowka': 4}
przycisk_reset = [(8, 6), (9, 6), (10, 6), (11, 6), (12, 6), (13, 6), (8, 7), (9, 7), (10, 7), (11, 7), (12, 7),(13, 7)]
gracz = 1

#tworze plansze
def create_board():
    board = [[empty for column in range(columns)] for row in range(rows)]
    return board

def poczatkowe_rozmieszczenie():
    #zawsze ustalam takie poczatkowe wartosci
    gracz1 = {'pionek': 1, 'krolowka': 3}
    gracz2 = {'pionek': 2, 'krolowka': 4}
    #przydzielanie elementow i lokalizacji dla bialych
    for current_row in range(5, 8, 2):
        for current_column in range(0, 8, 2):
            board[current_row][current_column] = gracz1['pionek']
            print("board1 ", board[current_row][current_column])
    for current_row in range(6, 7):
        for current_column in range(1, 8, 2):
            board[current_row][current_column] = gracz1['pionek']
            print("board2 ", board[current_row][current_column])
    #przydzielanie lokalizacji planszy dla czarnych
    for current_row in range(0, 3, 2):
        for current_column in range(1, 8, 2):
            board[current_row][current_column] = gracz2['pionek']
            print("board3 ", board[current_row][current_column])
    for current_row in range(1, 2):
        for current_column in range(0, 8, 2):
            board[current_row][current_column] = gracz2['pionek']
            print("board4 ", board[current_row][current_column])

        # przydzielanie lokalizacji planszy dla pustych
    for current_row in range(3, 5, 1):
        for current_column in range(0, 8, 1):
            board[current_row][current_column] = 0
            print("board3 ", board[current_row][current_column])

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
                circle_white_krol = pygame.draw.circle(screen, white, rect_center, radius)
                circle_white_center_krol = circle_white_krol.center
                text_surface_obj = font_obj.render('Bd', True, black)
                text_rect_obj = text_surface_obj.get_rect()
                text_rect_obj.center = circle_white_center_krol
                screen.blit(text_surface_obj, text_rect_obj)
            if board[row][column] == 4:
                circle_black_krol = pygame.draw.circle(screen, black, rect_center, radius)
                circle_black_center_krol = circle_black_krol.center
                text_surface_obj = font_obj.render('Cd', True, white)
                text_rect_obj = text_surface_obj.get_rect()
                text_rect_obj.center = circle_black_center_krol
                screen.blit(text_surface_obj, text_rect_obj)

    rect2 = pygame.draw.rect(screen, green, [600, 450, 400, 150])
    rect2_center = rect2.center #       srodek prostokatu
    text_surface_obj = font_obj.render('Reset', True, black)
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = rect2_center
    screen.blit(text_surface_obj, text_rect_obj)

def tura(gracz):
    font_obj = pygame.font.Font('freesansbold.ttf', 20)
    rect2 = pygame.draw.rect(screen, green, [600, 0, 400, 150])
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
    #print("WYBORRRRRRRR",wybor_tab)

    if wybor_tab == gracz1['pionek'] or gracz1['krolowka']:
        return True
    elif wybor_tab == gracz2['pionek'] or gracz2['krolowka']:
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
        #blokuje wyjscie za plansze
        if nowy_x == 8:
            print("Nie mozna ruszać poza plansze")
            return False
        if (nowy_y - y) == -1 and (nowy_x - x) == 1:
            print('1111',nowy_y - y)
            print('2222',nowy_x - x)
            print('1111', nowy_y)
            print('2222', nowy_x)
            return True
        elif (nowy_y - y) == -1 and (nowy_x - x) == -1:
            print(nowy_y-y)
            print(nowy_x-x)
            return True
        elif (nowy_y - y) == -2 and (nowy_x - x) == 2:
            if board[nowy_y + 1][nowy_x - 1] == gracz2['pionek'] or gracz2['krolowka']:
                board[nowy_y + 1][nowy_x - 1] = 0
                return True
            else:
                return False
        elif (nowy_y - y) == -2 and (nowy_x - x) == -2:
            if board[nowy_y + 1][nowy_x + 1] == gracz2['pionek'] or gracz2['krolowka']:
                board[nowy_y + 1][nowy_x + 1] = 0
                return True
            else:
                return False
        else:
            print("za daleko")
            return False

    #ruch gracz2
    elif board[y][x] == 2:
        #blokuje wyjscie za plansze
        if nowy_x == 8:
            print("Nie mozna ruszać poza plansze")
            return False
        if (nowy_y - y) == 1 and (nowy_x - x) == 1:
            return True
        elif (nowy_y - y) == 1 and (nowy_x - x) == -1:
            return True
        elif (nowy_y - y) == 2 and (nowy_x - x) == 2:
            if board[nowy_y - 1][nowy_x - 1] == gracz2['pionek'] or gracz2['krolowka']:
                board[nowy_y - 1][nowy_x - 1] = 0
                return True
            else:
                return False
        elif (nowy_y - y) == 2 and (nowy_x - x) == -2:
            if board[nowy_y - 1][nowy_x + 1] == gracz2['pionek'] or gracz2['krolowka']:
                board[nowy_y - 1][nowy_x + 1] = 0
                return True
            else:
                return False
        else:
            print("za daleko")
            return False

def czy_ktos_wygral(gracz, board):
    lista = []
    for row in board:
        lista.append(row.count(gracz2['pionek']))
        lista.append(row.count(gracz2['krolowka']))
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
                if board[nowy_y - 1][nowy_x + 1] == gracz2['pionek'] or gracz2['krolowka']:
                    return True
            elif board[nowy_y - 2][nowy_x - 2] == 0:
                if board[nowy_y - 1][nowy_x + 1] == gracz2['pionek'] or gracz2['krolowka']:
                    return True
        except IndexError:
            pass
    if gracz == 2:
        try:
            if board[nowy_y + 2][nowy_x + 2] == 0:
                if board[nowy_y - 1][nowy_x + 1] == gracz2['pionek'] or gracz2['krolowka']:
                    return True
            elif board[nowy_y + 2][nowy_x - 2] == 0:
                if board[nowy_y - 1][nowy_x + 1] == gracz2['pionek'] or gracz2['krolowka']:
                    return True
        except IndexError:
            pass
    if board[nowy_y][nowy_x] == gracz1['krolowka']:
        try:
            for i in range(8):
                if board[nowy_y - i][nowy_x + i] == gracz2['krolowka']:
                    if board[nowy_y - (i+1)][nowy_x + (i+1)] == 0:
                        return True
                elif board[nowy_y - i][nowy_x - i] == gracz2['krolowka']:
                    if board[nowy_y - (i+1)][nowy_x - (i+1)] == 0:
                        return True
                elif board[nowy_y + i][nowy_x + i] ==  gracz2['krolowka']:
                    if board[nowy_y + (i+1)][nowy_x + (i+1)] == 0:
                        return True
                elif board[nowy_y + i][nowy_x - i] == gracz2['krolowka']:
                    if board[nowy_y + (i+1)][nowy_x - (i+1)] == 0:
                        return True
        except IndexError:
            pass
    else:
        return False

def ogranicz(board, x, y, nowy_x, nowy_y):
    tabx = []
    taby = []
    if y < nowy_y:
        for row in range(y, nowy_y):
            taby.append(row)
    if y > nowy_y:
        for row in range(y, nowy_y, -1):
            taby.append(row)
    if x < nowy_x:
        for column in range(x, nowy_x):
            tabx.append(column)
    if x > nowy_x:
        for column in range(x, nowy_x, -1):
            tabx.append(column)
    tab = list(zip(tabx, taby))
    board_values = [board[y][x] for x, y in tab]
    if len(board_values) > 2:
        if all(i == 0 for i in board_values[1:-1]) is True:
            board[nowy_y][nowy_x] = board[y][x]
            board[y][x] = 0
            return True

    if len(board_values) == 2:
        if all(i == gracz2['pionek'] for i in board_values[1:]) is True:
            board[nowy_y][nowy_x] = board[y][x]
            board[y][x] = 0
            return True
        elif all(i == gracz2['krolowka'] for i in board_values[1:]) is True:
            board[nowy_y][nowy_x] = board[y][x]
            board[y][x] = 0
            return True
        elif all(i == 0 for i in board_values[1:]) is True:
            board[nowy_y][nowy_x] = board[y][x]
            board[y][x] = 0
            return True

    # czy krolowka tez moze ruszac sie jak pionek? Na wikipedii jest ze tak
    elif len(board_values) == 1:
        if all(i == 0 for i in board_values[1:]) is True:
            board[nowy_y][nowy_x] = board[y][x]
            board[y][x] = 0
            return True
    else:
        print("Nie mozesz kilku jednoczesnie")
        return False

def krol(gracz, board, x, y, nowy_x, nowy_y):
    if board[nowy_y][nowy_x] != 0:
        print("Ktos tutaj stoi")
        return False

    #niedozwolone ruchy
    if nowy_y == y:
        print("Nie możesz wykonac takiego ruchu")
        return False
    if nowy_x == x:
        print("Nie możesz wykonac takiego ruchu")
        return False

    if nowy_x > x and nowy_y > y:
        if (nowy_x - x) != (nowy_y - y):
            return False
    if nowy_x < x and nowy_y < y:
        if (x - nowy_x) != (y - nowy_y):
            return False
    if nowy_x < x and nowy_y > y:
        if (x - nowy_x) != (nowy_y - y):
            return False
    if nowy_x > x and nowy_y < y:
        if (nowy_x - x) != (y - nowy_y):
            return False

    #skoki
    if board[y][x] == gracz1['krolowka']:
        try:
            if board[nowy_y + 1][nowy_x - 1] == gracz2['pionek'] or gracz2['krolowka']:
                if x < nowy_x and y > nowy_y:
                    if ogranicz(board, x,y, nowy_x, nowy_y) is True:
                        board[nowy_y][nowy_x] = gracz1['krolowka']
                        board[nowy_y + 1][nowy_x - 1] = 0
                        return True
        except IndexError:
            pass
        try:  # North West Jump
            if board[nowy_y + 1][nowy_x + 1] == gracz2['pionek'] or gracz2['krolowka']:
                if x > nowy_x and y > nowy_y:
                    if ogranicz(board, x, y, nowy_x, nowy_y) is True:
                        board[nowy_y][nowy_x] = gracz1['krolowka']
                        board[nowy_y + 1][nowy_x + 1] = 0
                        return True
        except IndexError:
            pass
        try:
            if board[nowy_y - 1][nowy_x - 1] == gracz2['pionek'] or gracz2['krolowka']:
                if ogranicz(board, x, y, nowy_x, nowy_y) is True:
                    if x < nowy_x and y < nowy_y:
                        board[nowy_y][nowy_x] = gracz1['krolowka']
                        board[nowy_y - 1][nowy_x - 1] = 0
                        return True
        except IndexError:
            pass
        try:
            if board[nowy_y - 1][nowy_x + 1] == gracz2['pionek'] or gracz2['pionek']:
                if ogranicz(board, x, y, nowy_x, nowy_y) is True:
                    if x > nowy_x and y < nowy_y:
                        board[nowy_y][nowy_x] = gracz1['krolowka']
                        board[nowy_y - 1][nowy_x + 1] = 0
                        return True
        except IndexError:
            pass

def reset(x,y):#on bedzie inny
    if (x,y) in przycisk_reset:
        print("RESET")
        create_board()
        poczatkowe_rozmieszczenie()
        gracz = 1
        print("Tura gracza: ", gracz)
        tura(gracz)
        return True

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
    for event in pygame.event.get():
        pozycja_myszy = pygame.mouse.get_pos()
        pozycja_myszy_kordy = ((pozycja_myszy[0] // width), (pozycja_myszy[1] // height))
        print(pozycja_myszy_kordy)#to jest sprawdzenie dzialania ! ZAKOMENTOWAC POTEM
        #zdarzenia
        if event.type == pygame.QUIT:  #exit?
            game_over = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #if reset(pozycja_myszy_kordy) is True:
               ## poczatkowe_rozmieszczenie()
               # print("Ustawiono początkowe")
            #elif reset(pozycja_myszy_kordy) is False:
                #print("Nie ustawiono początkowego")

            pozycja = pygame.mouse.get_pos() #w pikselach
            print("kliknales ", pozycja)
            x = round(pozycja[0]//width,0) #zaokrąglam do 0 miejsa po przecinku
            y = round(pozycja[1]//height,0)
            print("kliknales ", (x,y)) #w kordach

            if reset(x,y) == True:#to nie dziala jakbym chcial, chyba musze zrobic z game()
                gracz = 1

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
                                #i czy gracz bedzie mial kolejny ruch(zasada ze po biciu drugi ruch gdy mozliwe bicie)
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
                    if board[y][x] == (gracz1['krolowka']):
                        if krol(gracz, board, x, y, nowy_x, nowy_y) is True:

                            if czy_ktos_wygral(gracz, board) is True:
                                game_over = True

                            suma_teraz = sum([sum(row) for row in board])

                            if suma_wczesniej > suma_teraz:
                                if podwojne_bicie(board, nowy_x, nowy_y) is True:
                                    pass
                                else:
                                # jesli nie to zmieniam gracza
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
                                    # i tu zrobic wypisanie na okno czyja tura
                                else:
                                    gracz = 1
                                    tura(gracz)
                                    # i tu tez zrobic!
                                gracz1, gracz2 = gracz2, gracz1

                    #zamiana na krola jak dojdzie do samego konca
                    for row in range(8):
                        for column in range(8):
                            if board[0][column] == 1:
                                board[0][column] = 3
                            elif board[7][column] == 2:
                                board[7][column] = 4
                    break
   # print("GRACZ1 = ",gracz1)
    #print("GRACZ2 = ",gracz2)
    # Limit 60fps
    clock.tick(60)
    draw_board(board)
    # Update screen with what we drew
    pygame.display.flip()
# Exit the game
pygame.quit()