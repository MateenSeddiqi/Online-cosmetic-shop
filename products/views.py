from django.shortcuts import render, redirect, get_object_or_404
from .forms import FeedbackForm, ProductForm, ContactUsForm
from .models import Feedback, Product, contactUs
from django.http import HttpResponse

def home(request):
    products= Product.objects.all()
    feedback_form = FeedbackForm()
    context = {
        'products': products,
        'feedback_form': feedback_form,
    }
    return render(request, 'home.html', context)

def displayFeedback(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback.html', {'feedbacks': feedbacks})

def add_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('displayFeedback')
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

# Product View codes 

def manageProduct(request):
    products = Product.objects.all()
    return render(request, 'manageProduct.html', {'products': products})


def addProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manageProduct')
    else:
        form = ProductForm()
    return render(request, 'addProduct.html', {'form': form})


def deleteProduct(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('manageProduct')


def updateProduct(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES or None, instance=product)
        if form.is_valid():
            form.save()
            return redirect('manageProduct')
    else:
        # Populate the form with the existing product data
        form = ProductForm(instance=product)
    return render(request, 'updateProduct.html', {'form': form})


def aboutPage(request):
    return render(request, 'about.html', {})

def contact(request):
    if request.method == 'POST':
        contactUs = ContactUsForm(request.POST)
        if contactUs.is_valid():
            contactUs.save()
            return redirect('home')
        
    else:
        contactUs = ContactUsForm
    return render (request, 'contactUs.html', {'contactUs': contactUs})

def ContactMsg(request):
    contact_msgs = contactUs.objects.all()
    return render(request, 'contactMsg.html', {'contactMsgs': contact_msgs})

def deleteContactMsg(request, pk):
    contact_msgs = get_object_or_404(contactUs, pk=pk)
    contact_msgs.delete()
    return redirect('contactMsg')

def ProductDetail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'productDetails.html', {'product': product})