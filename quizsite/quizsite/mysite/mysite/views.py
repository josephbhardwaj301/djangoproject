@@ -9,7 +9,10 @@ def index(request):
    links = ["admin:index", "aggregates", "all", "between", "initial", "formdata"]
    return render(request, "home.html", {"links": links})


def mysession(request):
    session=request.session
    session[1]="One"
    return render(request,"session.html",{"session":session})
def test(request):
    return render(request, "bootstrap.html")
def vsj404(request,exception):
