
/*********************************************************************
ESP8266ARS: Arduino project for ALBA Remote Sensors base on ESP8266. 

Author(s): Roberto J. Homs Puron <rhoms@cells.es>, 
           Alberto Rubio Garcia <arubio@cells.es>
           Sergio Astorga Sanchez <sastorga@cells.es>
        
Copyright (C) 2017, CELLS / ALBA Synchrotron

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

**************************************************************/

#ifndef MAX31855_H
#define MAX31855_H

#include <SPI.h>
#include <Wire.h>

#define MAX_FREQ 8000000 // 8MHZ
#define SPI_MODE SPI_MODE0
#define BITS_ORDER MSBFIRST

class BasicCS{
  public:
    BasicCS() {};
    BasicCS(int gpio);
    void setHigh() {setValue(true);};
    void setLow() {setValue(false);};
  private:
    virtual void setValue(bool value);
    int gpio;
    
};

class Pcf8574CS: public BasicCS{
  public:
    Pcf8574CS(int addr, uint8_t pin);
  private:
    int addr;
    uint8_t pin;
    void setValue(bool value);
};

class MAX31855{
  public:
    MAX31855(BasicCS *cs, int8_t sck, int8_t miso);
    MAX31855(BasicCS *cs);
   
    double readThermocouple();
    double readInternal();
    bool isShortVcc();
    bool isShortGnd();
    bool isOpenCircuit();
    bool isFault(); 
    
  private:
    BasicCS *cs;
    int8_t sck, miso;
    double thermocouple, internal;
    bool short_vcc;
    bool short_gnd;
    bool open_circuit;
    bool fault;
    void updateValues();
  
  
};
#endif
