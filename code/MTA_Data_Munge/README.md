## MTA Data Munge

This project is the start of the data munging required to get the entrance and exit stats from each station at different points of the day to develop a model of transit through the subway system.  For now a single file  [Read_Data.py](code/MTA_Data_Munge/Read_Data.py) handles reading in and pulling some stats from the csv file. 

A single input argument currently exists: --data which you must specify to point to a data file.   It will default to the sample data file that was dropped into the sample location. 