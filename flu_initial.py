import sys
sys.path.append('/home/konrad/ICM/cog-abm-tutorial/COG-ABM/src')
# TODO adapt to your instalations^^^^

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


class FluAgentState(object):

    # TODO


class FluInteraction(Interaction):

    def num_agents(self):
        return 2

    def interact(self, agent1, agent2):
        ags1, ags2 = agent1.state, agent2.state
        # TODO


def prepare_agents(num_agents, num_doctors, num_ill):
    agents = [Agent(state=FluAgentState())
        for _ in xrange(num_agents)]
    #TODO and adapt ^^^^


def flu_experiment(num_agents, num_doctors, num_ill, iters):
    agents = prepare_agents(num_agents, num_doctors, num_ill)
    topology = generate_simple_network(agents)
    s = Simulation(topology, FluInteraction(), agents)
    return s.run(iters, DUMP_FREQ)


def analyze(results):
    def tmp(agents):
        return avg([ for agent in agents])
        # TODO ^^^^^^ 1 - infected, 0 - not infected
    return [(it, tmp(agents)) for it, agents in results]


def present_results(analysis):
    import pprint
    pprint.pprint(analysis)
    from presenter.charts import wykres
    wykres(analysis, "iteration", "ill percentage")


def main(args):
    res = \
        flu_experiment(NUM_AGENTS, NUM_DOCTORS, NUM_ILL, ITERS)
    analysis = analyze(res)
    present_results(analysis)


if __name__ == '__main__':
    main(sys.argv[1:])
