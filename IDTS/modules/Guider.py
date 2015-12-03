__author__ = 'Soukaina'
#Libraries
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import re
import IDTS.modules.Tree
import IDTS.modules.MathModel
import IDTS.modules.Evaluator

#extract the hint given student answer and system answer
def get_hint (problem, std_answer ):
    hint = ""
    wrong_turn = get_wrong_turn (problem, std_answer)
    if (wrong_turn):
        hint = wrong_turn.get_hint()
    return hint

#gets the node at which the mistake happened
def get_wrong_turn (problem, std_answer):
    sys_sol = problem.problem_type
    answer = IDTS.modules.Evaluator.MatchAnswer(problem, std_answer)
    if (answer != '0'):
        wrong_turn = IDTS.modules.MathModel.root.findAncestor(answer, sys_sol)
        return wrong_turn
    else:
        return None

#returns phrases of the problem statement that help with the current issue the user is facing
def give_hint (problem, answer):
    statement = problem.problem_statement
    wrong_turn = get_wrong_turn (problem, answer)
    if (wrong_turn.key == 15): #order is the problem
        if (problem.problem_type == '5' or problem.problem_type == '4'): #if combination exercise
            the_hint = re.search("\[(.*)\]<com>", problem.problem_statement)
            the_hint = the_hint.group(1)
            if (re.search("\[", the_hint)):
                the_hint = the_hint.split("[")[1]
        if (problem.problem_type == '1' or problem.problem_type == '2' or problem.problem_type == '3'): #if permutation exercise
            the_hint = re.search("\[(.*)\]<per>", problem.problem_statement)
            the_hint = the_hint.group(1)
            if (re.search("\[", the_hint)):
                the_hint = the_hint.split("[")[1]
    elif (wrong_turn.key == 20 or wrong_turn.key == 10): #repetition is the problem
        if (problem.problem_type == '2' or problem.problem_type == '4'): #if repetition is allowed
            the_hint = re.search("\[(.*)\]<rep>", problem.problem_statement)
            the_hint = the_hint.group(1)
            if (re.search("\[", the_hint)):
                the_hint = the_hint.split("[")[1]
        if (problem.problem_type == '3' or problem.problem_type == '5'): #if repetition is not allowed
            the_hint = re.search("\[(.*)\]<nor>", problem.problem_statement)
            the_hint = the_hint.group(1)
            if (re.search("\[", the_hint)): #if the phrase is at the end of problem statement, strip the other tagged phrases
                the_hint = the_hint.split("[")[1]
    elif (wrong_turn.key == 26): #constrained repetition is the problem
        the_hint = re.search("\[(.*)\]<lre>", problem.problem_statement)
        the_hint = the_hint.group(1)
        if (re.search("\[", the_hint)):
            the_hint = the_hint.split("[")[1]
    return the_hint

def give_feedback (problem, answer):
    feedback = ""
    eval_result = IDTS.modules.Evaluator.CheckAnswer(problem, answer)
    if (eval_result != 1):
        if (eval_result == -2):
            feedback = "sorry, this formula is not recognised"
        if (IDTS.modules.Guider.get_hint(problem, answer)):
            feedback = IDTS.modules.Guider.get_hint(problem, answer)
    if(eval_result == 1):
        feedback = "Correct answer! You rock! :D"
    return feedback

