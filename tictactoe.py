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



# Constantes del tablero
ancho_total = 450
alto_total = 450
tam_casilla = 125
x_inicio = 40
y_inicio = 50

# Coordenadas generadas a partir de constantes
coor = []
for fila in range(3):
    start_y = y_inicio + (fila * tam_casilla)
    fila_coor = []
    for col in range(3):
        start_x = x_inicio + (col * tam_casilla)
        fila_coor.append((start_x, start_y))
    coor.append(fila_coor)

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
    # Verificar filas
    for fila in range(3):
        if tablero[fila][0] == tablero[fila][1] == tablero[fila][2] != "":
            return (True, "fila", fila)
    
    # Verificar columnas
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] != "":
            return (True, "col", col)
            
    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != "":
        return (True, "diag", 0) # 0 para diagonal principal
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != "":
        return (True, "diag", 1) # 1 para diagonal inversa
        
    return None

def ver_empate():
    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] == "":
                return False
    return True

def dibujar_linea_ganadora(info, ganador):
    tipo, indice = info
    color = ROJO if ganador == "X" else AZUL
    grosor = 10
    
    start_pos = (0,0)
    end_pos = (0,0)
    
    if tipo == "fila":
        # Y es constante (centro de la fila)
        y = y_inicio + (indice * tam_casilla) + (tam_casilla // 2)
        # X va desde inicio de primera casilla hasta fin de ultima
        start_pos = (x_inicio + 15, y)
        end_pos = (x_inicio + (3 * tam_casilla) - 15, y)
        
    elif tipo == "col":
        # X es constante (centro de la columna)
        x = x_inicio + (indice * tam_casilla) + (tam_casilla // 2)
        start_pos = (x, y_inicio + 15)
        end_pos = (x, y_inicio + (3 * tam_casilla) - 15)
        
    elif tipo == "diag":
        if indice == 0: # Principal \
            start_pos = (x_inicio + 20, y_inicio + 20)
            end_pos = (x_inicio + (3 * tam_casilla) - 20, y_inicio + (3 * tam_casilla) - 20)
        else: # Inversa /
            start_pos = (x_inicio + (3 * tam_casilla) - 20, y_inicio + 20)
            end_pos = (x_inicio + 20, y_inicio + (3 * tam_casilla) - 20)

    pygame.draw.line(screen, color, start_pos, end_pos, grosor)


# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

font = pygame.font.Font(None, 40)

game_over = False
running = True
ganador = None # "X", "O", o "Empate"
info_victoria = None # Tupla (tipo, indice)

def reiniciar_juego():
    global tablero, turno, game_over, ganador, info_victoria
    tablero = [["", "", ""],
               ["", "", ""],
               ["", "", ""]]
    turno = "X"
    game_over = False
    ganador = None
    info_victoria = None

def mostrar_mensaje(texto, color):
    # Crear una superficie de texto
    img_texto = font.render(texto, True, color)
    # Fondo semitransparente para el texto
    s = pygame.Surface((450, 80))
    s.set_alpha(200)
    s.fill(BLANCO)
    screen.blit(s, (0, 185))
    
    # Centrar el texto
    rect = img_texto.get_rect(center=(450/2, 450/2))
    screen.blit(img_texto, rect)
    
    # Mensaje de reinicio
    img_reinicio = font.render("Presiona R o Enter para reiniciar", True, NEGRO)
    img_reinicio = pygame.transform.scale(img_reinicio, (int(img_reinicio.get_width()*0.6), int(img_reinicio.get_height()*0.6)))
    rect_reinicio = img_reinicio.get_rect(center=(450/2, 450/2 + 40))
    screen.blit(img_reinicio, rect_reinicio)

while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r or event.key == pygame.K_RETURN:
                reiniciar_juego()

        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = event.pos
            
            # Verificar limites del tablero jugable
            limite_x = x_inicio + (3 * tam_casilla)
            limite_y = y_inicio + (3 * tam_casilla)
            
            if (mouseX >= x_inicio and mouseX < limite_x) and (mouseY >= y_inicio and mouseY < limite_y):
                # Calcular filas y columnas usando las constantes
                fila = (mouseY - y_inicio) // tam_casilla
                colum = (mouseX - x_inicio) // tam_casilla
                
                # Proteccion extra por si acaso
                if 0 <= fila < 3 and 0 <= colum < 3:
                    if tablero[fila][colum] == "":
                        tablero[fila][colum] = turno
                        
                        resultado = ver_ganador()
                        if resultado:
                            ganador = turno
                            game_over = True
                            info_victoria = (resultado[1], resultado[2]) # Guardar tipo e indice
                        elif ver_empate():
                            ganador = "Empate"
                            game_over = True
                        
                        turno = "O" if turno == "X" else "X"

    graficar_board()
    
    if game_over and ganador != "Empate" and info_victoria:
        dibujar_linea_ganadora(info_victoria, ganador)
    
    if game_over:
        if ganador == "Empate":
            mostrar_mensaje("¡Empate!", NEGRO)
        else:
            color = ROJO if ganador == "X" else AZUL
            mostrar_mensaje(f"¡El jugador {ganador} gana!", color)
            
    pygame.display.update()

pygame.quit()