import random
import string


def generateRandomSoln(length=5):
    return [random.choice(string.printable) for _ in range(length)]


def eval(solution):
    target = "rahul"
    difference = 0
    for i in range(len(target)):
        s = solution[i]
        
        t = target[i]
        
        difference = difference + abs(ord(s)-ord(t))
        
    return difference



def mutate(solution):
    index = random.randint(0, len(solution)-1)
    solution[index] = random.choice(string.printable)


best_possible_solution = generateRandomSoln()
best_possible_score = eval(best_possible_solution)
while(True):
    print('So far the best solution score is:', best_possible_score,
          ' solution is:', "".join(best_possible_solution))
    
    if best_possible_score == 0:
        break
    
    newSolution = list(best_possible_solution)
    mutate(newSolution)
    
    score = eval(newSolution)
    
    if eval(newSolution) < best_possible_score:
        best_possible_solution = newSolution
        best_possible_score = score
