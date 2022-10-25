
int motor1pin1 = 2;
int motor1pin2 = 3;
void setup() {
  Serial.begin(115200);
  pinMode(motor1pin1, OUTPUT);
  pinMode(motor1pin2, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
}
unsigned long messageTimestamp = 0;
void loop() {
  uint64_t now = millis();
  if (now - messageTimestamp > 0) {
    messageTimestamp = now;
   
    if (Serial.available() > 0){
      int x_mid;
      if (Serial.read() == 'X'){
        x_mid = Serial.parseInt();
      }
      if(x_mid == 1){
          stepperRight();
          Serial.println(x_mid);
        } else if(x_mid == 2){
          stepperLeft();
          Serial.println(x_mid);
        }else{
          stepperStop();
          Serial.println(x_mid);
        }
    }
  }
 
}
void stepperRight() {
  digitalWrite(motor1pin1, HIGH);  //for one direction
  digitalWrite(motor1pin2, LOW);
  delay(4);
  digitalWrite(motor1pin1, LOW);  //for stop
  digitalWrite(motor1pin2, LOW);
}
void stepperLeft() {
  digitalWrite(motor1pin1, LOW);  //for the other direction
  digitalWrite(motor1pin2, HIGH);
  delay(4);
  digitalWrite(motor1pin1, LOW);  //for stop
  digitalWrite(motor1pin2, LOW);
}
void stepperStop() {
  digitalWrite(motor1pin1, LOW);  //for stop
  digitalWrite(motor1pin2, LOW);
}
