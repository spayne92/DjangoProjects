# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import loader      # N/A
# shorctut objects to shorten idiomatic operations
from django.shortcuts import get_object_or_404, render
# shortcut for creating idiomatic generic views
from django.views import generic

from .models import Question, Choice

class IndexView(generic.ListView):
    # creates list of 5 most recent questions (by pub_date)
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # loads template for polls index page
    #template = loader.get_template('polls/index.html')
    # builds dictionary mapping to be passed to template
    # (maps template variable name to python object)
    #context = {'latest_question_list': latest_question_list}
    # returns template loaded with above context
    #return HttpResponse(template.render(context,request))
    # shortcut to skip template loading step
    #return render(request, 'polls/index.html', context)

    # generic view version of above implemenations
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # return last five published questions
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    """
    # tries to assign object with question based on primKey
    try:
        question = Question.objects.get(pk=question_id)
    # raises 404 except is above object nonexistent
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    """
    # compacts try/except from above version
    #question = get_object_or_404(Question, pk=question_id)
    # renders page with polls/detail template loaded with question context
    #return render(request, 'polls/detail.html', {'question': question})

    # generic view version of above implementations
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    #question = get_object_or_404(Question, pk=question_id)
    #return render(request, 'polls/results.html', {'question': question})

    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
