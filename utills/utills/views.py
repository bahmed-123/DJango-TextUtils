from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def Analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    # check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

     # check which checkbox is on
    if removepunc == "on" and (len(djtext) > 0):

        punctuations = """!()-[]{};:'"\,<>./?@#$%^&*_~"""
        analyzed = ""
        for char in djtext:

            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps=="on" and (len(djtext) > 0):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Change to Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on" and (len(djtext) > 0):
        analyzed = ""
        for char in djtext:
            if char != "/n" and char != "/r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre",analyzed)

        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on" and (len(djtext) > 0):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}


    if (removepunc == "on" and (len(djtext) > 0) or fullcaps=="on" and (len(djtext) > 0) or newlineremover == "on" and (len(djtext) > 0) or extraspaceremover == "on" and (len(djtext) > 0)):
        return HttpResponse("Please Select Operator")

    return render(request, 'analyze.html', params)