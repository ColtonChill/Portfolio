# Personal Projects
Each of these projects are examples of Code that demonstrate a different ability and set of knowledge. 


## Fractal Generator
Originally, this project was a failed attempt of a math student to make a fractal generator. I then took over their failed project, refactored, modularized, and expanded its capacities.

Demonstrates:
* Teamwork, Research ability
* Refactoring and Debugging
* Mathematical Understanding
* Documentation Capacity

### Execution Dependencies:

```
$ sudo apt-get install python3-pil.imagetk
```
```
$ pip3 install colour
```

_(Read the user manual for run instructions)_

## Parallel Pi
* Built with gradle so no additional dependencies are necessary.
* Uses multi-threading to asynchronous calculate Pi using Bellard's Algorithm
* Demonstrate resource sharing and concurrent blocking calls.  

Can be run by installing gradle
```
$ sudo apt-get install gradle
```
then building and executing the result `.jar` file
```
$ gradle build
$ java -jar build/libs/Parallel\ Pi-1.0-SNAPSHOT.jar
```

## Weather Web App

This project takes several nested API called to get the user's local weather as well as the 5 day forecast. Each forecast element can be voted on by the user as either likely or unlikely by clicking on the element in question.

Demonstrates:
* Dynamic Aesthetics
* API Calls
* Vue Life-cycle