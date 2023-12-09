from django.shortcuts import render, redirect
from .models import chatRecord
from datetime import datetime
from django.http import HttpResponse, FileResponse
# Create your views here.


def index(request):
    if request.method == "POST":
        # print("get Post")
        message = request.POST["text"]

        if message and request.FILES:
            file = request.FILES["file"]
            # print("creating new message: ",message)
            newc = chatRecord(texts=message, post_date=datetime.now(), filename=file.name, upload=file)
            newc.save()
            # return
        elif message:
            # print("creating new message: ",message)
            newc = chatRecord(texts=message, post_date=datetime.now())
            newc.save()
            # return
        return redirect("FileHelper:index")


    # print("showing all")
    all_chat = chatRecord.objects.order_by("post_date")
    # for obj in all_chat:
        # print("each", obj.texts, "date:", obj.post_date)
    context = {
        "all_chat": all_chat,
    }
    return render(request, "FileHelper/index.html", context)


def download(request, filename):
    file = chatRecord.objects.get(filename=filename).upload
    response = HttpResponse(file.open('rb'))
    response['content_type'] = "application/octet-stream"
    response['Content-Disposition'] = 'attachment; filename="'+ filename +'"'
    return response
