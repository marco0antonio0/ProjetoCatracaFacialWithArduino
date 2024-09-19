import cv2
import serial
import serial.tools.list_ports
from services.draw_results import draw_results
from services.process_frame import process_frame
from services.load_known_faces import load_known_faces


# Função para listar as portas seriais disponíveis
def listar_portas():
    ports = list(serial.tools.list_ports.comports())
    if len(ports) == 0:
        print("Nenhuma porta serial disponível.")
    else:
        print("Portas seriais disponíveis:")
        for i, port in enumerate(ports):
            print(f"{i}: {port.device}")

    return ports


def main():
    # ================================================================================
    # Listar as portas disponíveis e escolher uma
    portas_disponiveis = listar_portas()

    if len(portas_disponiveis) == 0:
        print(
            "Nenhuma porta disponível. Certifique-se de que o Arduino está conectado."
        )
        return

    # Pedir ao usuário para escolher a porta
    porta_escolhida = int(input("Escolha o número da porta que deseja usar: "))
    arduino_port = portas_disponiveis[porta_escolhida].device
    baud_rate = 9600

    # Tenta conectar à porta serial escolhida
    try:
        arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
        print(f"Conectado ao Arduino na porta {arduino_port}")
    except serial.SerialException as e:
        print(f"Erro ao abrir a porta serial {arduino_port}: {e}")
        return
    # ================================================================================

    directory = "./images"
    # Carrega as codificações faciais e os nomes a partir dos diretórios
    known_face_encodings, known_face_names = load_known_faces(directory)

    # ========================================
    video_capture = cv2.VideoCapture(0)
    # ========================================
    process_this_frame = True
    face_locations, face_names = [], []

    while True:
        ret, frame = video_capture.read()

        # Processa frames alternados para melhorar o desempenho
        if process_this_frame:
            face_locations, face_names = process_frame(
                frame, known_face_encodings, known_face_names
            )

            # Se um rosto conhecido for detectado, enviar comando para o Arduino
            if len(face_names) > 0:  # Verifica se há rostos conhecidos detectados
                for name in face_names:
                    if name in known_face_names:
                        print(f"Rosto conhecido detectado: {name}")
                        arduino.write(
                            b"8"
                        )  # Envia o comando '8' para acionar o LED no Arduino
            else:
                arduino.write(b"9")  # Envia o comando '9' se nenhum rosto for detectado

        # Desenha os resultados no frame
        frame = draw_results(frame, face_locations, face_names)

        # Alterna o processamento de frames
        process_this_frame = not process_this_frame

        # Exibe o frame resultante
        cv2.imshow("Video", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    arduino.close()  # Fecha a comunicação serial


if __name__ == "__main__":
    main()
