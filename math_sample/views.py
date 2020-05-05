from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Lesson
from .forms import FeedbackForm
from django.views import generic
from .models import Feedback
import logging
#from mathsample_com_learning import BasicLogicForFirstApp, serial_number, number01, sign, number02, equals_sign
from mathsample_com_Data_info import Beginner_jump
# Create your views here.


logger = logging.getLogger('django')

# class HandlerAnswerView1(generic.CreateView):
#
#     def post(self, request, *args, **kwargs):
#         answer = request.POST.get('answer')
#         print(answer)


# class BaseListView(generic.ListView):
#     model = Lesson
#     template_name = 'math_sample/index.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['data'] = Lesson.objects.all()
#         context['feedbacks'] = Feedback.objects.all()
#         context['form'] = FeedbackForm
#         return context


def base_view(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['username']
            send_mail('Math for everyone', f'Thank you for your feedback. We will keep connection with you, {name}.',
                      'mathsampleus@gmail.com', [email], fail_silently=True)
            form.save()
            messages.success(request, 'Thank you for feedback!')
            return render(request, 'math_sample/index.html',
                          {'data': Lesson.objects.all(),
                            'feedbacks': Feedback.objects.all(),
                            'form': form,
                           'anchor': 'feedback'})
        return render(request, 'math_sample/index.html',
                      {'data': Lesson.objects.all(),
                       'feedbacks': Feedback.objects.all(),
                       'form': form,
                       'anchor': 'feedback'})
    context = {'data': Lesson.objects.all(),
               'feedbacks': Feedback.objects.all(),
               'form': form}

    return render(request, 'math_sample/index.html', context)


# def feedback(request):
#
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#
#             send_mail('Math for everyone', 'Thank you for your feedback. We will keep connection with you.',
#                       'mathsampleus@gmail.com', [form.email], fail_silently=True)
#             form.save()
#             messages.success('Thank you for feedback!')
#             return HttpResponse(status=200)
#     else:
#
#         form = FeedbackForm()
#
#     context = {'form': form}
#     return render(request, 'math_sample/index.html', context)
        # try:
        #     user_feed = request.POST.get('feedbackUsername')
        #     email_feed = request.POST.get('feedbackEmail')
        #     text_feed = request.POST.get('feedbackText')
        #     new_feedback = Feedback(username=user_feed, email=email_feed, text=text_feed)
        #     new_feedback.save()
        #     send_mail('Math for everyone', 'Thank you for your feedback. We will keep connection with you.', 'mathsampleus@gmail.com', [email_feed], fail_silently=True)
        #     logger.info("feedback() - saving feedback from {}".format(user_feed))
        #
        # except Exception as exc:
        #     print('Error: ', exc)
        #     logger.error("feedback() - error occurred: {}".format(exc))
        #     return HttpResponse(status=500)
        #
        # return HttpResponse(status=200)