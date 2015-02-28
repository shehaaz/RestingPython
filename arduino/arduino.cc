#include <PinChangeInt.h>
#include <eHealth.h>


char recv[128];
float parameter = -0.1;
uint8_t cont = 0;


void setup()
{
  Serial.begin(9600);

  eHealth.initPulsioximeter();

  PCintPort::attachInterrupt(6, readPulsioximeter, RISING);
  delay(1000);

}

void loop()
{
  while (Serial.available()>0) {
  }
  // Enters in command mode
  Serial.print("$$$");
  check();
  Serial.print("factory RESET\r");
  check();

  Serial.print("set wlan channel 0\r");
  check();
  Serial.print("set wlan ssid shehaaz\r");
  check();
  Serial.print("set wlan phrase comcastsucks\r");
  check();
  // Sets DHCP and TCP protocol
  Serial.print("set ip dhcp 1\r");
  check();
  Serial.print("set ip protocol 1\r");
  check();

  Serial.print("set wlan join 1\r");
  check();
  Serial.print("join shehaaz\r");
  check();

  Serial.print("set ip proto 18\r");
  check();

  Serial.print("set ip host APP_REMOTE_IP\r");
  check();
  Serial.print("set ip remote 5000\r");
  check();
  Serial.print("set com remote GET$/data/\r");
  check(); //removed 3 in server3

  Serial.print("set uart mode 2\r");
  check();
  Serial.print("set sys trigger 1\r");
  check();
  Serial.print("set sys sleep 10\r");
  check();

  Serial.print("set sys auto 5\r");
  check();

  Serial.print("set comm timer 2500\r");
  check();
  Serial.print("open\r");
  check();


  while(1){

    int airFlow = eHealth.getAirFlow();
    float temperature = eHealth.getTemperature();
    float conductance = eHealth.getSkinConductance();
    float resistance = eHealth.getSkinResistance();
    float conductanceVol = eHealth.getSkinConductanceVoltage();
    int BPM = eHealth.getBPM();
    int SPO2 = eHealth.getOxygenSaturation();
    uint8_t pos = eHealth.getBodyPosition();

    float ECG = eHealth.getECG();



    Serial.print(int(temperature));
    Serial.print(",");
    Serial.print(int(BPM));
    Serial.print(",");
    Serial.print(int(SPO2));
    Serial.print("\n");

    delay(250);



  }
}

void check(){
  cont=0;
  delay(500);
  while (Serial.available()>0)
  {
    recv[cont]=Serial.read();
    delay(10);
    cont++;
  }
  recv[cont]='\0';
  Serial.println(recv);
  Serial.flush();
  delay(100);
}



////Include always this code when using the pulsioximeter sensor

void readPulsioximeter(){

  cont ++;

  if (cont == 50) { //Get only one of 50 measures to reduce the latency
    eHealth.readPulsioximeter();
    cont = 0;
  }
}
