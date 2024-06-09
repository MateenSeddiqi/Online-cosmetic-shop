from django.shortcuts import render, redirect, get_object_or_404
from .forms import FeedbackForm
from .models import Feedback

def home(request):
    feedback_form = FeedbackForm()
    return render(request, 'home.html', {'feedback_form': feedback_form})

def displayFeedback(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback.html', {'feedbacks': feedbacks})

def add_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('displayFeedback')
    return redirect('home')

def update_feedback(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            return redirect('displayFeedback')
    else:
        form = FeedbackForm(instance=feedback)
    return render(request, 'update_feedback.html', {'form': form})


def delete_feedback(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)
    feedback.delete()
    return redirect('displayFeedback')

