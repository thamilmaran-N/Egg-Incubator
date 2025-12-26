## Project Overview

This project implements an automatic egg incubator that maintains the optimal temperature (37°C–38°C) and humidity (50%–60%) required for egg hatching.
The system uses a Raspberry Pi Pico W to monitor environmental conditions using a DHT22 sensor, control a heating bulb through a relay, provide audible alerts via a buzzer, display real-time values on an I2C LCD, and log data to ThingSpeak for remote monitoring.

## Objectives
- Automatically maintain incubation temperature and humidity
- Minimize manual intervention during incubation
- Provide real-time local monitoring using LCD
- Enable remote monitoring through ThingSpeak
- Reduce power consumption through controlled actuation
- Provide alerts when conditions go out of range

## Tools & Software Used
- MicroPython – Programming language
- Thonny IDE – Code development and upload
- ThingSpeak – Cloud-based data logging
- Wokwi Simulator – Circuit and logic simulation

## Hardware Components
- 1.Microcontroller	Raspberry Pi Pico W (RP2040)
- 2.Temperature & Humidity Sensor	DHT22
- 3.Relay Module 5V Single Channel
- 4.LCD Display	16×2 I2C
- 5.Heating Element	40W Incandescent Bulb
- 6.Buzzer	5V
- 7.Power Supply 5V Adapter
- 8.Breadboard
- 9.Connecting Wires

## Pin Connections
<img width="973" height="424" alt="image" src="https://github.com/user-attachments/assets/16412cf1-f284-407a-9374-5c373ec262dc" />

## Working Principle
- The DHT22 sensor continuously measures temperature and humidity.
- If temperature < 37°C, the relay activates the bulb for heating.
- If temperature > 38°C, the bulb is turned OFF and the buzzer alerts.
- Humidity levels outside 50–60% trigger buzzer alerts.
- Real-time values and alerts are displayed on the I2C LCD.
- Temperature and humidity data are periodically uploaded to ThingSpeak via WiFi.

## Output
<img width="982" height="606" alt="image" src="https://github.com/user-attachments/assets/3d7e3afe-d419-4540-95db-ce133334d95e" />
<img width="647" height="793" alt="image" src="https://github.com/user-attachments/assets/d1438355-0f97-4e86-b44c-378db05942b6" />

## Outcome
- Achieved precise control of temperature and humidity
- Reduced manual monitoring effort
- Enabled real-time and remote monitoring
- Demonstrated a cost-effective and scalable incubation solution
- Suitable for small-scale poultry farming and academic use

## Applications
- Poultry farming
- Academic and laboratory experiments
- Wildlife conservation hatcheries
- Smart agriculture systems
- IoT-based environmental monitoring
