from src.server.j2l.pytactx.agent import Agent


class IDeathArbiter:
    def __init__(self):
        pass

    def isDead(self, agent: Agent):
        """
            this method returns true if the agent is dead
            :param agent: Agent
            :return: bool
        """
        pass

    def killAgent(self, agent: Agent):
        """
            this method kills the agent
            :param agent: Agent
            :return: void
        """
        pass

    def checkIsDeathElseKill(self, agent: Agent):
        """
            this method checks if the agent is dead and kills it if it is
            :param agent: Agent
            :return: void
        """
        pass

class DeathArbiter(IDeathArbiter):
    def __init__(self):
        super().__init__()

    def isDead(self, agent: Agent):
        """
            this method returns true if the agent is dead
            :param agent: Agent
            :return: bool
        """
        return agent.life <= 0

    def killAgent(self, agent: Agent):
        """
            this method kills the agent
            :param agent: Agent
            :return: void
        """
        agent.life = 0

    def checkIsDeathElseKill(self, agent: Agent):
        """
            this method checks if the agent is dead and kills it if it is
            :param agent: Agent
            :return: void
        """
        if self.isDead(agent) is False:
            self.killAgent(agent)