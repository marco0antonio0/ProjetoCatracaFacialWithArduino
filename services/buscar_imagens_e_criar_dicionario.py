import os

def buscar_imagens_e_criar_dicionario(diretorio_base):
    """
    Busca todas as imagens em um diretório base e cria um dicionário com os identificadores das imagens e seus caminhos.

    Args:
        diretorio_base (str): Caminho do diretório base onde as imagens estão armazenadas.

    Returns:
        dict: Dicionário com identificadores de imagens como chaves e caminhos completos como valores.
    """
    extensoes_validas = ('.jpg', '.jpeg', '.png')
    known_faces = {}

    # Percorre todos os diretórios e subdiretórios
    for root, _, files in os.walk(diretorio_base):
        for file in files:
            if file.lower().endswith(extensoes_validas):
                nome = os.path.splitext(file)[0]  # Extrai o nome do arquivo sem extensão
                caminho_completo = os.path.join(root, file)  # Cria o caminho completo
                known_faces[nome] = caminho_completo  # Adiciona ao dicionário

    return known_faces
