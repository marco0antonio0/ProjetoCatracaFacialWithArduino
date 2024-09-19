import face_recognition
import cv2
import numpy as np


def recognize_faces(frame):
    """
    Detecta rostos e obtém as codificações dos rostos no frame atual.

    Args:
        frame (ndarray): Frame de vídeo capturado.

    Returns:
        tuple: Uma tupla contendo as localizações dos rostos e as codificações faciais.
    """
    # Reduz o tamanho do frame para 1/4 para aumentar a velocidade de processamento
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Converte o frame de BGR para RGB
    rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])

    # Detecta os rostos e obtém as codificações dos rostos no frame atual
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    return face_locations, face_encodings
