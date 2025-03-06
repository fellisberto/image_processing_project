from utils import (
    carregar_imagem_caminho,
    exibir_imagem_cv2,
    exibir_imagem_pil,
    exibir_imagem_skimage,
    converter_para_cinza,
    redimensionar_imagem,
    rotacionar_imagem
)

# Caminho da imagem
caminho_imagem = '../data/imagem_exemplo.jpg'

# Carregar imagens em diferentes bibliotecas
imagem_cv2, imagem_pil, imagem_sk = carregar_imagem_caminho(caminho_imagem)

# Exibir imagens originais
exibir_imagem_cv2('Imagem OpenCV', imagem_cv2)
exibir_imagem_pil(imagem_pil)
exibir_imagem_skimage(imagem_sk)

# Converter e exibir imagens em escala de cinza
imagem_cinza_cv2, imagem_cinza_sk = converter_para_cinza(imagem_cv2, imagem_sk)
exibir_imagem_cv2('Imagem Cinza OpenCV', imagem_cinza_cv2)
exibir_imagem_skimage(imagem_cinza_sk)

# Redimensionar e exibir imagens
tamanho = (200, 200)
imagem_redimensionada_cv2, imagem_redimensionada_pil, imagem_redimensionada_sk = redimensionar_imagem(
    imagem_cv2, imagem_pil, imagem_sk, tamanho)
exibir_imagem_cv2('Imagem Redimensionada OpenCV', imagem_redimensionada_cv2)
exibir_imagem_pil(imagem_redimensionada_pil)
exibir_imagem_skimage(imagem_redimensionada_sk)

# Rotacionar e exibir imagem
imagem_rotacionada = rotacionar_imagem(imagem_cv2, 45)
exibir_imagem_cv2('Imagem Rotacionada OpenCV', imagem_rotacionada)
