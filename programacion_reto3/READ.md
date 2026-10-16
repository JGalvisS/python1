# Smart Home Control

## Student Information

- **Student:** Jessica Katherine Galvis Silva
- **Group:** 213023_493
- **Program:** Systems Engineering
- **Source code:** Original work

## Project Description

Smart Home Control is a desktop application built with Python and Tkinter. Its graphical interface lets users configure and control lightbulbs, curtains, and a thermostat. The interface validates user input and sends the selected values to the central controller.

## Project Structure

```text
programacion_reto3/
├── central_controller.py  # Coordinates device actions and system status
├── curtain.py             # Curtain device class
├── device.py              # Base device class
├── lightbulb.py           # Lightbulb device class
├── main.py                # Tkinter interface and application entry point
├── thermostat.py          # Thermostat device class
└── README.md              # Project documentation
```

The project separates the interface, controller, and device classes:

- **`main.py`** builds the GUI, validates inputs, and calls the controller.
- **`central_controller.py`** coordinates device configuration, global actions, and status requests.
- **`device.py`** provides the base device class.
- **`curtain.py`**, **`lightbulb.py`**, and **`thermostat.py`** implement the individual device classes.

## Features

- Select a room for each device.
- Turn individual devices on or off.
- Configure lightbulb mode and brightness.
- Configure curtain and thermostat schedules using 24-hour `HH:MM` format.
- Set the thermostat temperature.
- Turn all devices on or off.
- Display the system status.

## Requirements

- Python 3.9 or later is recommended.
- Tkinter, normally included with the standard Python installation.

No third-party Python packages are required.

## How to Run

1. Open PowerShell or the VS Code terminal.
2. Change to the project directory:

   ```powershell
   cd ~\programacion_reto3
   ```

3. Run the application:

   ```powershell
   py main.py
   ```

   If `py` is not available, try:

   ```powershell
   python main.py
   ```

## Input Notes

- Schedule fields accept 24-hour times, such as `09:00` or `18:30`.
- Lightbulb brightness must be between `0` and `100`.
- Lightbulb mode must be `warm` or `white`.
- Thermostat temperature must be between `0` and `35 °C`.
- Empty optional configuration fields are passed to the controller as unspecified values.