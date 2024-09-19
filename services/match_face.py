import face_recognition
import numpy as np


def match_face(face_encoding, known_face_encodings, known_face_names):
    """
    Compara uma codificação facial com codificações conhecidas e retorna o nome correspondente.

    Args:
        face_encoding (ndarray): Codificação facial a ser comparada.
        known_face_encodings (list): Lista de codificações faciais conhecidas.
        known_face_names (list): Lista de nomes correspondentes às codificações conhecidas.

    Returns:
        str: Nome correspondente ao rosto mais próximo ou "Unknown" se não houver correspondência.
    """
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Unknown"

    # Usa o rosto conhecido mais próximo com a menor distância
    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        name = known_face_names[best_match_index]

    return name
