# 1st Round : Freiburg, Helsinki and Prague, using automatically generated schedules
#############

## 30.03.20 - 04.04.20
Maps:		automatically from OSM
Schedules: 	automatically from GTFS
Cities:		Freiburg, Helsinki and Prague

### Improvements achieved
* Devices are turned off before starting and after reaching the destination

### Improvements needed:
* Not sure how realistic is the schedule, we need to reproduce a schedule manually to compare

### Learned
* Probabilistic routing algorithms seems to have better performance than naive approaches. 
However, there are several things that hold smart algorithms to improve its performance
1) The unbalance in the schedules cause several devices to loose its messages (since they are turned off)
2) Metrics:
2.1) Delivery Probability: Freiburg(1st PRoPHET, 2nd Epidemic), Helsinki (1st MaxP, 2nd PRoPHET, 3rd Epidemic, 4th Spray), Prague (1st MaxP, 2nd Epidemic, 3rd PRoPHET, 4th Spray)
2.2) Latency: Freiburg(1st PRoPHET, 2nd Epidemic), Helsinki (1st Spray, 2nd Max, 3rd Epidemic, 4th PRoPHET), with epidemic performing specially poorly to small buffer sizes, Prague (1st Spray, 2nd Max, 3rd Epidemic, 4th PRoPHET)
2.3) Hop Counts: Freiburg (1st PRoPHET, 2nd Epidemic), Helsinki (Spray, PRoPHET, Max, Epi), Prague (Spray, PRoPHET, Max, Epi)



# 2nd Round : Freiburg using Real Schedule
#############

## 05.04.20
Maps:		automatically from OSM
Schedules: 	Manually created from the schedule of Freiburg
Cities:		Freiburg

### Improvements achieved
* Wrote an alternative algorithm that calculate the number of trams independent from the transformation process and used it to calculate the number of needed trams for the map from Freiburg I am using.

### Improvements needed:
* I believe that all trams within the same line should have a common identifier. It makes no sense that a station sees two buses of the same line as completely independent devices.

### Learned
* The best delivery probability was from MaxProp, followed by Epidemic and PRoPHET, but the difference was small.
