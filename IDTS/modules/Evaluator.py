#Solve the problem and compare the solution with the answer provided by the user
__author__ = 'Soukaina'

#Libraries
import re
import sympy
from sympy.parsing.sympy_parser import parse_expr
import IDTS.modules.problem_parser


#finds the answer to a problem
def Solve (problem):
    #construct formula solution depending on problem type
    formula = ""
    if problem.problem_type == '1':
        denom = ""
        if (int(problem.num_of_vars) <= 2):
            formula = "factorial("+vars['n']+")"
        else:
            formula = "factorial("+problem.vars['n']+")/("
            for x in range (1, int(problem.num_of_vars)):
                denom += "factorial("+problem.vars['n'+ str(x)]+")*"
            denom = denom[:-1]
            denom +=")"
            formula +=denom
    elif problem.problem_type == '2':
        formula = problem.vars['n']+"**"+problem.vars['k']
    elif problem.problem_type == '3':
        formula = "factorial("+problem.vars['n']+")/factorial("+problem.vars['n']+"-"+problem.vars['k']+")"
    elif problem.problem_type == '4':
        formula = "factorial("+problem.vars['k']+problem.vars['n']+"-1)/(factorial("+problem.vars['k']+")*factorial("+problem.vars['n']+"-1))"
    elif problem.problem_type == '5':
        formula = "factorial("+problem.vars['n']+")/(factorial("+problem.vars['k']+")*factorial("+problem.vars['n']+"-"+problem.vars['k']+"))"
    return formula

#matches answer to one type of problems
def MatchAnswer (problem, answer):
    pattern_formula_probType1 = re.compile("^(factorial\([0-9]+\)(/\((factorial\([0-9]+\)\*?)+\))?|[0-9]+(\*[0-9]+)*)$")
    pattern_formula_probType2 = re.compile("^[0-9]+(\*\*|\^)[0-9]+$")
    pattern_formula_probType3 = re.compile("^(factorial\([0-9]+\)/factorial\([0-9]+-[0-9]+\)|factorial\([0-9]+\)/factorial\([0-9]+\))$")
    pattern_formula_probType4 = re.compile("^factorial\(([0-9]+\+[0-9]+-1|[0-9]+-1|[0-9]+\+[0-9]+|[0-9]+)\)/\(factorial\(([0-9]+|[0-9]+-1)\)\*?factorial\(([0-9]+|[0-9]+-[0-9]+)\)\)$")
    pattern_formula_probType5 = re.compile("^factorial\([0-9]+\)/\(factorial\([0-9]+(-[0-9]+)?\)\*?factorial\([0-9]+(-[0-9]+)?\)\)$")
    constrained_rep_pattern = re.compile("^(factorial\([0-9]+\)|[0-9]+(\*[0-9]+)*)$")

    if (re.match(pattern_formula_probType1,answer)):
        if(int(problem.num_of_vars) > 2):
            return '1'
        elif (int(problem.num_of_vars) == 2 and re.match(constrained_rep_pattern,answer)):
            return '1'
        else:
            return CheckAnswerType5(problem, answer)
    elif (pattern_formula_probType2.match(answer)):
        return '2'
    elif (pattern_formula_probType3.match(answer)):
        return '3'
    elif (pattern_formula_probType4.match(answer)):
        return CheckAnswerType5(problem, answer)
    elif (pattern_formula_probType5.match(answer)):
        return CheckAnswerType5(problem, answer)
    else:
        return '0'

#helper function of MatchAnswer : handles the confusion between formulas of problems type 4 and 5
def CheckAnswerType5 (problem, answer):
    facN = parse_expr('factorial('+problem.vars['n']+')')
    str = answer.split("/")[0]
    fac_ans = parse_expr(str)
    if (facN == fac_ans):
        return '5'
    facTop = parse_expr('factorial('+problem.vars['n']+'+'+problem.vars['k']+'-1)')
    if(facTop == fac_ans):
        return '4'
    else:
        return '-1'

#Checks if the answer provided is correct given the system answer
def CheckAnswer (problem, answer):
    answerType = MatchAnswer(problem, answer)
    if (answerType == '-1'):
        answerType = '4' #assumption that the user was trying to answer type 4 instead of type 5
    elif (answerType == '0'): #if the user enters garbage or a completely wrong formula
        return -2
    if problem.problem_type == answerType:
        if (parse_expr (answer) == parse_expr(problem.formula)):
            return 1
        else:
            return 0
    else:
        return -1


