import copy


finalStates = []
nonFinalStates = [] 
old = []
limbaj =[]

class State:


    def __init__(self, data1, data2):
        self.final = int(data1)
        self.name = data2
        self.transitions = {}

    def __str__(self):
        return f"State: \n   - name = {self.name}\n   - final = {self.final}\n   - transitions = {self.transitions})\n"
        
    def writeToFile(self, file):
        file.write(self.__str__() + "\n")

    def add_transition(self, symbol, nextState):
        self.transitions[symbol] = nextState

    def getNextState(self, symbol):
        try:
            return self.transitions[symbol]
        except KeyError:
            return None

def getStateCopy(old, stateName):
    for state in old:
        if stateName == state.name:
            return state



def citire():

    with open ("data.in", "r") as f:
        l = f.readline().strip().split()

        for i in l:
            limbaj.append(i)

        for lines in f:
            lines = lines.strip().split()
            state = State(lines[0], lines[1])
            
            lines = f.readline().strip().split()

            for a in range(0, len(lines)-1, 2):
                state.add_transition(lines[a], lines[a+1])
                
            
            if state.final == 0:
                nonFinalStates.append(state)
            else:
                finalStates.append(state)





def afisare():
    with open("data.out", "w") as g:
        g.write("Stari Non-finale:\n")
        for i in nonFinalStates:
            g.write(f" {i.name} - {i.transitions}\n")
        g.write("\n")
        g.write("Stari Finale:\n")
        for i in finalStates:
            g.write(f" {i.name} - {i.transitions}\n")
        g.write("\n")
        g.write("Cuvinte:\n")
        for i in limbaj:
            g.write(f"{i} ")

         
        g.write("\n")

        minimal = HopcroftAlgorithm(old)

        g.write(f"\nAutomatul minimal: \n ")
        for state in minimal:
            state.writeToFile(g)


def getX(state, old, X):
    toStates = []

    for sets in state:
        for transition in sets.transitions:
            toStates.append(sets.transitions[transition])

    for sets in old:
        for stateOld in sets:
            for i in toStates:
                if i == stateOld.name:
                    X.append(stateOld)





def HopcroftAlgorithm(old):

    new = []
    old = [nonFinalStates, finalStates]
    ok = 0
    while True:
        A = old.pop()
        X = [] 
        ok = 0 
        getX(A, old, X)
        

        intersection = [] 
        difference = [] 

        for sets in old:
            for state in sets:
                for x in X:
                    if state.name == x.name:
                        intersection.append(state)
                    else:
                        difference.append(state)
        
        if len(difference) == 0 or len(new) == len(old):
            break
        else:
            new.append(difference)
        
        new.append(intersection)


        old = copy.deepcopy(new)
        new = []

    minimalStates = [] 
    for sublist in old:
        for state in sublist:
            minimalStates.append(state)

    return minimalStates

citire() 
afisare()

