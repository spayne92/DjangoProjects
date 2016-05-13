# Create your views here.
from django.http import HttpResponse    # N/A
from django.http import Http404
from django.template import loader      # N/A
from django.shortcuts import get_object_or_404, render

from .models import Question

def index(request):
    # creates list of 5 most recent questions (by pub_date)
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # loads template for polls index page
    # //template = loader.get_template('polls/index.html')
    # builds dictionary mapping to be passed to template
    # (maps template variable name to python object)
    context = {'latest_question_list': latest_question_list}
    # returns template loaded with above context
    # //return HttpResponse(template.render(context,request))
    # shortcut to skip template loading step
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    """
    # tries to assign object with question based on primKey
    try:
        question = Question.objects.get(pk=question_id)
    # raises 404 except is above object nonexistent
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    """
    # compacts try/except from above version
    question = get_object_or_404(Question, pk=question_id)
    # renders page with polls/detail template loaded with question context
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
