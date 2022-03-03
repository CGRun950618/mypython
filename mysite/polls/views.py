from django.shortcuts import render

# Create your views here.

from django.http import  HttpResponse,Http404,HttpResponseRedirect
from .models import Choice,Question
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
#
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

def index(request):
    lastest_question_list=Question.objects.order_by('-pub_date')[:5]
    template=loader.get_template('polls/index.html')
    context={
        'latest_question_list':lastest_question_list,
    }
    return HttpResponse(template.render(context,request))


# def detail(request,question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})

def detail(request,question_id):
     #快捷函数get_object_or_404
     question=get_object_or_404(Question,pk=question_id)
     return render(request,'polls/detail.html',{'question':question})











# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
#
# def results(request, question_id):
#     response = "问题 %s."
#     return HttpResponse(response % question_id)
#
# def vote(request, question_id):
#     return HttpResponse("投票 %s." % question_id)
#
# def man(request,pg):
#     return HttpResponse("男性 %s 个"%pg)