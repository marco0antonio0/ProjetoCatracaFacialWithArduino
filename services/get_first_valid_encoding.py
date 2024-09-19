import os
import face_recognition

def get_first_valid_encoding(path):
    """
    Carrega a primeira imagem válida de um diretório ou arquivo e retorna sua codificação facial.

    Args:
        path (str): Caminho do diretório contendo as imagens ou de um arquivo de imagem.

    Returns:
        encoding (list): Codificação facial encontrada.
    """
    # Verifica se é um diretório ou um arquivo
    if os.path.isdir(path):
        # Se for um diretório, percorre os arquivos dentro dele
        for file_name in os.listdir(path):
            if file_name.lower().endswith((".png", ".jpg", ".jpeg")):
                image_path = os.path.join(path, file_name)
                image = face_recognition.load_image_file(image_path)
                encodings = face_recognition.face_encodings(image)

                if encodings:  # Retorna a primeira codificação válida encontrada
                    return encodings[0]
    elif os.path.isfile(path) and path.lower().endswith((".png", ".jpg", ".jpeg")):
        # Se for um arquivo de imagem, processa-o diretamente
        image = face_recognition.load_image_file(path)
        encodings = face_recognition.face_encodings(image)

        if encodings:  # Retorna a primeira codificação válida encontrada
            return encodings[0]

    return None