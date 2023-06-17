from django.shortcuts import HttpResponse, render


def radiobuttons(request):
    a = 0
    b = 0
    result = 0
    if request.GET:
        a = int(request.GET["a"])
        b = int(request.GET["b"])
        cmd = request.GET["command"]
        if cmd == "Add":
            result = a + b
        if cmd == "Sub":
            result = a - b
        if cmd == "Mul":
            result = a * b
        if cmd == "Div":
            result = a / b
    return render(request, "radiobuttons.html", {"a": a, "b": b, "result": result})


def index(request):
    return HttpResponse("Home")


def sub(request):
    if request.GET:
        aa = request.GET["aa"]
        bb = request.GET["bb"]
        subt = int(aa) - int(bb)
        return HttpResponse("Subtract= " + str(subt))
    return HttpResponse("Sub")


def add(request):
    if request.GET:
        a = request.GET["a"]
        b = request.GET["b"]
        result = int(a) + int(b)
        return HttpResponse("Result = " + str(result))
    return HttpResponse("Add")


def plus(request):
    a = 0
    b = 0
    result = 0
    if request.GET:
        a = int(request.GET["a"])
        b = int(request.GET["b"])
        result = a + b
    return render(request, "add.html", {"a": a, "b": b, "result": result})


def test(request):
    return render(request, "test.html")


def test1(request):
    return render(request, "test1.html")


def mul(request):
    if request.GET:
        aaa = request.GET["a"]
        bbb = request.GET["b"]
        mult = int(aaa) * int(bbb)
        return HttpResponse("Multiply= " + str(mult))
    return HttpResponse("Mul")


def addsub(request):
    a = 0
    b = 0
    result = 0
    if request.GET:
        a = int(request.GET["a"])
        b = int(request.GET["b"])
        cmd = request.GET["command"]
        if cmd == "Add":
            result = a + b
        if cmd == "Sub":
            result = a - b
        if cmd == "Mul":
            result = a * b
        if cmd == "Div":
            result = a / b
    return render(request, "addsub.html", {"a": a, "b": b, "result": result})


def selectaddsub(request):
    a = 0
    b = 0
    result = 0
    if request.GET:
        a = int(request.GET["a"])
        b = int(request.GET["b"])
        cmd = request.GET["command"]
        if cmd == "Add":
            result = a + b
        if cmd == "Sub":
            result = a - b
        if cmd == "Mul":
            result = a * b
        if cmd == "Div":
            result = a / b
    return render(request, "selectaddsub.html", {"a": a, "b": b, "result": result})


def addsub(request):
    a = 0
    b = 0
    result = 0
    if request.GET:
        a = int(request.GET["a"])
        b = int(request.GET["b"])
        cmd = request.GET["command"]
        if cmd == "Add":
            result = a + b
        elif cmd == "Sub":
            result = a - b
    return render(request, "addsub.html", {"a": a, "b": b, "result": result})


def mcq(request):
    qno = 0
    questions = [("Which is the capital of UP?", "Lucknow", "Tokyo", "Paris", "Hukulganj", 1),
                 ("Which is the capital of Japan?", "Lucknow", "Tokyo", "Paris", "Hukulganj", 2),
                 ("Which is capital of Uttar Pradesh?", "Delhi", "Pune", "Kolkata", "Lucknow", 4)]
    n = len(questions)
    if request.GET:
        qno = int(request.GET["qno"])
        qno += 1
        if qno >= n:
            return HttpResponse("Quiz Over")
    for qno, correct_answer in questions:
        answer = input(f"{qno}? ")
        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"The answer is {correct_answer!r}, not {answer!r}")
    question = questions[qno][0]
    opt1 = questions[qno][1]
    opt2 = questions[qno][2]
    opt3 = questions[qno][3]
    opt4 = questions[qno][4]
    return render(request, "mcqintable.html",
                  {"qno": qno, "question": question, "opt1": opt1, "opt2": opt2, "opt3": opt3, "opt4": opt4})

#
# def session(request):
#     key = " "
#     if request.POST:
#         key = request.POST["key"]
#         try:
#             request.session.pop(key)
#         except:
#             pass
#         return request(request, "sessionremove.html", {"key": key})


def sessionadd(request):
    name = request.GET["name"]
    request.session["data"] = name
    return HttpResponse(name)


def sessionshow(request):
    name = request.session.get("data")
    return HttpResponse(name)

# def session(request):
#     name=request.session.get("mcqintable.html")
#     request.session["data"]=name
#     return HttpResponse(name)
