from django.http import HttpResponse
def homePageView(request):
    return render(request, "home.html")
