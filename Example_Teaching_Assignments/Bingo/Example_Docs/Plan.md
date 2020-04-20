# 1. Requirements

A program needs to be able to read the users input, proved the user with
a basis user interface, and create a bingo deck to their specifications.

# 2. Design

The program will then take a series arguments, guild the user though
correct use, and mae the necessary data constructs to whichever source is 
required.


### Input/Output Dialogue

The program will take a message after promting the user. This dialog with go back
and forth until all of the required information has be extracted.
The program will then take that input and proceed, informing the user
if an error is encountered.

### Processing

Most if not all of the processing and computations will be decentralized,
occurring over several files as is more logical for the particular calculation
in question. See UML chart for the particular dependence trails that will
be utilized.


# 3. Implementation

* The program is kicked of in the file `src/UserInterface.py`, which will then 
begin the cascading call chain necessary to complete the process.
* The user/testing_file will execute the file and provide information to program.
* The inputs will be necessary to determine the size and quantity of 
cards generated, however the individual cards will be randomly generated,
so identical inputs will have divergent outputs.
This allows the program to have the locations for specific information hard coded in.
* This information will either be printed to the console, or stored in a 
file of the users determination.


# 4. Verification

Most of this program will be run using Unit Test found it `src/Testing`.
Each of the test will be tailored to a specific function, so that 
error can be more easily identified and corrected. Below is an enumeration
of the unit tests and there specific results.



## Test Cases
TBD by student
