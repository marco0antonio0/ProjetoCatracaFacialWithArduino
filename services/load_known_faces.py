import numpy as np
from .get_first_valid_encoding import get_first_valid_encoding
from .buscar_imagens_e_criar_dicionario import buscar_imagens_e_criar_dicionario

def load_known_faces(directory_dir):
    """
    Carrega as codificações faciais e os nomes das pessoas a partir de seus diretórios.

    Args:
        known_faces (dict): Dicionário com nomes e caminhos dos diretórios.

    Returns:
        known_face_encodings (list): Lista de codificações faciais.
        known_face_names (list): Lista de nomes correspondentes às codificações.
    """
    known_faces = buscar_imagens_e_criar_dicionario(directory_dir)
    known_face_encodings = []
    known_face_names = []

    for name, directory in known_faces.items():
        encoding = get_first_valid_encoding(directory)
        if encoding is not None:
            known_face_encodings.append(encoding)
            known_face_names.append(name)
        else:
            print(
                f"Atenção: Nenhuma imagem válida encontrada para {name} em {directory}"
            )

    return known_face_encodings, known_face_names
