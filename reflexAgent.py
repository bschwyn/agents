
#This is a simple reflex agent for operating in Vacuum Cleaner World
#The agent selects actions based off of the current percept and ignores the percept history

class Action():

    def move(self):
        return 0

    def suck(self):
        return False

    def do(self):
        return (self.move(), self.suck())


class Suck(Action):
    def suck(self):
        return True

    def move(self):
        direction = 0
        return direction

class Left(Action):

    def move(self):
        direction = -1
        return direction

class Right(Action):
    def move(self):
        direction = 1
        return direction

class Agent():

    def __init__(self):
        self.rules = rules = {"dirty": Suck(),
                "A": Right(),
                "B": Left()
                 }

    def sensors(self, env):
        location = env.location
        dirty = env.location.cleanliness


    def interpretInput(self,percepts):
        location = percepts[0]
        status = percepts[1]
        state = (location, status)
        return state

    def ruleMatch(self, state, rules):
        location = state[0]
        status = state[1]
        if status == "dirty":
            return rules[status]
        else:
            return rules[location]

    def simpleReflexAgent(self,percepts):
        rules = self.rules
        state = self.interpretInput(percepts)
        action = self.ruleMatch(state, rules)



        return action.do()

vacuum = Agent()
percepts = ["B", "dirty"]
action = vacuum.simpleReflexAgent(percepts)
print(action)
percepts = ["A", "clean"]
action = vacuum.simpleReflexAgent(percepts)
print(action)