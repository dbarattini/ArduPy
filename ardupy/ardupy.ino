#include <Servo.h>

const byte numChars = 32;
const byte maxServos = 9;

char receivedChars[numChars];
char tempChars[numChars];        // temporary array for use when parsing
Servo servos[maxServos];
int n_servos = 0;

      // variables to hold the parsed data
char cmd[numChars] = {0};
int pin = 0;
int payload = 0;
int pitch = -1;

boolean newData = false;

//============

void setup() {
    Serial.begin(9600);
    Serial.println("This program expects 3 pieces of data - text: a string (command), an integer (pin) and an integer (payload)");
    Serial.println("Enter data in this style <pinMode, 13, 1>  ");
    Serial.println("Input -> 0 | Output -> 1 | Low -> 0 | High -> 1");
}

//============

void loop() {
    recvWithStartEndMarkers();
    if (newData == true) {
        strcpy(tempChars, receivedChars);
            // this temporary copy is necessary to protect the original data
            //   because strtok() used in parseData() replaces the commas with \0
        parseData();
        showParsedData();
        
        if(strcmp(cmd,"pinMode") == 0){
          pinMode(pin, payload);
        } else if(strcmp(cmd,"digitalWrite") == 0){
          digitalWrite(pin, payload);
        } else if(strcmp(cmd,"digitalRead") == 0){
          Serial.println(digitalRead(pin));
        } else if(strcmp(cmd,"analogRead") == 0){
          Serial.println(analogRead(pin));
        } else if(strcmp(cmd,"analogWrite") == 0){
          analogWrite(pin, payload);
        } else if(strcmp(cmd,"servoAttach") == 0){
          if(n_servos < maxServos){
            Servo newServo;
            newServo.attach(pin);
            servos[n_servos] = newServo;
            Serial.println(n_servos);
            n_servos ++;
          } else{
            Serial.println(-1);
          }      
        } else if(strcmp(cmd,"servoWrite") == 0){
          servos[pin].write(payload); // pin is the servo position in the array
        } else if(strcmp(cmd,"tone") == 0){
          if(pitch == -1){  // first message containing pitch as payload
            pitch = payload;
          } else{           // second message containing time as payload
            tone(pin, pitch, payload);
            pitch = -1;
          }
        } else if(strcmp(cmd,"noTone") == 0){
          noTone(pin);
        }
        newData = false;
    }
}

//============

void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;

    while (Serial.available() > 0 && newData == false) {
        rc = (char) Serial.read();

        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }

        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}

//============

void parseData() {      // split the data into its parts

    char * strtokIndx; // this is used by strtok() as an index

    strtokIndx = strtok(tempChars,",");      // get the first part - the string
    strcpy(cmd, strtokIndx); // copy it to cmd
 
    strtokIndx = strtok(NULL, ","); // this continues where the previous call left off
    pin = atoi(strtokIndx);     // convert this part to an integer

    strtokIndx = strtok(NULL, ",");
    payload = atoi(strtokIndx);     // convert this part to an integer

}

//============

void showParsedData() {
    if(strcmp(cmd, "servoWrite") == 0){
      Serial.println("CMD " + String(cmd) + " NAME " + String(pin) + " PAYLOAD " + String(payload));
    } else{
      Serial.println("CMD " + String(cmd) + " PIN " + String(pin) + " PAYLOAD " + String(payload));
    }
}
