import face_recognition


def load_face_encodings(image_paths, names):
    """
    Carrega imagens e gera codificações faciais para rostos conhecidos.

    Args:
        image_paths (list): Lista de caminhos para as imagens.
        names (list): Lista de nomes correspondentes aos rostos nas imagens.

    Returns:
        tuple: Uma tupla contendo duas listas - codificações faciais e nomes.
    """
    face_encodings = []
    for image_path in image_paths:
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]
        face_encodings.append(encoding)
    return face_encodings, names
