import cv2
import numpy as np

# Carregar a imagem
imagem = cv2.imread('cavalo.jpg')

# Separando os canais de cor em azul, verde e vermelho
azul, verde, vermelho = cv2.split(imagem)

# Mesclando os canais de cor, na ordem azul, verde e vermelho
imagem_mesclada = cv2.merge((azul, verde, vermelho))

# Invertendo os canais de cor
imagem_invertida = cv2.merge((vermelho, verde, azul))

# Criando uma imagem branca nas dimensões da imagem lida
blank = np.zeros(imagem.shape[:2], dtype='uint8')

# Abrindo as imagens por canais e mesclando com as matrizes de zero (blank)
canal_azul = cv2.merge([azul, blank, blank])
canal_verde = cv2.merge([blank, verde, blank])
canal_vermelho = cv2.merge([blank, blank, vermelho])

# Exibindo a imagem original
cv2.imshow('Imagem Original', imagem)

# Exibindo os canais de cores separadamente
cv2.imshow('Canal Azul', canal_azul)
cv2.imshow('Canal Verde', canal_verde)
cv2.imshow('Canal Vermelho', canal_vermelho)

# Exibindo a imagem mesclada
cv2.imshow('Imagem Mesclada', imagem_mesclada)

# Exibindo a imagem com canais invertidos
cv2.imshow('Imagem Invertida', imagem_invertida)

# Salvando as imagens dos canais
cv2.imwrite('Azul.png', canal_azul)
cv2.imwrite('Verde.png', canal_verde)
cv2.imwrite('Vermelho.png', canal_vermelho)

# Salvando a imagem mesclada e a imagem com os canais invertidos
cv2.imwrite('imagem_mesclada.png', imagem_mesclada)
cv2.imwrite('imagem_invertida.png', imagem_invertida)

# Esperar até que uma tecla seja pressionada
cv2.waitKey(0)

# Fechar todas as janelas
cv2.destroyAllWindows()
