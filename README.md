**Project Title**

Building energy efficiency.

**Description**

The aim of this project is to estimate the energy efficiency of a building starting from 8 parameters.<br>
In this project I use the following dataset:

<a href="https://archive.ics.uci.edu/dataset/242/energy+efficiency">UCI Archive</a>

The study represented by this dataset correlates the heating load and cooling load requirements of<br> 
buildings with building parameter.<br>
In this project I focus the interest on the heating load.<br>
For the extimation I use a multiple linear regression model.<br>
I normalized the features values in order to let the model more efficient and I based the analysis on<br>
4 features selected from the starting 8 using RFE(recursive feature elimination) to let faster<br>
program elaboration.<br> 
The dataset is composed by 768 samples with 8 X parameters and 2 target variables y.<br>
I will use only y1(heating load).<br>
All variables are :<br>
X1	Relative Compactness<br>

X2	Surface Area<br>

X3	Wall Area<br>

X4	Roof Area<br>

X5	Overall Height<br>

X6	Orientation<br>

X7	Glazing Area<br>

X8	Glazing Area Distribution<br>

y1	Heating Load<br>

y2	Cooling Load<br>


**Usage**

To use this program , follow the next steps :<br>
- download the file zip from the http address shown above on the local disk ;<br>
- unzip the excel table in a directory ;<br>
- launch the program in the same directory.<br>
It is also mandatory to have installed the python libraries pandas and scikit-learn.<br>

**License**

Distributed under the MIT License. See `LICENSE.txt` for more information.
