#   Gioco dell'oca sviluppato da GodAlecs
#   https://github.com/GodAlecs
import sys
from random import randint

#   Funzione Main
def main():
    #   Visiona se lo script è stato avviato con i parametri giusti
    if len(sys.argv[1:]) == 1 and sys.argv[1].isdigit():
        #   Controlla se ci sono 2 o più giocatori
        if int(sys.argv[1]) < 2:
            print("Non puoi avviare la partita se non si dispone di almeno 2 giocatori!")
        else:
            #   Inizia la partita
            start_game(int(sys.argv[1]))
    else:
        print("Utilizza: python main.py <numero-giocatori>")

#   Funzione che genera numeri randomici per il dado
def random():
    return randint(1, 6)

#   Funzione che vede se qualcuno ha vinto
def check_winner(players):
    for x in players:
        if players[x] == 20:
            print("La pedina numero '" + x + "' ha vinto!")
            return False
        else: 
            return True

#    Funzione che visiona se il giocatore ha superato la casella 20
def check_if_pass_the_box(list, player):
    if list[player] >= 20:
        diff = list[player] - 20
        list[player] = 20 - diff

#   Funzione che visiona se qualcuno ha vinto
def check_winner(list, round):
    if list[round] == 20:
        print("La pedina numero '" + str(round) + "' ha vinto!")
        return False
    else:
        return True

#   Funzione inizio gioco
def start_game(players):
    print("|------------[ INIZIO PARTITA ]-------------|")
    list = []
    for x in range(players):
        list.append(0)
    
    round = 0
    while (check_winner(list, round)):
        dado = random()
        list[round] += dado
        check_if_pass_the_box(list, round)
        round = (round + 1) % players

    print("|------------[ FINE PARTITA ]-------------|")

#   Non rimuovere
if __name__ == "__main__":
    main()