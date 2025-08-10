import pygame

pygame.init()

screen = pygame.display.set_mode((450,450))
pygame.display.set_caption("Triki")

fondo = pygame.image.load("stactic/tictactoe_background.png")
equix = pygame.image.load("stactic/x.png")
circulo = pygame.image.load("stactic/circle.png")

fondo = pygame.transform.scale(fondo,(450,450))
equix = pygame.transform.scale(equix,(125,125))
circulo = pygame.transform.scale(circulo,(125,125))


coor = [[(40,50),  (165,50), (290,50)],
        [(40,175), (165,175), (290,175)],
        [(40,300), (165,300), (290,300)]]

tablero = [["", "", ""],
           ["", "", ""],
           ["", "", ""]]

turno = "X"
game_over = False
clock = pygame.time.Clock()

def graficar_board():
    screen.blit(fondo, (0, 0))
    for fila in range(3):
        for colum in range(3):
            if tablero[fila][colum] == "X":
                dibujar_X(fila,colum)
            elif tablero[fila][colum] == "O":
                dibujar_O(fila,colum)



def dibujar_X(fila,colum):
    screen.blit(equix,(coor[fila][colum]))


def dibujar_O(fila,colum):
    screen.blit(circulo,(coor[fila][colum]))

""""
[0][0],[0][1],[0][2]
[1][0],[1][1],[1][2]
[2][0],[2][1],[2][2]
"""

def ver_ganador():
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != "":
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != "":
            return True
        if tablero[0][0] == tablero[1][1] == tablero[2][2] != "":
            return True
        if tablero[0][2] == tablero[1][1] == tablero[2][0] != "":
            return True
        if tablero[0][1] == tablero[1][1] == tablero[2][1] != "":
            return True
        return False

while not game_over:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            if (mouseX >=40 and mouseX < 415) and ( mouseY >=40 and mouseY <425):
                fila = (mouseY - 50) // 125
                colum = (mouseX -50) // 125
                if tablero[fila][colum] == "":
                    tablero[fila][colum] = turno
                    fin_juego = ver_ganador()
                    if fin_juego:
                        print(f"el jugador {turno} ha ganado")
                        game_over = True

                    turno = "O" if turno == "X" else "X"

    graficar_board()
    pygame.display.update()

pygame.quit()