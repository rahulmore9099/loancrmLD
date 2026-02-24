from django.shortcuts import render

def ai_page(request):
    return render(request, "ai_assistant/ai.html")