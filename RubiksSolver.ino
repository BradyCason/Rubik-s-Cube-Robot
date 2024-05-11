#include <Arduino.h>
#include "A4988.h"

// -------------------------------------------------------------------
//
// PASTE MOVES HERE
String moves[] = {"R1", "U2", "D2", "R2", "L2", "U2", "D2", "L2"};
int numMoves = 8;
//
//
// -------------------------------------------------------------------
 
int StepR = 13;
int DireR  = 12;
int StepL = 5;
int DireL  = 4;
int StepU = 9;
int DireU  = 8;
int StepD = 11;
int DireD  = 10;
int StepF = 3;
int DireF  = 2;
int StepB = 7;
int DireB  = 6;

int MS1 = 13;
int MS2 = 14;
int MS3 = 15;
int Sleep = 16;
 
//Motor Specs
const int spr = 200; //Steps per revolution
int RPM = 150; //Motor Speed in revolutions per minute
int Microsteps = 1; //Stepsize (1 for full steps, 2 for half steps, 4 for quarter steps, etc)

int turnDelay = 50;
 
//Providing parameters for motor control
A4988 stepperR(spr, DireR, StepR, MS1, MS2, MS3);
A4988 stepperL(spr, DireL, StepL, MS1, MS2, MS3);
A4988 stepperU(spr, DireU, StepU, MS1, MS2, MS3);
A4988 stepperB(spr, DireB, StepB, MS1, MS2, MS3);
A4988 stepperD(spr, DireD, StepD, MS1, MS2, MS3);
A4988 stepperF(spr, DireF, StepF, MS1, MS2, MS3);
 
void setup() {
  Serial.begin(9600);
  pinMode(StepR, OUTPUT); //Step pin as output
  pinMode(StepL, OUTPUT); //Step pin as output
  pinMode(StepU, OUTPUT); //Step pin as output
  pinMode(StepD, OUTPUT); //Step pin as output
  pinMode(StepF, OUTPUT); //Step pin as output
  pinMode(StepB, OUTPUT); //Step pin as output
  pinMode(DireR,  OUTPUT); //Direcction pin as output
  pinMode(DireL,  OUTPUT); //Direcction pin as output
  pinMode(DireU,  OUTPUT); //Direcction pin as output
  pinMode(DireD,  OUTPUT); //Direcction pin as output
  pinMode(DireF,  OUTPUT); //Direcction pin as output
  pinMode(DireB,  OUTPUT); //Direcction pin as output
  digitalWrite(StepR, LOW); // Currently no stepper motor movement
  digitalWrite(StepL, LOW); // Currently no stepper motor movement
  digitalWrite(StepU, LOW); // Currently no stepper motor movement
  digitalWrite(StepD, LOW); // Currently no stepper motor movement
  digitalWrite(StepB, LOW); // Currently no stepper motor movement
  digitalWrite(StepF, LOW); // Currently no stepper motor movement
  digitalWrite(DireR, LOW);
  digitalWrite(DireL, LOW);
  digitalWrite(DireU, LOW);
  digitalWrite(DireD, LOW);
  digitalWrite(DireF, LOW);
  digitalWrite(DireB, LOW);

  // Set target motor RPM to and microstepping setting
  stepperR.begin(RPM, Microsteps);
  stepperL.begin(RPM, Microsteps);
  stepperU.begin(RPM, Microsteps);
  stepperD.begin(RPM, Microsteps);
  stepperB.begin(RPM, Microsteps);
  stepperF.begin(RPM, Microsteps);

  move(moves);
}
 
void loop() {
    
}

void move(String moves[]){
  for (int i = 0; i < numMoves; i++){
    String move = moves[i];
    if (move == "R1" || move == "r"){
      R();
    }
    else if (move == "R3" || move == "r'"){
      RPrime();
    }
    else if (move == "R2" || move == "r2"){
      R2();
    }
    else if (move == "L1" || move == "l"){
      L();
    }
    else if (move == "L3" || move == "l'"){
      LPrime();
    }
    else if (move == "L2" || move == "l2"){
      L2();
    }
    else if (move == "U1" || move == "u2"){
      U();
    }
    else if (move == "U3" || move == "u'"){
      UPrime();
    }
    else if (move == "U2" || move == "u2"){
      U2();
    }
    else if (move == "F1" || move == "f"){
      Fturn();
    }
    else if (move == "F3" || move == "f'"){
      FPrime();
    }
    else if (move == "F2" || move == "f2"){
      F2();
    }
    else if (move == "D1" || move == "d"){
      D();
    }
    else if (move == "D3" || move == "d'"){
      DPrime();
    }
    else if (move == "D2" || move == "d2"){
      D2();
    }
    else if (move == "B1" || move == "b"){
      B();
    }
    else if (move == "B3" || move == "b'"){
      BPrime();
    }
    else if (move == "B2" || move == "b2"){
      B2();
    }
    
  }
}

// R ---------------------------------------------------
void R(){
  stepperR.rotate(90);
  delay(turnDelay);
}

void RPrime(){
  stepperR.rotate(-90);
  delay(turnDelay);
}

void R2(){
  stepperR.rotate(180);
  delay(turnDelay);
}

// L ---------------------------------------------------
void L(){
  stepperL.rotate(90);
  delay(turnDelay);
}

void LPrime(){
  stepperL.rotate(-90);
  delay(turnDelay);
}

void L2(){
  stepperL.rotate(180);
  delay(turnDelay);
}

// U ---------------------------------------------------
void U(){
  stepperU.rotate(90);
  delay(turnDelay);
}

void UPrime(){
  stepperU.rotate(-90);
  delay(turnDelay);
}

void U2(){
  stepperU.rotate(180);
  delay(turnDelay);
}

// F ---------------------------------------------------
void Fturn(){
  stepperF.rotate(90);
  delay(turnDelay);
}

void FPrime(){
  stepperF.rotate(-90);
  delay(turnDelay);
}

void F2(){
  stepperF.rotate(180);
  delay(turnDelay);
}

// D ---------------------------------------------------
void D(){
  stepperD.rotate(90);
  delay(turnDelay);
}

void DPrime(){
  stepperD.rotate(-90);
  delay(turnDelay);
}

void D2(){
  stepperD.rotate(180);
  delay(turnDelay);
}

// B ---------------------------------------------------
void B(){
  stepperB.rotate(90);
  delay(turnDelay);
}

void BPrime(){
  stepperB.rotate(-90);
  delay(turnDelay);
}

void B2(){
  stepperB.rotate(180);
  delay(turnDelay);
}

