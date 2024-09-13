import cv2
import numpy as np

# Carregar a imagem
img = cv2.imread("mama_contornos.jpg", cv2.IMREAD_GRAYSCALE)

# Verificar se a imagem foi carregada corretamente
if img is None:
    print("Erro: A imagem não pôde ser carregada. Verifique o caminho e o nome do arquivo.")
else:
    # Mostrar a imagem para verificar o conteúdo
    cv2.imshow('Imagem Original', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Calcular o número de pixels brancos (valor 255) e pretos (valor 0)
    numero_pixels_branco = np.sum(img == 255)
    numero_pixels_preto = np.sum(img == 0)

    print('Número de pixels brancos:', numero_pixels_branco)
    print('Número de pixels pretos:', numero_pixels_preto)

    # Calcular o percentual de pixels brancos
    total_pixels = img.size
    percentual_pixels_brancos = (numero_pixels_branco / total_pixels) * 100

    print("Percentual de pixels brancos:", percentual_pixels_brancos)

    # Ajustar o limiar se necessário
    limiar = 30
    if percentual_pixels_brancos > limiar:
        resultado = 'Imagem com possível presença de câncer'
        cor_texto = (0, 0, 255)  # Vermelho
    else:
        resultado = 'Imagem sem indícios de câncer'
        cor_texto = (0, 255, 0)  # Verde

    print(resultado)

    # Converter a imagem para BGR (para adicionar cor ao texto)
    img_colorida = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    # Adicionar o texto na imagem
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img_colorida, resultado, (10, 30), fonte, 0.7, cor_texto, 2, cv2.LINE_AA)
    cv2.putText(img_colorida, f"Percentual de pixels brancos: {percentual_pixels_brancos:.2f}%", 
                (10, 60), fonte, 0.7, cor_texto, 2, cv2.LINE_AA)

    # Exibir a imagem com o resultado
    cv2.imshow('Resultado da Análise', img_colorida)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
