from django.shortcuts import render

"""
Views.py
요청(request)을 처리할 함수들을 정의하는 파일
"""

# 루트 url (최상위 url)에 접근하면 실행되는 함수
def get_home(request):
    return render(request, "home.html")

# 정답을 입력하고 /result/ url에 접근하면 실행되는 함수
def check_answer(request):
    # 문제 수가 많아진다면 이러한 작업도 반복문 안으로 넣으면 좋을겁니다
    a1 = (request.GET["q1"] == "1")
    a2 = (request.GET["q2"] == "3")
    # a3 = (request.GET["q3"] == "?") 아직 회장을 몰라서 주석 처리
    score = a1 + a2
    return render(request, "result.html", {"a1" : a1, "a2" : a2, "score" : score})
