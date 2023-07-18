void setup() {
  Serial.begin(9600);     // Sets up serial communication
  
  pinMode(22, OUTPUT);    // Sets the digital pin 22 as output
  pinMode(23, OUTPUT);    // Sets the digital pin 23 as output
  pinMode(24, OUTPUT);    // Sets the digital pin 24 as output
  pinMode(25, OUTPUT);    // Sets the digital pin 25 as output
  pinMode(26, OUTPUT);    // Sets the digital pin 26 as output
  pinMode(27, OUTPUT);    // Sets the digital pin 27 as output
  pinMode(28, OUTPUT);    // Sets the digital pin 28 as output
  pinMode(29, OUTPUT);    // Sets the digital pin 29 as output
  pinMode(30, OUTPUT);    // Sets the digital pin 30 as output
  pinMode(31, OUTPUT);    // Sets the digital pin 31 as output
}

void loop() {
  Serial.println("\nSerial connection successful!");
  
  while (Serial.available() == 0) {
  // Only prompts user for input once between inputs
  }
  
  String input = Serial.readString();
  input.trim();
  Serial.println(input);

  
// ALLs
  if(input.indexOf("all high") > -1){
      // Turns on voltage for all segmented electrodes at once

      // Removes paths for ground
      digitalWrite(23, LOW);
      digitalWrite(25, LOW);
      digitalWrite(27, LOW);
      digitalWrite(29, LOW);
      digitalWrite(31, LOW);
      delay(200);

      // Connects paths for voltage
      digitalWrite(22, HIGH);
      digitalWrite(24, HIGH);
      digitalWrite(26, HIGH);
      digitalWrite(28, HIGH);
      digitalWrite(30, HIGH);

      Serial.println("Voltage set to high on all arduino controlled electrodes.");
  }

  if(input.indexOf("all low") > -1){
    // Connects all segmented electrodes to ground at once

    // Removes paths for voltage
    digitalWrite(22, LOW);
    digitalWrite(24, LOW);
    digitalWrite(26, LOW);
    digitalWrite(28, LOW);
    digitalWrite(30, LOW);
    delay(200);

    // Connects all electrodes to ground
    digitalWrite(23, HIGH);
    digitalWrite(25, HIGH);
    digitalWrite(27, HIGH);
    digitalWrite(29, HIGH);
    digitalWrite(31, HIGH);

    Serial.println("Voltage set to low on all arduino controlled electrodes.");
  }


  if(input.indexOf("all off") > -1){
    // Drains voltage and removes voltage paths for all segmented electrodes at once

    Serial.println("Powering off all arduino controlled electrodes...");

    // Removes paths for voltage
    digitalWrite(22, LOW);
    digitalWrite(24, LOW);
    digitalWrite(26, LOW);
    digitalWrite(28, LOW);
    digitalWrite(30, LOW);
    delay(200);

    // Connects all electrodes to ground to remove any voltage
    digitalWrite(23, HIGH);
    digitalWrite(25, HIGH);
    digitalWrite(27, HIGH);
    digitalWrite(29, HIGH);
    digitalWrite(31, HIGH);
    delay(200);

    // Removes paths for ground
    digitalWrite(23, LOW);
    digitalWrite(25, LOW);
    digitalWrite(27, LOW);
    digitalWrite(29, LOW);
    digitalWrite(31, LOW);

    Serial.println("All arduino controlled electrodes powered off.");
  }


// Electrode set 'a'
  if(input.indexOf("a high") > -1){
    digitalWrite(31, LOW); // Sets the digital pin 31 to off;
    delay(200);
    digitalWrite(30, HIGH); // Sets the digital pin 30 to on;
    Serial.println("Voltage set to high on electrode set 'a.'");
  }

  if(input.indexOf("a low") > -1){
    digitalWrite(30, LOW); // Sets the digital pin 30 to off;
    delay(200);
    digitalWrite(31, HIGH); // Sets the digital pin 31 to on;
    Serial.println("Voltage set to low on electrode set 'a.'");
  }

  if(input.indexOf("a off") > -1){
    digitalWrite(30, LOW); // Sets the digital pin 30 to off;
    delay(200);
    digitalWrite(31, HIGH); // Sets the digital pin 31 on;
    delay(400);
    digitalWrite(31, LOW); // Sets the digital pin 31 off;
    Serial.println("Voltage turned off for electrode set 'a.'");
  }


// Electrode set 'b'
  if(input.indexOf("b high") > -1){
    digitalWrite(29, LOW); // Sets the digital pin 29 to off;
    delay(200);
    digitalWrite(28, HIGH); // Sets the digital pin 28 to on;
    Serial.println("Voltage set to high on electrode set 'b.'");
  }

  if(input.indexOf("b low") > -1){
    digitalWrite(28, LOW); // Sets the digital pin 28 to off;
    delay(200);
    digitalWrite(29, HIGH); // Sets the digital pin 29 to on;
    Serial.println("Voltage set to low on electrode set 'b.'");
  }

  if(input.indexOf("b off") > -1){
    digitalWrite(28, LOW); // Ensures the digital pin 28 is off;
    delay(200);
    digitalWrite(29, HIGH); // Sets the digital pin 29 on;
    delay(400);
    digitalWrite(29, LOW); // Sets the digital pin 29 off;
    Serial.println("Voltage turned off for electrode set 'b.'");
  }


// Electrode set 'c'
  if(input.indexOf("c high") > -1){
    digitalWrite(27, LOW); // Sets the digital pin 27 to off;
    delay(200);
    digitalWrite(26, HIGH); // Sets the digital pin 26 to on;
    Serial.println("Voltage set to high on electrode set 'c.'");
  }

  if(input.indexOf("c low") > -1){
    digitalWrite(26, LOW); // Sets the digital pin 26 to off;
    delay(200);
    digitalWrite(27, HIGH); // Sets the digital pin 27 to on;
    Serial.println("Voltage set to low on electrode set 'c.'");
  }

  if(input.indexOf("c off") > -1){
    digitalWrite(26, LOW); // Sets the digital pin 26 to off;
    delay(200);
    digitalWrite(27, HIGH); // Sets the digital pin 27 to on;
    delay(400);
    digitalWrite(27, LOW); // Sets the digital pin 27 to off
    Serial.println("Voltage turned off for electrode set 'c.'");
  }


// Electrode set 'd'
  if(input.indexOf("d high") > -1){
    digitalWrite(25, LOW); // Sets the digital pin 25 to off;
    delay(200);
    digitalWrite(24, HIGH); // Sets the digital pin 24 to on;
    Serial.println("Voltage set to high on electrode set 'd.'");
  }

  if(input.indexOf("d low") > -1){
    digitalWrite(24, LOW); // Sets the digital pin 24 to off];
    delay(200);
    digitalWrite(25, HIGH); // Sets the digital pin 25 to on;
    Serial.println("Voltage set to low on electrode set 'd.'");
  }

  if(input.indexOf("d off") > -1){
    digitalWrite(24, LOW); // Sets the digital pin 24 to off];
    delay(200);
    digitalWrite(25, HIGH); // Sets the digital pin 25 to on;
    delay(400);
    digitalWrite(25, LOW); // Sets the digital pin 25 to off;
    Serial.println("Voltage turned off for electrode set 'd.'");
  }


// Electrode set 'e'
  if(input.indexOf("e high") > -1){
    digitalWrite(23, LOW); // Sets the digital pin 23 to off;
    delay(200);
    digitalWrite(22, HIGH); // Sets the digital pin 22 on;
    Serial.println("Voltage set to high on electrode set 'e.'");
  }

  if(input.indexOf("e low") > -1){
    digitalWrite(22, LOW); // Sets the digital pin 22 to off;
    delay(200);
    digitalWrite(23, HIGH); // Sets the digital pin 23 to on;
    Serial.println("Voltage set to low on electrode set 'e.'");
  }

  if(input.indexOf("e off") > -1){
    digitalWrite(22, LOW); // Sets digital pin 22 to off;
    delay(200);
    digitalWrite(23, HIGH); // Sets digital pin 23 to on;
    delay(400);
    digitalWrite(23, LOW); // Sets digital pin 23 off;
    Serial.println("Voltage turned off for electrode set 'e.'");
  }

}