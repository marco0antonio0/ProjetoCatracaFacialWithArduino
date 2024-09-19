int ledPin8 = 8;  // Porta 8
int ledPin9 = 9;  // Porta 9

void setup() {
  Serial.begin(9600);
  pinMode(ledPin8, OUTPUT);
  pinMode(ledPin9, OUTPUT);
  digitalWrite(ledPin9, HIGH);  // Desativa a porta 9 (se necessário)
  digitalWrite(ledPin8, HIGH);  // Desativa a porta 8
}

void loop() {
  if (Serial.available()) {
    char command = Serial.read();

    if (command == '8') {
      digitalWrite(ledPin8, LOW); // Ativa a porta 8
      digitalWrite(ledPin9, HIGH);  // Desativa a porta 9 (se necessário)
    } 
    else if (command == '9') {
      digitalWrite(ledPin8, LOW);  // Desativa a porta 8
      digitalWrite(ledPin9, HIGH); // Ativa a porta 9
    }
  }
}
