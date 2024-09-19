
# Reconhecimento Facial em Vídeo
![img](imagesReadme/banner.png)
Este projeto implementa um sistema de reconhecimento facial em tempo real usando a webcam. Ele carrega as codificações faciais conhecidas a partir de imagens armazenadas em diretórios específicos e então processa o vídeo capturado pela webcam para identificar as faces presentes.

## Estrutura do Projeto

- **`main.py`**: O ponto de entrada do sistema. Configura a captura de vídeo e coordena as etapas de processamento e exibição.
- **`images/`**: Adicione Imagens para dectção facial, sendo o titulo da imagem vai ser usado como label identificador na imagem
- **`services/`**:
  - **`load_face_encodings.py`**: Carrega as codificações faciais conhecidas a partir das imagens em diretórios.
  - **`draw_results.py`**: Desenha os resultados de reconhecimento no frame de vídeo.
  - **`buscar_imagens_e_criar_dicionario.py`**: Busca todas as imagens em um diretório e cria um dicionário associando os nomes às imagens.
  - **`recognize_faces.py`**: Reconhece faces em imagens ou frames de vídeo usando codificações faciais conhecidas.
  - **`match_face.py`**: Realiza a correspondência entre uma face detectada e as codificações faciais conhecidas.
  - **`process_frame.py`**: Processa cada frame de vídeo para detectar e reconhecer faces.
  - **`get_first_valid_encoding.py`**: Extrai a primeira codificação facial válida de um diretório ou arquivo de imagem.
  - **`load_known_faces.py`**: Carrega as codificações faciais e os nomes das pessoas a partir de diretórios especificados.

## Instalação

1. Clone o repositório e acesse a pasta do projeto:

   ```bash
   git clone https://github.com/marco0antonio0/py-facial-detector-video
   ```

    ```bash
   cd seu-repositorio
   ```

2. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

3. Certifique-se de que você tenha o `opencv-python` e o `face_recognition` instalados.

## Uso

1. Adicione as imagens das pessoas que deseja reconhecer nos diretórios apropriados no diretorio images.
   ```bash
   ./images/
   ```
2. Execute o script principal:

   ```bash
   python3 app.py
   ```

   Isso iniciará a captura de vídeo e o sistema tentará reconhecer as faces em tempo real.

3. Pressione `q` para sair do vídeo.

## Modularização

O código foi modularizado para facilitar a manutenção e a legibilidade:

- **Captura de Vídeo**: A captura de vídeo é configurada na função `main()`, que chama os serviços para carregar as codificações faciais e processar cada frame.
- **Processamento de Frames**: O processamento dos frames é realizado alternadamente para melhorar o desempenho. Isso é feito na função `process_frame()`.
- **Desenho dos Resultados**: A função `draw_results()` é responsável por desenhar as caixas delimitadoras e os nomes das pessoas reconhecidas no frame de vídeo.
- **Carregamento de Codificações**: As codificações faciais conhecidas são carregadas usando a função `load_known_faces()`.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
