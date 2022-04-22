Run tests:<br>
python -m pytest --alluredir={report path} --base_url={Url} <br>
allure serve {report path}

About Vehicle API<br><br>
This API giving ability to control all main system of vehicle<br><br>
Vehicle API could be used for next actions
- Control Gear Shifter Stalks pins. Shifting Gears based on pins voltage values
- Control Acceleration Pedal. Sending Torque to Motor based on pedal position
- Control Brake Position based on signals from Braking System
- Control Battery state based on info from Battery<br>

PINS API<br>

GET /api/pins - returns all pins voltage<br>
GET /api/pins/PinId - returns one pin voltage<br>
POST /api/pins/PinId/update_pin - set voltage on given pin. Provide `form-data` with field `Voltage` and value to set<br>
POST /api/pins/update_pins - set voltage on few given pins with one request. Provide `json` with fields to set<br>

SIGNALS API<br>

GET /api/signals - returns all signals values<br>
GET /api/signals/{SigId} - returns one signal value