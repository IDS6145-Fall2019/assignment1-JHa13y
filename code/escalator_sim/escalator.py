"""Main Sim Class, Escalator... Queue to sample"""
import argparse

class Queue:

    def __init__(self):
        self.waiting =[]

    def get_next_individual(self):
        """Returns the next individual in the queue"""
        pass

class Escalator:

    def __init__(self, evil=0.0, stand_only=False):
        self.proportion_evil = evil
        self.stand_only = stand_only

        self.left_spots =[] #List of individuals
        self.right_spots =[] #List of individuals
        self.throughput_counter = 0

    def get_new_individual(self, type):
        """
        :param type: What type of individual do you need?
        :return: New individual taken from the queue
        """
        print("Implement me!  Need to get a new individual of type={}".format(type))
        pass


    def advance_time(self):
        """
        Advances time a single timestep.
        This is the inner loop of the behavior diagram!
        """
        print("Oh Boy!  We need to implement this step still!")
        pass

    def run_for_x_timesteps(self, t):
        """
        Runs
        :param t:
        :return: The amount of entities through the simulation..
        """
        for i in range(0, t):
            self.advance_time()

        return self.throughput_counter


if __name__== "__main__":
    parser = argparse.ArgumentParser(description='Lets simulate an escalator!')
    parser.add_argument('-s', dest='stand_only', action='store_true',
                        default=False, required=False,
                        help='Boolean controlling if the policy is stand only, or if walking is allowed')
    parser.add_argument('-t', dest='t', type=int,
                        default=25, required=False,
                        help='How many timesteps should we run the sim for?  (default=25)')
    parser.add_argument('--evil', dest='evil',
                        default=0.0, required=False, type=float,
                        help='What proportion of walkers are evil and will stand in the walk lane?')
    args = parser.parse_args()
    print("Running Sim with Parameters=")
    print(args)

    escalator = Escalator(evil= args.evil, stand_only=args.stand_only)
    escalator.run_for_x_timesteps(args.t)