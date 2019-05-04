ee250 Final project:
Richard Hernandez, Jae shin

The code is tested and fully functional. 
It first imports all the required pakages and and then initializes all the variables. 

The http messages to update the desired_temp is send from mailClient.py and supported by mailboxTools.py (included in the repository). If a valid command is input it sends the temp to rpi-jaeishin:4250.

When entering or exiting wind mode the code sends an mqtt message to whoever is listening on "rpi-jaeishin/HVAC". mqttServer.py is also in the repo and is a test file to listen recieve the mqtt message. 

There is a function to read the indoor temp using the grove temperature sensor connected to the grove pi, and a function to get the outdoor temp through an API. 

The main() function has all the logic. This changes the mode, sounds the buzzer, turns on the lcd blacklight, and allows you to change the desired temp using the rotary encoder. 

The startup() function was provided to help with threading all the different processes going on when the program is run.

To run the program run:
	
	#Run on rpi
	python3 final.py -p 123

	#Run on VM
	python3 mailClient.py -a rpi-jaeishin:4250 -p 123 -u test

I used the documentation on this website as well as the book that comes
with the grovepi to implement the hardware.
->http://wiki.seeedstudio.com/GrovePi_Plus/

I used this link to format the strings to print on the screen and on the LCD
->https://pyformat.info



