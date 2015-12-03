import IDTS.modules.Evaluator
import re

class Problem(object):
    def __init__(self, problem_statement, problem_type, num_of_vars, vars):
        self.problem_statement = problem_statement
        self.problem_type = problem_type
        self.num_of_vars = num_of_vars
        self.vars = vars
        self.formula = None
    def print (self):
        str = "statement: "+self.problem_statement+" Type: " + self.problem_type + "variables "+ vars
        return str

def file_picker (user_problem_type_choice):
    #Specify the file depending on user choice
    if (user_problem_type_choice == '1'):
        tutor_file = "Problems_permutations.txt"
    elif (user_problem_type_choice == '2'):
       tutor_file = "Problems_combinations.txt"
    elif (user_problem_type_choice == '3'):
        tutor_file = "Problems_random.txt"
    else:
        tutor_file = ""
    return tutor_file

#removes the markups from the problem statement
def get_pure_problem_statement (problem):
    statement = re.sub(r"<[a-z]+>", "", problem.problem_statement)#problem.problem_statement.split("<")[0] + problem.problem_statement.split(">")[1]
    statement = statement.replace("[", "")
    statement = statement.replace("]", "")
    print(statement)
    return statement

#Open the file containing the problems and place them on a list of problems
def problem_extractor (user_problem_type_choice):
    problems = []
    file = file_picker(user_problem_type_choice)
    exercisesFile = open ("ITS.txt", "r")
    #print(exercisesFile.readlines()[2])
    numOfExercises = exercisesFile.readlines()[2].split("NUMOFPROBS=")[1]
    numOfExercises = ''.join(filter(lambda x: x.isdigit(), numOfExercises))
    exercisesFile.close()
    exercisesFile = open ("ITS.txt", "r")
    #loop through the exercises one by one
    for x in range(1,int(numOfExercises)+1):
        problem = ''
        for line in exercisesFile:
            if line.strip() == "[START]":  # get problem from text file
                break
        # Reads text until the end of the block:
        for line in exercisesFile:  # Keep reading
            if line.strip() == "[END]":
                break
            problem +=line
        #extract problem statement and structure
        problem_statement = problem.split("PROBID")[0]
        problem_type = problem.split("PROBID =") [1].split()[0]
        numOfVars = problem.split("NUMOFVARS =")[1].split()[0]
        #Get the variables and their values
        vars = [int(numOfVars)]
        vars = problem.split("VARS = [")[1].split("]")[0]
        vars = [x.strip() for x in vars.split(',')]
        vals = [int(numOfVars)]
        vals = problem.split("VALS = [")[1].split("]")[0]
        vals = [x.strip() for x in vals.split(',')]
        variables = dict(zip(vars, vals))
        problem_struct = Problem(problem_statement, problem_type, numOfVars, variables)
        formula = IDTS.modules.Evaluator.Solve (problem_struct)
        problem_struct.formula = formula
        problems.append(problem_struct)
    exercisesFile.close()
    return problems


