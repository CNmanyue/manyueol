#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 21:47
# @Author  : zhouxw
# @File    : views.py
# @Software: PyCharm


from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .forms import CaptchaTestForm
from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_context_data(self, **kwargs):
        """
        2. 如果使用 generic view, 添加验证码form到context中返回到template
        :param kwargs:
        :return:
        """
        context = super().get_context_data(**kwargs)
        context['form'] = CaptchaTestForm()
        return context


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    form = CaptchaTestForm(request.POST)

    # 3. Validate the form: the captcha field will automatically
    # check the input
    if not form.is_valid():
        # error_message = "You didn't pass in the captcha change."
        return render(request, 'polls/detail.html', locals())
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        error_message = "You didn't select a choice."
        return render(request, 'polls/detail.html', locals())
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
