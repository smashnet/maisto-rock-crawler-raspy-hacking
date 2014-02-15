maisto-rock-crawler-raspy-hacking
=================================

In this project i will hack the Maisto [Rock Crawler RC car](http://www.amazon.de/Maisto-581152-Crawler-farblich-sortiert/dp/B003ML36HI/ref=sr_1_1?ie=UTF8&qid=1392464428&sr=8-1&keywords=maisto+rock+crawler) attaching a Raspberry Pi to it.

You can finally access the Rock Crawler through its own WebInterface that gives you the following features:

* Steering using sliders
* See where you are driving using the Raspberry Pi camera
* ... more to come

Status
======

The project just started so I'm currently figuring out how the internal PCB of the car works.

PCB
===

![Backside of the main PCB](https://github.com/smashnet/maisto-rock-crawler-raspy-hacking/blob/master/pcb/pcb_back.jpg?raw=true)

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
	
##Hacking the control
In order to control the car you just need to bridge a, b, c or d with the 3V pin shown in the picture below.

| Pin | Function |
|:---:| -------- |
| a   | Steer left |
| b   | Steer right |
| c   | Drive backwards |
| d   | Drive forwards |

![PCB back detail](https://github.com/smashnet/maisto-rock-crawler-raspy-hacking/blob/master/pcb/pcb_back_detail.jpg?raw=true)