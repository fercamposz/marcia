import pygame
import random

pygame.init()
largura, altura = 550, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Bingo da mae marcia")

fonte = pygame.font.SysFont("arial", 25)
fonte_bingo = pygame.font.SysFont("arial", 40, bold=True)

# cores
roxo = (150, 0, 200)
branco = (255, 255, 255)
preto = (0, 0, 0)
rosa = (147, 112, 219)

# cartelinha cm numeros
cartela = []
colunas = {
    "B": random.sample(range(1, 16), 5),
    "I": random.sample(range(16, 31), 5),
    "N": random.sample(range(31, 46), 5),
    "G": random.sample(range(46, 61), 5),
    "O": random.sample(range(61, 76), 5)
}

for i in range(5):
    linha = [colunas["B"][i], colunas["I"][i], colunas["N"][i], colunas["G"][i], colunas["O"][i]]
    cartela.append(linha)

cartela[2][2] = "❤️"  # dxa o centro sem nd (hello kitty)

# imagem da hello kitty no meio
hello = pygame.image.load("hellokitty.png")
hello = pygame.transform.scale(hello, (78, 65))

# looop
rodando = True
while rodando:
    tela.fill(rosa)

    # letras BINGO no topo
    letras = ["B", "I", "N", "G", "O"]
    for i, letra in enumerate(letras):
        texto = fonte_bingo.render(letra, True, roxo)
        tela.blit(texto, (i * 100 + 30, 20))

    # por favor funciona porraaaaaaaaaa
    for y in range(5):
        for x in range(5):
            num = cartela[y][x]
            rect = pygame.Rect(x * 100 + 20, y * 100 + 70, 80, 80)
            pygame.draw.rect(tela, branco, rect)
            pygame.draw.rect(tela, roxo, rect, 3)

            if num == "❤️":
                tela.blit(hello, (x * 100 + 20, y * 100 + 70))  # meio sem nada
            else:
                texto = fonte.render(str(num), True, preto)  #exibe os numeros na cor preta 
                tela.blit(texto, (x * 100 + 45, y * 100 + 100))

    pygame.display.flip()

pygame.quit()
