# from msilib.schema import ListView

import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render_to_response
import IDTS
# Create your views here.

def index(request):
    if request.method == 'GET':
      #
        return render_to_response('index.html') 
    if request.method == 'POST':
        data = json.loads(request.body)
        problems = []
        #Get the category the user wants to work on (permutations, combinations or random)
        #when user presses start button in the interface: exercise set should begin loading one problem at a time
        if data['type'] == "start":
            #the variable here is for my program to use, but I should get user choice from the interface
            #user choice that I should get from interface is what I called data([problem_type])
            #the function 'get_problem_type' assumes that it will get one of the three strings 'Permutations', 'Combinations, or 'Random'
            #It transforms it to a value that the system understands
            problems_type = IDTS.modules.interface.get_problem_type(data['problem_type'])
            #the function simply turns it into an int because the loop will use it
            numOfExercises = IDTS.modules.interface.get_num_problems(data['numOfExercises'])
            #problems bellow will only be used by my back-end
            problems = IDTS.modules.interface.get_problems(problems_type)
            #create the list of problem statements and their ids
            #ids are the same ones u should display in the green bubble in the interface that displays number of the current exercise
            #each element of the list is a tuple that has two attributes (int id, string problem)
            data['problems'] = IDTS.modules.interface.get_problem_statements(problems_type, numOfExercises)
            return HttpResponse(data['problems'])
        #when a user answers a problem
        elif data['type'] == "exercise":
            #I need to get the problem id as an int...is this smth I can do??
            prob_id = int(data['problem_id'])
            #data['answer'] should be coming from the interface
            #answer should be normally a string, the functions takes care of making it a string
            answer = IDTS.modules.interface.get_answer(data['answer'])
            #data['evaluation'] gives u an int value that tells u if the answer is correct or not (u can check those values in 'modules.interface'
            data['evaluation'] = IDTS.modules.interface.evaluate_answer(prob_id, problems, answer)
            #data['feedback'] gives you the string that should be displayed to the user: it is a question
            data['feedback'] = IDTS.modules.interface.give_feedback(prob_id, problems, answer)
            return HttpResponse(data['evaluation'],data['feedback'])
        #when user asks for a hint inside the problem: keyword/key-phrase inside the problem that can help him/her
        elif data['type'] == "give_me_hint":
            prob_id = int(data['problem_id'])
            answer = IDTS.modules.interface.get_answer(data['answer'])
            data['hint'] = IDTS.modules.interface.give_hint(prob_id, problems,answer)
            #the hint should normally be highlighted or underlined inside the problem statement in the interface but whatever
            return HttpResponse(data['hint'])