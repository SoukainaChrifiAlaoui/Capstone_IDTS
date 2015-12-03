import IDTS.modules.Tree
import IDTS.modules.MathModel
import IDTS.modules.problem_parser
import IDTS.modules.Guider
import re

#gets user choice as a string and returns another string that contains a specific number
#Permutations is '1'
#Combinations is '2'
#Random is '3'
#This number is used to designate which exercises file to open : it is passed to the function 'file_picker' in 'problem_parser' module
def get_problem_type (user_choice):
    problems_type = ""
    if (user_choice == 'Permutations'):
        problems_type = '1'
    elif (user_choice == 'Combinations'):
        problem_type = '2'
    elif (user_choice == 'Random'):
        problems_type = '3'
    return problems_type

#gets user input as a string and returns a number
#this number is the number of exercises that the user will work on: it will be used while looping
def get_num_problems (user_choice):
    return int(user_choice)

#gets the type of problems user wants to work on, opens the specific file and loads problems in a list of Problem objects
#Problem object structure can be checked in the module 'problem_parser'
#problems_type parameter should come from function get_problem_type above
def get_problems (problems_type):
    problems = IDTS.modules.problem_parser.problem_extractor(problems_type)
    return problems

#returns problem statement as it should be displayed to the user
#This problem statement is stripped from its annotations. Only pure text is displayed
#problem parameter is an element of the list problems gotten via the function above
def get_problem_statement (problem):
    statement = IDTS.modules.problem_parser.get_pure_problem_statement(problem)
    return statement

#gets the answer of the user from the input stream or interface as a string
def get_answer (answer):
    return str(answer)

#Evaluates the answer given the problem and returns an integer value depending if the answer is right or wrong
#if returns 1 the answer is correct
#if returns -2 the input is garbage or a completely messed up formula (unrecognised formula)
#if returns 0 the formula on itself is correct but there is a mistake in teh numbers
#if returns -1 the answer uses a wrong formula (formula is recognised but it is wrong for the given problem)
def evaluate_answer (problem_id, problems, answer):
    result = IDTS.modules.Evaluator.CheckAnswer(problems[problem_id], answer)
    return result

#Gives feedback depending on the output of 'evaluate_answer' function above
# calls the 'Guider' module if 'checkAnswer' returns a value other than 1 and gets the question or comment it should display
#the function it calls can be checked at 'Guider' module. It calls 'checkAnswer' and gets the result itself
#function 'evaluate_answer' doesn't have to be called before this function
def give_feedback (problem_id, problems, answer):
    feedback = IDTS.modules.Guider.give_feedback(problems[problem_id], answer)
    return feedback

#returns the string it should be highlighted inside the problem statement to give the user a hint depending on the mistake s/he made
def give_hint (problem_id, problems, answer):
    hint = IDTS.modules.Guider.give_hint(problems[problem_id], answer)
    return hint
#constructs data structure with all problem statements and their ids
def get_problem_statements (problems_type, numOfExercises):
    problems_list = []
    problems = IDTS.modules.interface.get_problems(problems_type)
    for x in range(0, numOfExercises):
        problem_statement = get_problem_statement(problems[x])
        tuple = (x, problem_statement)
        problems_list.append(tuple)
    return problems_list






