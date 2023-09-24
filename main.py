import matplotlib.pyplot as plt
import numpy as np


def desenhar_labirinto(labirinto, caminho=None):
    mapa_cores = {'#': 0, '.': 1, 'R': 2, 'Q': 3}
    labirinto_numerico = np.array([[mapa_cores[celula] for celula in linha] for linha in labirinto])
    cmap = plt.cm.colors.ListedColormap(['black', 'white', 'grey', 'yellow'])
    plt.imshow(labirinto_numerico, cmap=cmap)
    ax = plt.gca()
    ax.set_xticks(np.arange(-.5, labirinto_numerico.shape[1], 1), minor=True)
    ax.set_yticks(np.arange(-.5, labirinto_numerico.shape[0], 1), minor=True)
    ax.grid(which="minor", color="gray", linestyle='-', linewidth=1)
    if caminho:
        for i in range(1, len(caminho)):
            y1, x1 = caminho[i - 1]
            y2, x2 = caminho[i]
            plt.arrow(x1, y1, x2 - x1, y2 - y1, head_width=0.2, head_length=0.2, fc='blue', ec='blue')
    plt.show()


def encontrar_caminho(labirinto):
    global objetivo
    for i, linha in enumerate(labirinto):
        for j, celula in enumerate(linha):
            if celula == "R":
                inicio = (i, j)
            elif celula == "Q":
                objetivo = (i, j)

    pilha = [inicio]
    visitados = set()

    direcoes = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    # Busca em profundidade
    while pilha:
        pos_atual = pilha[-1]

        if pos_atual == objetivo:
            return pilha

        visitados.add(pos_atual)
        for dx, dy in direcoes:
            x, y = pos_atual[0] + dx, pos_atual[1] + dy
            if 0 <= x < len(labirinto) and 0 <= y < len(labirinto[0]) and labirinto[x][y] not in ("#", "R") and (
                    x, y) not in visitados:
                pilha.append((x, y))
                break
        else:
            pilha.pop()
    return None

labirinto = [
    ["R", ".", "#", "#", ".", ".", ".", ".", ".", ".", "."],
    [".", "#", ".", ".", "#", ".", "#", ".", "#", "#", "."],
    [".", ".", "#", ".", "#", ".", "#", ".", ".", ".", "#"],
    [".", "#", ".", "#", ".", ".", ".", "#", "#", ".", "."],
    [".", ".", ".", "#", ".", "#", ".", ".", ".", "#", "."],
    [".", "#", ".", ".", ".", ".", ".", ".", "#", ".", "Q"]
]

caminho = encontrar_caminho(labirinto)
if caminho:
    for pos in caminho:
        print(pos)
    desenhar_labirinto(labirinto, caminho)
else:
    print("Não há caminho até o queijo.")
