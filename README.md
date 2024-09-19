# Reconhecimento Facial em Vídeo com Simulação de Catraca

https://github.com/user-attachments/assets/6e428713-54ec-40aa-adb2-0b7d46f221fd

Este projeto implementa um sistema de reconhecimento facial em tempo real usando a webcam e simula o controle de uma catraca baseada na autenticação facial. Através da detecção facial, o programa comunica-se com um Arduino, que controla LEDs para representar o mecanismo de abrir ou fechar a catraca.

## Objetivo do Projeto

Este projeto tem como objetivo acadêmico desenvolver um sistema que detecta rostos conhecidos e, de acordo com o resultado da autenticação, simula a abertura ou fechamento de uma catraca. Essa simulação é feita utilizando dois LEDs conectados a um Arduino: um LED vermelho e um LED azul. O LED azul indica a abertura da catraca (autorização concedida), enquanto o LED vermelho indica que a catraca está fechada (acesso negado).

A comunicação entre o software de detecção facial, escrito em Python, e o Arduino é feita através de uma conexão serial, onde comandos são enviados para o Arduino controlar os LEDs.

## Estrutura do Projeto

- **`main.py`**: O ponto de entrada do sistema. Configura a captura de vídeo, realiza a detecção facial e envia comandos para o Arduino abrir ou fechar a catraca.
- **`images/`**: Diretório onde são armazenadas as imagens das pessoas que serão usadas para reconhecimento facial. O nome do arquivo da imagem é utilizado como o rótulo identificador.
- **`services/`**:
  - **`load_face_encodings.py`**: Carrega as codificações faciais conhecidas a partir das imagens armazenadas.
  - **`draw_results.py`**: Desenha os resultados da detecção facial no frame de vídeo.
  - **`buscar_imagens_e_criar_dicionario.py`**: Cria um dicionário associando os nomes das pessoas às suas imagens.
  - **`recognize_faces.py`**: Realiza o reconhecimento facial nos frames de vídeo usando as codificações faciais conhecidas.
  - **`match_face.py`**: Realiza a correspondência entre uma face detectada e as codificações conhecidas.
  - **`process_frame.py`**: Processa cada frame de vídeo para detectar e reconhecer faces.
  - **`get_first_valid_encoding.py`**: Extrai a primeira codificação facial válida de um diretório ou arquivo de imagem.
  - **`load_known_faces.py`**: Carrega as codificações faciais e os nomes das pessoas conhecidas a partir de diretórios.

## Comunicação com o Arduino

A comunicação com o Arduino é feita via conexão serial. Dependendo do resultado da autenticação facial, o sistema envia comandos específicos para o Arduino para ativar ou desativar os LEDs:

- **Comando '8'**: Enviado quando uma face conhecida é detectada. Este comando aciona o LED azul (porta 8) no Arduino, indicando que a "catraca" está aberta.
- **Comando '9'**: Enviado quando nenhum rosto conhecido é detectado. Este comando aciona o LED vermelho (porta 9) no Arduino, indicando que a "catraca" está fechada.

### Código do Arduino

O código do Arduino é responsável por receber os comandos via serial e controlar os LEDs:

```cpp
int ledPin8 = 8;  // Porta 8 (LED azul - catraca aberta)
int ledPin9 = 9;  // Porta 9 (LED vermelho - catraca fechada)

void setup() {
  Serial.begin(9600);
  pinMode(ledPin8, OUTPUT);
  pinMode(ledPin9, OUTPUT);
  digitalWrite(ledPin9, HIGH);  // Inicialmente, a catraca está fechada (LED vermelho aceso)
  digitalWrite(ledPin8, HIGH);  // LED azul apagado
}

void loop() {
  if (Serial.available()) {
    char command = Serial.read();

    if (command == '8') {
      digitalWrite(ledPin8, LOW);  // Acende o LED azul (abre a catraca)
      digitalWrite(ledPin9, HIGH); // Apaga o LED vermelho
    }
    else if (command == '9') {
      digitalWrite(ledPin8, HIGH); // Apaga o LED azul
      digitalWrite(ledPin9, LOW);  // Acende o LED vermelho (fecha a catraca)
    }
  }
}
```

## Instalação

1. Clone o repositório e acesse a pasta do projeto:

   ```bash
   git clone https://github.com/marco0antonio0/py-facial-detector-video
   ```

   ```bash
   cd py-facial-detector-video
   ```

2. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

3. Certifique-se de que você tenha o `opencv-python` e o `face_recognition` instalados.

## Uso

1. Adicione as imagens das pessoas que deseja reconhecer no diretório apropriado:

   ```bash
   ./images/
   ```

2. Conecte o Arduino via cabo serial e execute o script principal:

   ```bash
   python3 app.py
   ```

   Isso iniciará a captura de vídeo e o sistema tentará reconhecer as faces em tempo real, acionando os LEDs de acordo com o reconhecimento.

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
