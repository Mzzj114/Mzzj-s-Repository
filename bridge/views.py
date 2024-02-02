from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import textPart
# Create your views here.



def getText(textname: str, language: str):
    obj = textPart.objects.get(text_name=textname)
    if language == "zh":
        return obj.texts
    return obj.texts_en


def fui_context(language):
    ui_context = {
        "home_title": getText("home title", language),
        "home_subtitle": getText("home subtitle", language),
        "ui_navbar_title": getText("ui navbar title", language),
        "ui_sidebar_title": getText("ui sidebar title", language),
        "ui_butt_home": getText("ui butt 1", language),
        "ui_butt_about": getText("ui butt 2", language),
        "ui_butt_acti": getText("ui butt 3", language),
        "ui_butt_shop": getText("ui butt 4", language),
        "ui_butt_commu":getText("ui butt 5", language),
        "lan": language,
    }
    return ui_context


def index(request, language="en"):
    context = {
        "intro": getText("home Project Introduction", language),
        "organizer_intro": getText("home Organizer intro", language),
        "acti_intro": getText("home Activity intro", language),
        "shop_intro": getText("home Shop intro", language),
        "commu_intro": getText("home Commu intro", language),
        "ui_learn_more": getText("ui learn more", language),

    }
    return render(request, "bridge/home.html",
                  dict(context, **fui_context(language)))


def thingsPage(request, language):
    context = {
        "intro": getText("home Project Introduction", language),
        "pptIntro": getText("class ppt Intro", language),
        "biliIntro": getText("class bili Intro", language),
        "githubIntro": getText("class github Intro", language),
        "csdnIntro": getText("class csdn Intro", language),
    }
    return render(request, "bridge/video.html",
                  dict(context, **fui_context(language)))


def commuPage(request, language):
    context = {
        "explain": getText("commu text", language),
    }
    return render(request, "bridge/commu.html",
                  dict(context, **fui_context(language)))
