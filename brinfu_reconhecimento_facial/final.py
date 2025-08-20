import face_recognition
import cv2

# Carrega imagem do Aluno e codifica o rosto em um vetor
minha_face = face_recognition.load_image_file("eu.jpg")
minha_cod = face_recognition.face_encodings(minha_face)[0]
meu_nome = "Diego Macedo"

# Limite de distância para reconhecimento indo de 0.1 a 1.0
# Valores típicos: 0.6 é um limite comum para considerar "mesma pessoa".
# Quando menor mais preciso, mas pode aumentar falsos negativos.
distancia_limite = 0.6

# BGR (0, 0, 255) é vermelho, 
# (0, 255, 0) é verde
# (255, 0, 0) é azul
cor_reconhecido = (0, 0, 255)

# Branco para o texto
cor_texto = (255, 255, 255)

# Abre a câmera
video = cv2.VideoCapture(0)

# Laço principal para capturar vídeo
while True:
    # Captura um frame da câmera
    ret, frame = video.read()
    if not ret:
        break

    # Reduz imagem e converte para RGB
    small = cv2.resize(
        src=frame, # Origem de qual imagem para reduzir reduzir
        dsize=(0, 0),  # Tamanho de destino, 0 significa manter a proporção
        fx=0.25, # Fator de escala na largura
        fy=0.25  # Fator de escala na altura
    )

    # Converte a imagem de BGR (OpenCV) para RGB (face_recognition)
    rgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

    # Detecta rostos e codifica cada um
    locs = face_recognition.face_locations(rgb)
    codes = face_recognition.face_encodings(rgb, locs)

    for (top, right, bottom, left), code in zip(locs, codes):
        name = "Desconhecido"
        
        dists = face_recognition.face_distance([minha_cod], code)
        
        # Verifica se a distância é menor que o limite
        if dists[0] < distancia_limite:
            name = meu_nome

        # Ajusta posições para o tamanho original
        top, right, bottom, left = [v*4 for v in (top, right, bottom, left)]

        # Desenha retângulo e escreve o nome
        cv2.rectangle(
            img=frame, #Origem da imagem onde desenhar o retângulo
            pt1=(left, top),  # Cordeadas do canto superior esquerdo
            pt2=(right, bottom),  # Codeadas do canto inferior direito
            color=cor_reconhecido, # Cor do retângulo em BGR (azul, verde, vermelho)
            thickness=2 # Espessura do retângulo, -1 o triangulo é preenchido
        )
        
        # Desenha um círculo ao redor do rosto (opcional)
        # cv2.circle(
        #     img=frame, # Origem da imagem onde desenhar o círculo
        #     center=((left + right) // 2, (top + bottom) // 2), # Centro do círculo
        #     radius=300, # Raio do círculo
        #     color=color_reconhecido, # Cor do círculo em BGR (azul, verde, vermelho)
        #     thickness=2 # Preenchido
        # )

        # Escreve o nome abaixo do rosto
        cv2.putText(
            img=frame, 
            text=name, 
            org=(left, bottom + 20), 
            fontFace=cv2.FONT_HERSHEY_SIMPLEX, 
            fontScale=0.7, 
            color=cor_texto, 
            thickness=1
        )

    # Exibe o vídeo com os rostos detectados
    cv2.imshow("Video", frame)

    # Pressione a tecla 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break