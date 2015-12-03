#Interface for interaction with the user
__author__ = 'Soukaina'
#Libraries
import re
import IDTS.modules.Evaluator
import IDTS.modules.Guider
import IDTS.modules.problem_parser
import IDTS.modules.Guider
#Print instructions
print("Welcome to your discrete math tutor\n")
print("Please choose the type of problems you want to exercise on, or choose random to generate random exercises\n")
print('1. PERMUTATION - with constrained repetition .\n'
      '2. PERMUTATION - with repetition and no limit on the number of repetitions.\n'
      '3. Random')
#get user input
problemType_userchoice = input("Please enter the number of your choice: ")
#get the number of exercises to work on
numOfExercises = input ("Please type the number of exercises you want to work on in this set: ")
print("This set will have " + numOfExercises +" exercises\nGood Luck!\n\n")
problems = IDTS.modules.problem_parser.problem_extractor(problemType_userchoice)
for x in range(0, int(numOfExercises)):
    problem = problems[x]
    print("Problem" + str(x+1))
    string = IDTS.modules.problem_parser.get_pure_problem_statement(problem)
    print("Formula:" +problems[x].formula)
    print("Please type your answer as a formula with numbers plugged in it, not as a number")
    answer = input("Answer: ")
    while (IDTS.modules.Evaluator.CheckAnswer(problem, answer)!= 1):
        if (IDTS.modules.Evaluator.CheckAnswer(problem, answer)== -2):
            print("sorry, this formula is not recognised")
        if (IDTS.modules.Guider.get_hint(problem, answer)):
            #print(modules.Guider.give_hint(problem, answer))
            print(IDTS.modules.Guider.get_hint(problem, answer))
        answer = input("Answer: ")
    if(IDTS.modules.Evaluator.CheckAnswer(problem, answer)== 1):
        print ("Correct answer! You rock! :D")



