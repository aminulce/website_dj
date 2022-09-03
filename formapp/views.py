from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm, SnippetForm
from crispy_forms.helper import FormHelper
from .nlpapp import NatLang


def home(request):
    print (request.method)
    renderResponse = ''
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        print(request.method)
        if form.is_valid():
            job = form.cleaned_data['job']
            resume = form.cleaned_data['resume']
            [numJobWords, numResumeWords, numMatchedWords] = NatLang(job,resume)
            #return HttpResponse("<p>There are " + str(numJobWords) + " unique words in Job description</p><p>There are " + str(numResumeWords) + "unique words in Resume</p><p>There are " + len(numMatchedWords)+" matched words between job description and resume")
            print ("valid")
            renderResponse = "<p>There are " + str(numResumeWords) + " unique words in Resume</p><p>There are "+str(numJobWords)+" unique words in Job description</p><p>There are "+str(numMatchedWords)+" matched words</p>"
            #return HttpResponse()
    else:
        form = SnippetForm()

    form = SnippetForm()
    context = {'form':form, 'result':renderResponse}
    return render(request, 'home.html',context)

def contact(request):
    print (request.method)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(request.method)
        if form.is_valid():
            jobdesc = form.cleaned_data['your_name']
            return HttpResponse(jobdesc)
            print (jobdesc)
    else:
        form = ContactForm()

    form = ContactForm()
    context = {'form':form}
    return render(request, 'form.html',context)
    # return HttpResponse('<h1>This is coming from the contact request response</h1>')

def snippet_detail(request):
        print (request.method)
        renderResponse = ''
        numResumeWords = ''
        numJobWords = ''
        numMatchedWords = ''
        matched = 0
        if request.method == 'POST':
            form = SnippetForm(request.POST)
            print(request.method)
            if form.is_valid():
                job = form.cleaned_data['job']
                resume = form.cleaned_data['resume']
                [numJobWords, numResumeWords, numMatchedWords] = NatLang(job,resume)
                #return HttpResponse("<p>There are " + str(numJobWords) + " unique words in Job description</p><p>There are " + str(numResumeWords) + "unique words in Resume</p><p>There are " + len(numMatchedWords)+" matched words between job description and resume")
                print ("valid")
                #renderResponse = "<p>There are " + str(numResumeWords) + " unique words in Resume</p><p>There are "+str(numJobWords)+" unique words in Job description</p><p>There are "+str(numMatchedWords)+" matched words</p>"
                renderResponse = "Following are the results after comparing the job description and resume"
                #return HttpResponse()
                matched = (numMatchedWords/numJobWords)*100
        else:
            form = SnippetForm()

        form = SnippetForm()
        context = {'form':form,
                   'result':renderResponse,
                   'matched':matched,
                   'unmatched':100-matched,
                   'numResumeWords':numResumeWords,
                   'numJobWords':numJobWords,
                   'numMatchedWords':numMatchedWords}
        return render(request, 'resumeCompare.html',context)
