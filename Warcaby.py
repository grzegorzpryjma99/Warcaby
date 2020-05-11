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
przyjaciel = {'pionek': 1, 'krolowka': 3}
wrog = {'pionek': 2, 'krolowka': 4}

#tworze plansze
def create_board():
    board = [[empty for column in range(columns)] for row in range(rows)]
    return board

def place_starting_pieces():
    #przydzielanie elementow i lokalizacji dla bialych
    for current_row in range(5, 8, 2):
        for current_column in range(0, 8, 2):
            board[current_row][current_column] = przyjaciel['pionek']
    for current_row in range(6, 7):
        for current_column in range(1, 8, 2):
            board[current_row][current_column] = przyjaciel['pionek']

    #przydzielanie lokalizacji planszy dla czarnych
    for current_row in range(0, 3, 2):
        for current_column in range(1, 8, 2):
            board[current_row][current_column] = wrog['pionek']
    for current_row in range(1, 2):
        for current_column in range(0, 8, 2):
            board[current_row][current_column] = wrog['pionek']


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
                pygame.draw.circle(screen, gold, rect_center, radius, border)
            if board[row][column] == 4:
                pygame.draw.circle(screen, gold, rect_center, radius, border)
    rect2 = pygame.draw.rect(screen, green, [650, 50, 300, 100])
    rect2_center = rect2.center #       srodek prostokatu(na tekst o turze)
    text_surface_obj = font_obj.render('Hello World!', True, black)     #tu bedzie tekst z tura
    text_rect_obj = text_surface_obj.get_rect()
    text_rect_obj.center = rect2_center
    screen.blit(text_surface_obj, text_rect_obj)

#Ustalam ze gra sie nie skonczyla
game_over = False
board = create_board()
place_starting_pieces()

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
border = (window_width // 200)#3

#Gra
while game_over == False:
    #print("cos")


    # Limit to 60 frames per second
    clock.tick(60)

    # Draw onto screen
    draw_board(board)

    # Update screen with what we drew
    pygame.display.flip()

# Exit the game
pygame.quit()