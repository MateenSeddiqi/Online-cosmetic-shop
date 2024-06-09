from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, 'home.html')

def displayFeedback(request):
    return render(request, 'feedback.html')



# from django.shortcuts import render, redirect
# from .models import Feedback

# def feedback_view(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         feedback = request.POST['feedback']
#         Feedback.objects.create(name=name, email=email, feedback=feedback)
#         return redirect('success_page')
#     return render(request, 'feedback.html')


# from django.shortcuts import render, redirect
# from .forms import FeedbackForm
# from .models import Feedback

# def feedback_view(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success_page')
#     else:
#         form = FeedbackForm()
#     return render(request, 'feedback.html', {'form': form})
