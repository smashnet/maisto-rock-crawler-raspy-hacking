#Maisto Rock Crawler PCB

Since I couldn't find something on the internet about this PCB I just grabbed my multimeter and found out on my own:

| Pin | Function |
| --- | -------- |
| GND | Ground |
| VCC | 6V from battery pack |
| Ant | Antenna |
| M1  | Motor for forward and backward driving (one on the front axis and one in the rear) |
| M2  | Steering motor (only front axis) |
| a   | If steer left: 	3V, else 0V |
| b   | If steer right: 	3V, else 0V |
| c   | Drive backwards: 3V, else 0V |
| d   | Drive forwards:	3V, else 0V |
| RF_sel | Channel A: both 3V, Channel B: white 3v green 0v, Channel C: white 0v green 3v |

##Voltages M1

	Driving forwards:
	(M1-) ---- (-6V) ---- (M1+)
	
	Driving backwards:
	(M1-) ---- (6V) ---- (M1+)


##Voltages M2

	Steering left:
	(M2-) ---- (-2V) ---- (M2+)
	
	Steering right:
	(M2-) ---- (2V) ---- (M2+)
