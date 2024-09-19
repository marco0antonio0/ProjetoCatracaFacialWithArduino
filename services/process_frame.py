import face_recognition
import cv2
import numpy as np
from .match_face import match_face
from .recognize_faces import recognize_faces


def process_frame(frame, known_face_encodings, known_face_names):
    """
    Processa um frame de vídeo para detectar e reconhecer rostos.

    Args:
        frame (ndarray): Frame de vídeo capturado.
        known_face_encodings (list): Lista de codificações faciais conhecidas.
        known_face_names (list): Lista de nomes correspondentes aos rostos conhecidos.

    Returns:
        tuple: Uma tupla contendo localizações dos rostos e nomes reconhecidos.
    """
    # ====================================================================
    # Usa a função modularizada para reconhecimento de rostos
    face_locations, face_encodings = recognize_faces(frame)
    # ====================================================================

    # Realiza o "match" de cada rosto detectado
    face_names = [
        match_face(encoding, known_face_encodings, known_face_names)
        for encoding in face_encodings
    ]

    return face_locations, face_names
