## Smart City (My Problem) Model

Code is locate in [**the following folder**](escalator_sim/)

The main file is [**escalator.py**](escalator_sim/escalator.py) with the following input arguments:

* -t - number of timesteps
* -s - stand only.  Boolean controlling if the policy is stand only, or if walking is allowed
* --evil - What proportion of walkers are super selfish will stand in the walking lane.

Running the escalator.py file will call main and instantiate the code to run.   

Files of interest:

* [**policy.py**](escalator_sim/policy.py) Contains the abstract Policy definition as well as the specific standing and walking policies.
* [**individual.py**](escalator_sim/individual.py) Contains the concrete implementation of individuals
* [**escalaor.py**](escalator_sim/escalator.py) Contains the main escalator class which defines 1) Occupancy State of the escalator and 2) Logic Control over how individuals move through the escalator.  This file also has the Queue object to sample new individuals entering the escalator. This is also the location of main. 

