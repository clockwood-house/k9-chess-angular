# Mini K9 Controller
Code and configuration files for a portable Siri like remote presence robot!

The root directory contains some frequently requested design documents and plans as PDFs, plus the index.html that defines the HTML that is the root page of the end user app.

# Directory Structure

## conversation
JSON configuration files for IBM Watson Assistant workspaces

## css
CSS files for end user interface largely generated and maintained by Ionic

## img
Visuals for end user interface, includes default camera image and SVG for Sensors tab.  Some reference images of the hero prop are also included.

## js
The AngularJS JavaScript that is the bulk of the end user application function

File | Description
---  | ---
app.js | Basic structure of the application modules plus some low level functions
controllers.js | Each tab has its own controller in this file that respondes to user events and manipulates the model.  This separation of event handling and model manipulation makes maintenance and problem diagnosis easier.
directives.js | There are custom directives for the locked/unlocked icon on each tab (that shows whether communications between browser and dog are working in both directions) and the joystick on the Motors tab.  These directives make the HTML much easier to understand and maintain.
services.js | The shared services maintain a model of the state of the dog in the front end app; they also support the creation of sockets between the app and dog and the standardisation of messages flowing over that connection.  The translation between sensor readings and the SVG world are also calculated here for display on the sensors page.

## node-RED
This directory contains the flows to control K9.  It provides the means to flow information between the various elements of the dog and co-ordinates movement and speech.  It also contains the definition of the dashboard to show on K9's screen.

## python
This directory contains the python programs that use the Adafruit PWM Servo Driver and RoboClaw PID MotorController to make K9 move. A harness is included to generate sensor data to simulare collisions.  There are also some simple scripts to interface to Watson Conversation and STT (and to K9's espeak TTS)

Program | Description
---  | ---
K9PythonController.py | RoboClaw based Motor Controller
status.py | Sends K9's current state to node-RED (and browser) as JSON string every 200ms
ttsrobot.py | Uses Snowboy, Watson STT, Conversation and TTS - a bit Alexa like :+)

## script
Simple deployment scripts to move code into right place on the Pi

## snap
Standard JavaScript library used to integrate SVG and AngularJS on the Sensors page

## templates
This directory contains the HTML for each of the tabs of the user interface (including the definition of the tabs themselves!).  Keeping the html for each tab separately simplifies testing and maintenance.
