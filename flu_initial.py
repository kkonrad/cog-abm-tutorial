import sys
sys.path.append('/home/konrad/ICM/cog-abm-tutorial/COG-ABM/src')

import random

from cog_abm.core import Simulation, Agent
from cog_abm.core.interaction import Interaction
from cog_abm.extras.additional_tools import generate_simple_network
from cog_abm.extras.tools import avg

NUM_AGENTS = 100
NUM_DOCTORS =
NUM_ILL = 5
INFECT_PROBAB = 0.75
CURE_PROB = 0.95
ITERS = 500000
DUMP_FREQ = ITERS / 100



def main(args):
    res = \
        flu_experiment(NUM_AGENTS, NUM_DOCTORS, NUM_ILL, ITERS)
    analysis = analyze(res)
    present_results(analysis)


if __name__ == '__main__':
    main(sys.argv[1:])
