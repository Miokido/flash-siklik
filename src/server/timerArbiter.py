from j2l.pytactx.agent import Agent


class ITimeArbiter:
    def start(self) -> None:
        """
        Start the timer of the game by saving timestamp
        """
        ...

    def getDuration(self) -> int:
        """
        Return duration of the game
        """
        ...

    def setDuration(self, timer: int) -> None:
        """
        Set duration of the game
        """
        ...

    def getTimestamp(self) -> int:
        """
        Return timestamp
        """
        ...

    def getRemainingTime(self) -> int:
        """
        Get remaining time of the game
        """
        ...

    def setRemainingTime(self) -> None:
        """
        Set remaining time of the game
        """
        ...


class TimerArbiter(ITimeArbiter):
    def __init__(self, agent: Agent, duration: int = 300) -> None:
        self.__pytactxAgent = agent
        self.__duration = duration
        self.__startTimestamp = None
        self.__remainingTime = None

    def start(self) -> None:
        self.__startTimestamp = self.__pytactxAgent.game["t"]

    def getDuration(self) -> int:
        return self.__duration

    def setDuration(self, timer: int) -> None:
        if timer < 0:
            raise ValueError("Timer donné négatif")

    def getTimestamp(self) -> int:
        return self.__pytactxAgent.game["t"]

    def getRemainingTime(self) -> int:
        self.setRemainingTime()
        return self.__remainingTime

    def setRemainingTime(self) -> None:
        deltaTime = (self.getTimestamp() - self.__startTimestamp) // 1000
        self.__remainingTime = self.__duration - deltaTime
