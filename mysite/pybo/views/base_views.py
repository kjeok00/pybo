from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from ..forms import AnswerForm
from ..models import Question


def index(request):
    page = request.GET.get('page', '1') #page
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10) #페이지당 10개씩
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()

    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)