#include <Servo.h>
#include "LiquidCrystal.h"

const byte numChars = 32;
const byte maxServos = 9;

char receivedChars[numChars];
char tempChars[numChars];        // temporary array for use when parsing
Servo servos[maxServos];
int n_servos = 0;

      // variables to hold the parsed data
char cmd[numChars] = {0};
char payloads[10][32];
int i = -1;
int n_payloads = 0;

boolean newData = false;

// if you are using an LCD comment the first line and uncomment and modify the second line
LiquidCrystal lcd(-1, -1, -1, -1, -1, -1);  // ! FAKE lcd (can't initialize without constructor)
//LiquidCrystal lcd(12, 11, 5, 4, 3, 2);      // ! REAL lcd (modify with your pins)
// when you are NOT using an lcd uncomment the first line and comment the second

//============

void setup() {
    Serial.begin(9600);
    Serial.println("This program expects pieces of data - text: a string (command), an sequence of integers (payload)");
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
          pinMode(atoi(payloads[0]), atoi(payloads[1]));
        } else if(strcmp(cmd,"digitalWrite") == 0){
          digitalWrite(atoi(payloads[0]), atoi(payloads[1]));
        } else if(strcmp(cmd,"digitalRead") == 0){
          Serial.println(digitalRead(atoi(payloads[0])));
        } else if(strcmp(cmd,"analogRead") == 0){
          Serial.println(analogRead(atoi(payloads[0])));
        } else if(strcmp(cmd,"analogWrite") == 0){
          analogWrite(atoi(payloads[0]), atoi(payloads[1]));
        } else if(strcmp(cmd,"servoAttach") == 0){
          if(n_servos < maxServos){
            Servo newServo;
            newServo.attach(atoi(payloads[0]));
            servos[n_servos] = newServo;
            Serial.println(n_servos);
            n_servos ++;
          } else{
            Serial.println(-1);
          }      
        } else if(strcmp(cmd,"servoWrite") == 0){
          servos[atoi(payloads[0])].write(atoi(payloads[1])); // pin is the servo position in the array
        } else if(strcmp(cmd,"tone") == 0){
          tone(atoi(payloads[0]), atoi(payloads[1]), atoi(payloads[2]));
        } else if(strcmp(cmd,"noTone") == 0){
          noTone(atoi(payloads[0]));
        } else if(strcmp(cmd,"lcdCreate") == 0){
          // LiquidCrystal lcd(atoi(payloads[0]), atoi(payloads[1]),atoi(payloads[2]),atoi(payloads[3]),atoi(payloads[4]), atoi(payloads[5])); // doesn't work
        } else if(strcmp(cmd,"lcdBegin") == 0){
          lcd.begin(atoi(payloads[0]), atoi(payloads[1]));
        } else if(strcmp(cmd,"lcdPrint") == 0){
          lcd.print(payloads[0]);
        } else if(strcmp(cmd,"lcdSetCursor") == 0){
          lcd.setCursor(atoi(payloads[0]), atoi(payloads[1]));
        } else if(strcmp(cmd,"lcdClear") == 0){
          lcd.clear();
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

    i = -1;
    strtokIndx = strtok(NULL, ","); // this continues where the previous call left off
    while(strtokIndx != NULL){
      i++;
      strcpy(payloads[i], strtokIndx);
      strtokIndx = strtok(NULL, ",");
    }
    n_payloads = i + 1;
}

//============

void showParsedData() {
    if(strcmp(cmd, "servoWrite") == 0){
      Serial.println("CMD " + String(cmd) + " NAME " + String(payloads[0]) + " PAYLOAD " + String(payloads[1]));
    } else if(strcmp(cmd, "tone") == 0){
      Serial.println("CMD " + String(cmd) + " PIN " + String(payloads[0]) + " PITCH " + String(payloads[1]) + " TIME " + String(payloads[2]));
    }else{
      Serial.println("CMD " + String(cmd) + " PIN " + String(payloads[0]) + " PAYLOAD " + String(payloads[1]));
    }
}
