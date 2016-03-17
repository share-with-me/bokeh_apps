# bokeh_apps
This is just a 'Getting started' pack of bokeh - the data visualisation library in python. 

Important:
All the examples have been tried and executed in Linux 64 bit version. Please refer to proper steps in case of other operating systems including especially Windows!

Requirements - 
Given the examples in the repository, make sure that you have atleast the following modules installed.

1. bokeh (for installation, refer http://bokeh.pydata.org/en/latest/docs/installation.html

2. numpy and scipy

3. matplotlib

4. pip (makes the installation of various modules easy)

5. If while executing the code, a module cannot be found, make sure to install it by typing in the terminal
   pip install <module-name>

It consists of 4 folders - 

1. apps - It contains basic codes that can be run locally. Various aspects of all the features offered by bokeh have been tried to cover in the examples.
      To execute any python script in this folder:
      1. Navigate to the current directory
      2. type
            python <file_name>   
         Eg: python bar.py

2. fourier based - It just is an attempt to target various fourier transformation techniques. The execution is no different from that mentioned for 1.
  It is ongoing and further contributions shall be made shortly/
  
3. server-based  - This folder contains python files that require bokeh server functionality. PLease refer 
    http://bokeh.pydata.org/en/0.11.1/docs/user_guide/server.html for any details. The examples have been referred heavily from the ones mentioned on the above link for the purpose of learning. Further developments are on their way.
    The execution steps have been mentioned on the above link.
    
4. interactive apps - It is an attempt to make an interactive app using bokeh. Again, the examples on user guide have been referred. 
   To execute the script, open your terminal:
   1. Navigate to the current directory
   2. type
      bokeh serve --show climate.py
      It will show an instance running on localhost port number 5006. 
      
This repo contains examples that are a good starter kit. Further developments combining all of the above features are on their way :) 
Cheers!
