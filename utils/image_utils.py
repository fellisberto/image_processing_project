import cv2
from PIL import Image
from skimage import io
from skimage.color import rgb2gray
from skimage.transform import resize

def carregar_imagem_caminho(caminho):
    return cv2.imread(caminho), Image.open(caminho), io.imread(caminho)

def exibir_imagem_cv2(titulo, imagem):
    cv2.imshow(titulo, imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def exibir_imagem_pil(imagem_pil):
    imagem_pil.show()

def exibir_imagem_skimage(imagem_sk):
    io.imshow(imagem_sk)
    io.show()

def converter_para_cinza(imagem_cv2, imagem_sk):
    imagem_cinza_cv2 = cv2.cvtColor(imagem_cv2, cv2.COLOR_BGR2GRAY)
    imagem_cinza_sk = rgb2gray(imagem_sk)
    return imagem_cinza_cv2, imagem_cinza_sk

def redimensionar_imagem(imagem_cv2, imagem_pil, imagem_sk, tamanho):
    imagem_redimensionada_cv2 = cv2.resize(imagem_cv2, tamanho)
    imagem_redimensionada_pil = imagem_pil.resize(tamanho)
    imagem_redimensionada_sk = resize(imagem_sk, tamanho)
    return imagem_redimensionada_cv2, imagem_redimensionada_pil, imagem_redimensionada_sk

def rotacionar_imagem(imagem, angulo):
    h, w = imagem.shape[:2]
    centro = (w // 2, h // 2)
    matriz = cv2.getRotationMatrix2D(centro, angulo, 1.0)
    return cv2.warpAffine(imagem, matriz, (w, h))