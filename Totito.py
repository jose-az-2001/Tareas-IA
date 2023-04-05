import random
import math
import os

class Totito:
    def __init__(self):
        self.tablero = ['-' for _ in range(9)]
        if random.randint(0, 1) == 1:
            self.humano = 'X'
            self.bot = "O"

# Se imprime el tablero
    def mostrarTabla(self):
        print(" __________________")
        for i in range(3):
            print(" | ",self.tablero[0+(i*3)]," | ",self.tablero[1+(i*3)]," | ",self.tablero[2+(i*3)], "|")
            print(" __________________")
            
# Si el tablo esta lleno            
    def tablero_lleno(self,estado):
        return not "-" in estado
    
# arbol de desicion
    def jugaro_gana(self,estado,player):
        if estado[0]==estado[1]==estado[2] == player: return True
        if estado[3]==estado[4]==estado[5] == player: return True
        if estado[6]==estado[7]==estado[8] == player: return True
        if estado[0]==estado[3]==estado[6] == player: return True
        if estado[1]==estado[4]==estado[7] == player: return True
        if estado[2]==estado[5]==estado[8] == player: return True
        if estado[0]==estado[4]==estado[8] == player: return True
        if estado[2]==estado[4]==estado[6] == player: return True
        return False
    
# Verificamos si el humano gano
    def verificar_ganador(self):
        if self.jugaro_gana(self.tablero,self.humano):
            os.system("cls")
            print(f"    {self.humano} ganó el humano")
            return True
# Si no el bot gano
        if self.jugaro_gana(self.tablero,self.bot):
            os.system("cls")
            print(f"    {self.bot} ganó el bot")
            return True
        # Empate
        if self.tablero_lleno(self.tablero):
            os.system("cls")
            print("  Hay empate!")
            return True
        return False
    
# Empezar el juego
    def start(self):
        bot1 = bot_jugador(self.bot)
        human = humano(self.humano)
        while True:
            os.system("cls")
            print(f"Turno del humano {self.humano} ")
            self.mostrarTabla()
            
            #Verifica el tablero Humano
            square = human.humano_mov(self.tablero)
            self.tablero[square] = self.humano
            if self.verificar_ganador():
                break
            
            #Verifica el tablero Bot
            square = bot1.bot_mov(self.tablero)
            self.tablero[square] = self.bot
            if self.verificar_ganador():
                break
        print()
        self.mostrarTabla()
        
# Clase del humano
class humano:
    def __init__(self,letter):
        self.letter = letter
    
    def humano_mov(self,estado):
        # Elije la casilla a jugar
        while True:
            turno =  int(input("Elija una casilla para colocar X del 1 al 9: "))
            print()
            if estado[turno-1] == "-":
                break
        return turno-1
#clase del bot
class bot_jugador(Totito):
    def __init__(self,letter):
        self.bot = letter
        self.humano = "X" if letter == "O" else "O"
#Movimiento del bot
    def bot_mov(self,estado):
        turno = self.minimax(estado,self.bot)['posicion']
        return turno
    
    def jugadores(self,estado):
        n = len(estado)
        x = 0
        o = 0
        for i in range(9):
            if(estado[i] == "X"):
                x = x+1
            if(estado[i] == "O"):
                o = o+1
        
        if(self.humano == "X"):
            return "X" if x==o else "O"
        if(self.humano == "O"):
            return "O" if x==o else "X"
    
    def acciones(self,estado):
        return [i for i, x in enumerate(estado) if x == "-"]
    
    def result(self,estado,action):
        newestado = estado.copy()
        player = self.jugadores(estado)
        newestado[action] = player
        return newestado
    
    def terminal(self,estado):
        if(self.jugaro_gana(estado,"X")):
            return True
        if(self.jugaro_gana(estado,"O")):
            return True
        return False

    def minimax(self, estado, jugador):
        max_jugador = self.humano  
        other_jugador = 'O' if jugador == 'X' else 'X'

        # Verifica si existe un ganador en el movimiento anterior
        if self.terminal(estado):
            return {'posicion': None, 'puntuación': 1 * (len(self.acciones(estado)) + 1) if other_jugador == max_jugador else -1 * (
                        len(self.acciones(estado)) + 1)}
        elif self.tablero_lleno(estado):
            return {'posicion': None, 'puntuación': 0}

        if jugador == max_jugador:
            mOpcion = {'posicion': None, 'puntuación': -math.inf}  
        else:
            mOpcion = {'posicion': None, 'puntuación': math.inf}  
        for possible_move in self.acciones(estado):
            newestado = self.result(estado,possible_move)
            sim_score = self.minimax(newestado, other_jugador)  

            sim_score['posicion'] = possible_move  

            if jugador == max_jugador:
                if sim_score['puntuación'] > mOpcion['puntuación']:
                    mOpcion = sim_score
            else:
                if sim_score['puntuación'] < mOpcion['puntuación']:
                    mOpcion = sim_score
        return mOpcion



# Empezar el juego
totito = Totito()
totito.start()