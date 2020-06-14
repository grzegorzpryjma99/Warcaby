# Warcaby - Raport
## Założenia projektowe kodu
Głównym założeniem projektu było stworzenie prostej gry w warcaby (wersja dowolna). Całość kodu została zaimplementowana w języku Python.
Do stworzenia graficznego interfejsu użytkownika zastosowałem bibliotekę Pygame natomiast do późniejszych testów bibliotekę unittest. Wariant zasad gry w warcaby jaki wybrałem to Warcaby Tureckie.
## Ogólny opis kodu
Cały kod został podzielony na dwa moduły. Moduł testowy który zawiera 8 wymaganych testów napisanych za pomocą biblioteki unittest
Oraz moduł zawierający całą grę. W tym module zastosowałem podział na wymagane klasy ([str. 4 opcja 2](http://elf2.pk.edu.pl/pluginfile.php/88409/mod_resource/content/15/Projekty_JS_2020_wytyczne.pdf)). 
Jest to podział na klasę funkcjonalności programu oraz interfejsu użytkownika. Klasa Interface inicjuję początkowe ustawienie pionków, generuje planszę oraz tworzy wszystkie 
przyciski. Klasa Funkcje zawiera wiele metod z zaimplementowaną logiką poruszania się pionków. W tym module znajduje się również funkcja Game() z całą grą.
## Co udało się zrobić?
Udało się zrealizować główne założenia projektu. Nie obyło się jednak bez napotkanych problemów.
## Z czym były problemy?
* Największy problem sprawiło mi poprawne działanie przycisku reset. Po wykryciu kliknięcia w jego ikonę w głównej pętli programu zastosowałem funkcję która ustawiała ponownie początkowe dane 
i rekurencyjnie wywoływała siebie samą. Powodowało to wiele problemów, między innymi błąd (pygame.error: video system not initialized). Błąd nie kończył gry lecz po zakonczeniu działania aplikacji pojawiał się (tylko przy użyciu restu w grze). Rozwiązanie problemu zajęło dużo czasu lecz po  wielu próbach udało mi się 
temu zaradzić.
* Następny problem napotkałem podczas pisania testów, gdyż była to nowa rzecz i napotkałem wiele sytuacji które mnie zaskoczyły.
* Kolejny już mniejszy problem związany był z logiką damek. Wymagał on jednak po prostu głębszego zastanowienia.
## Testy
Początkowo wszystkie testy przebiegały pomyslnie z wyjątkiem ostatniego. Po naprawie błędu z przyciskiem reset i ogólnego ponawiania gry (problem rozwiązany przez dodanie sys.exit() na końcu pętli gry [sprawdź](https://github.com/grzegorzpryjma99/Warcaby/blob/master/Warcaby.py#L596)) test 8 (Rozpoczęcie nowej gry po zwycięstwie jednego z graczy.) konczył się błędem empty suite. 
Po ponownym zakomentowaniu tej lini kodu wszystkie testy kończą się poprawnie natomiast błąd moze wystąpić podczas zwykłego użytkowania aplikacji. Zastosowałem dlatego obsługę wyjątków.
Podsumowując, moja aplikacja przeszła poprawnie wszystkie wymagane testy
## Istotne fragmenty kodu
Moduły:

[1 Moduł Warcaby.py](https://github.com/grzegorzpryjma99/Warcaby/blob/master/Warcaby.py)

[2 Moduł testy.py](https://github.com/grzegorzpryjma99/Warcaby/blob/master/testy.py)

Wyjątki:

[1 Odnośnik](https://github.com/grzegorzpryjma99/Warcaby/blob/master/Warcaby.py#L260-L268)

[2 Odnośnik](https://github.com/grzegorzpryjma99/Warcaby/blob/master/Warcaby.py#L270-L278)

[3 Odnośnik](https://github.com/grzegorzpryjma99/Warcaby/blob/master/Warcaby.py#L280-L294)

[4 Odnośnik](https://github.com/grzegorzpryjma99/Warcaby/blob/master/Warcaby.py#L378-L386)

[5 Odnośnik](https://github.com/grzegorzpryjma99/Warcaby/blob/master/Warcaby.py#L387-L395)

[6 Odnośnik](https://github.com/grzegorzpryjma99/Warcaby/blob/master/Warcaby.py#L396-L404)

[7 Odnośnik](https://github.com/grzegorzpryjma99/Warcaby/blob/master/Warcaby.py#L405-L413)

Klasy

[1 Klasa](https://github.com/grzegorzpryjma99/Warcaby/blob/master/Warcaby.py#L4-L139)

[2 Klasa](https://github.com/grzegorzpryjma99/Warcaby/blob/master/Warcaby.py#L140-L453)

List comprehensions

[1 Odnośnik](https://github.com/grzegorzpryjma99/Warcaby/blob/master/Warcaby.py#L479)

[2 Odnośnik](https://github.com/grzegorzpryjma99/Warcaby/blob/master/Warcaby.py#L315)

[3 Odnośnik](https://github.com/grzegorzpryjma99/Warcaby/blob/master/Warcaby.py#L515)

[4 Odnośnik](https://github.com/grzegorzpryjma99/Warcaby/blob/master/Warcaby.py#L554)

## [Repository](https://github.com/grzegorzpryjma99/Warcaby)
