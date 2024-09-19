import cv2


def draw_results(frame, face_locations, face_names, padding=30):
    """
    Desenha os resultados da detecção e reconhecimento de rostos no frame, com um padding adicional.

    Args:
        frame (ndarray): Frame de vídeo original.
        face_locations (list): Lista de localizações dos rostos.
        face_names (list): Lista de nomes reconhecidos.
        padding (int): Quantidade de padding a ser adicionada ao redor do rosto.

    Returns:
        ndarray: Frame com as marcações desenhadas.
    """
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Redimensiona as localizações dos rostos para o tamanho original do frame
        top = max(0, (top * 4) - padding)
        right = min(frame.shape[1], (right * 4) + padding)
        bottom = min(frame.shape[0], (bottom * 4) + padding)
        left = max(0, (left * 4) - padding)

        # Desenha um retângulo ao redor do rosto com padding adicional
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Desenha uma etiqueta com o nome abaixo do rosto, com padding
        cv2.rectangle(
            frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED
        )
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    return frame
