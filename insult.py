import random

class insultGenerator(object):
    def __init__(self):
        # setup the lists of insult fodder

        self.nounList = ['loser',
                         'jerk',
                         'nerd',
                         'doodie head',
                         'butthead',
                         'bonehead',
                         'dunce',
                         'moron',
                         'nerf herder']
        self.adjectiveList = ['smelly',
                              'ugly',
                              'gimpy',
                              'slimy',
                              'crabby',
                              'scabby',
                              'scratchy']
        self.connectorList = ['are one',
                              'are the biggest',
                              'are becoming a']
    def getInsult(self):
        insult = "you"

        # connector phrase
        connector = random.randint(1, len(self.connectorList))
        insult += " " + self.connectorList[connector-1]

        # adjectives
        adjCount = random.randint(2,4)
        random.shuffle(self.adjectiveList)
        for i in range(0,adjCount):
            if i != 0:
                insult += ", "

            else:
                insult += " "
            insult += self.adjectiveList[i]

        # ending noun
        noun = random.randint(1,len(self.nounList))
        insult += " " + self.nounList[noun-1]
        return insult


# a little example to get some insults flowing
if __name__ == '__main__':
    ig = insultGenerator()
    insult = ig.getInsult()
    print(insult)
