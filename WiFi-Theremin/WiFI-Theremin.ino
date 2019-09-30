#include <SPI.h>
#include <ESP8266WiFi.h>

#define LED D1

const char* SSID = "<ssid>";
const char* PASS = "<***>";

int frequency=2600;
const int piezo=13;


int potPin = 2;

int dt1[3] = {697, 770, 852, 941};
int dt2[3] = {1209, 1336, 1477, 1633}


void setup(){
    Serial.begin(115200);
    WiFi.begin(SSID, PASS);

    Serial.println();
    Serial.print("Connecting to ");
    Serial.println(SSID);

    int i = 0;
    
    while(WiFi.status() != WL_CONNECTED){
        delay(1000);
        Serial.print(++i); Serial.print('.');
    }
    Serial.println('\n');
        Serial.println('\n');
    Serial.println("Connection established!");  
    Serial.print("IP address:\t");
    Serial.println(WiFi.localIP());  

    pinMode(LED, OUTPUT);
}

void loop(){
    Serial.print("RSSI: ");
    Serial.println(WiFi.RSSI());
    // delay(100);
    int dt = round(map(WiFi.RSSI(),-90,-30,0,15);
    Serial.println("dt: " + dt);
    
    switch(dt){
        case 0:
            tone(piezo, dt1[0]);
            tone(piezo, dt2[0]);
            break;
        case 1:
            tone(piezo, dt1[0]);
            tone(piezo, dt2[1]);
            break;
        case 2:
            tone(piezo, dt1[0]);
            tone(piezo, dt2[2]);
            break;
        case 3:
            tone(piezo, dt1[0]);
            tone(piezo, dt2[3]);
            break;
        case 4:
            tone(piezo, dt1[1]);
            tone(piezo, dt2[0]);
            break;
        case 5:
            tone(piezo, dt1[1]);
            tone(piezo, dt2[1]);
            break;
        case 6:
            tone(piezo, dt1[1]);
            tone(piezo, dt2[2]);
            break;
        case 7:
            tone(piezo, dt1[1]);
            tone(piezo, dt2[3]);
            break;
        case 8:
            tone(piezo, dt1[2]);
            tone(piezo, dt2[0]);
            break;
        case 9:
            tone(piezo, dt1[2]);
            tone(piezo, dt2[1]);
            break;
        case 10:
            tone(piezo, dt1[2]);
            tone(piezo, dt2[2]);
            break;
        case 11:
            tone(piezo, dt1[2]);
            tone(piezo, dt2[3]);
            break;
        case 12:
            tone(piezo, dt1[3]);
            tone(piezo, dt2[0]);
            break;
        case 13:
            tone(piezo, dt1[3]);
            tone(piezo, dt2[1]);
            break;
        case 14:
            tone(piezo, dt1[3]);
            tone(piezo, dt2[2]);
            break;
        case 15:
            tone(piezo, dt1[3]);
            tone(piezo, dt2[3]);
            break;
        default:
            break;    
    }
    // tone(piezo, frequency);
    delay(10);
    
}
