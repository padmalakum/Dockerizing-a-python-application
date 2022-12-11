from django.shortcuts import render
from .models import assessment
from django.http import JsonResponse


def index(request):
    if request.method == "GET":
        context = {"Title": "Assessment", }
        return render(request, "index.html", context)


def create(request):
    if request.method == 'POST':
        if request.POST.get('text') == "" or request.POST.get('start') == "" or request.POST.get('end') == "":
            error = "Field`s can`t be empty!"
            success = {"error": error}
            return JsonResponse(success)
        elif int(request.POST.get('start')) > int(request.POST.get('end')):
            error = "END must be greater than START!"
            success = {"error": error}
            return JsonResponse(success)
        elif int(request.POST.get('end')) > len(request.POST.get('text')):
            textLength = len(request.POST.get('text'));
            error = f"The END field may not be longer than {textLength} characters"
            success = {"error": error}
            return JsonResponse(success)
        else:
            text = request.POST['text']
            start = request.POST['start']
            end = request.POST['end']
            new_assessment = assessment(text=text, start=start, end=end)
            new_assessment.save()
            success_message = "Data saved successfully!"
            success = {"text": text, "start": start, "end": end, "success_message": success_message}
            return JsonResponse(success)
