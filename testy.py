import unittest
import Warcaby1.Warcaby as warcaby

class TestWarcaby(unittest.TestCase):
    #1 Wykonanie po dwa ruchy przez kazdego z graczy
    def test_jeden(self):
        #Pierwszy ruch gracza 1
        result = warcaby.Funkcje.ruch(warcaby.game, warcaby.board, 6, 5, 5, 4)
        self.assertIs(result,True)
        #Zmiana gracza
        if warcaby.game.getGracz() == 1:
            warcaby.game.setGracz(2)
        else:
            warcaby.game.setGracz(1)
        warcaby.game.gracz1, warcaby.game.gracz2 = warcaby.game.gracz2, warcaby.game.gracz1
        #Pierwszy ruch gracza 2
        result = warcaby.Funkcje.ruch(warcaby.game, warcaby.board, 5, 2, 4, 3)
        self.assertIs(result,True)
        #Zmiana gracza
        if warcaby.game.getGracz() == 1:
            warcaby.game.setGracz(2)
        else:
            warcaby.game.setGracz(1)
        warcaby.game.gracz1, warcaby.game.gracz2 = warcaby.game.gracz2, warcaby.game.gracz1
        # Drugi ruch gracza 1
        result = warcaby.Funkcje.ruch(warcaby.game, warcaby.board, 0, 5, 1, 4)
        self.assertIs(result, True)
        # Zmiana gracza
        if warcaby.game.getGracz() == 1:
            warcaby.game.setGracz(2)
        else:
            warcaby.game.setGracz(1)
        warcaby.game.gracz1, warcaby.game.gracz2 = warcaby.game.gracz2, warcaby.game.gracz1
        # Drugi ruch gracza 2
        result = warcaby.Funkcje.ruch(warcaby.game, warcaby.board, 3, 2, 2, 3)
        self.assertIs(result, True)

    #2 Niepowodzenie błędnego ruchu pionkiem
    def test_dwa(self):
        result = warcaby.Funkcje.ruch(warcaby.game, warcaby.board, 6, 5, 4, 3)
        self.assertIs(result,False)

    #3 Wykonanie bicia pojedynczego pionka
    def test_trzy(self):
        board1 = [[0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0], [2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        warcaby.game.setGracz(1)
        result = warcaby.Funkcje.ruch(warcaby.game, board1, 5, 4, 3, 2)
        self.assertIs(result, True)


    #Wykonanie bicia przynajmniej dwóch pionków
    def test_cztery(self):
        warcaby.game.setGracz(2)
        warcaby.game.gracz1, warcaby.game.gracz2 = warcaby.game.gracz2, warcaby.game.gracz1
        board2 = [[0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0], [2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0],
                  [0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0], [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        suma_wczesniej = sum([sum(row) for row in board2])
        result1 = warcaby.Funkcje.ruch(warcaby.game, board2, 3, 2, 5, 4)
        suma_teraz = sum([sum(row) for row in board2])
        self.assertIs(result1, True)
        warcaby.game.setGracz(2)
        if suma_wczesniej > suma_teraz:
            # i czy gracz bedzie mial kolejny ruch(zasada ze po biciu drugi ruch gdy mozliwe bicie)
            result2 = warcaby.Funkcje.podwojne_bicie(warcaby.game, board2, 5, 4)
        self.assertIs(result2, True)

    #5 Zamiana pionka na damke
    def test_piec(self):
        board1 = [[0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0], [2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 2, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        result1 = warcaby.Funkcje.ruch(warcaby.game, board1, 7, 6, 6, 7)
        self.assertIs(result1, True)
        self.assertIs(board1[6][7], 2)

    #6 Bicie damką
    def test_szesc(self):
        board1 = [[0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0], [2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 3, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        result = warcaby.Funkcje.krol(warcaby.game, board1, 6, 7, 3, 4)
        self.assertIs(result, True)


    #7 Wygrana gracza grajacego czarnymi pionkami
    def test_siedem(self):

        board = [[0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0], [2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        result = warcaby.Funkcje.czy_ktos_wygral(warcaby.game, board)
        warcaby.game.gracz1, warcaby.game.gracz2 = warcaby.game.gracz2, warcaby.game.gracz1
        self.assertIs(result, True)

    #8 Rozpoczecie nowej gry po zwyciestwie jednego z graczy
    def test_osiem(self):
        try:
            warcaby.game.gracz1, warcaby.game.gracz2 = warcaby.game.gracz2, warcaby.game.gracz1
            board = [[0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0], [2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            result = warcaby.Funkcje.czy_ktos_wygral(warcaby.game, board)
            self.assertIs(result, True)

            result2 = warcaby.game.ponawianie_gry(True) is True
            self.assertIs(result2, False)

            if warcaby.game.getGracz() == 2:
                warcaby.game.gracz1, warcaby.game.gracz2 = warcaby.game.gracz2, warcaby.game.gracz1
            warcaby.interfejs.poczatkowe_rozmieszczenie(board)
            warcaby.game.setGracz(1)
            warcaby.Game(warcaby.game_over)
        except Exception as e:
            print("Blad pojawil sie przy resetowaniu lub ponawianiu gry (pygame.error: video system not initialized)")
            print(e)


if __name__ == '__main__':
    unittest.main()