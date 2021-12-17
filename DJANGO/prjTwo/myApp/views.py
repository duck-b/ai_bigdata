from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
memberid = ''
memberemail = ''
def index(request):
    global memberid
    return render(request, 'myApp/login.html')

def loginCon(request):
    global memberemail
    global memberid
    email = request.POST['email']

    memberemail = email
    # DB에서 email select 하고, 없으면 insert 후에 ID 값 가져오기
    
    id = 123
    return redirect(f'/user/')

def user(request):
    # DB에서 ID 값으로 전체 저장 목록 가져오기
    global memberid
    global memberemail
    context = {
        'memberid': memberid,
        'memberemail': memberemail
    }
    return render(request, 'myApp/user.html', context)

def userWeek(request, week):
    # DB에서 ID 값으로 요일 저장 목록 가져오기
    global memberid
    global memberemail
    context = {
        'memberid': memberid,
        'memberemail': memberemail,
        'week': week
    }
    return render(request, 'myApp/user.html', context)

def search(request):
    global memberid
    context = {
        'memberid': memberid
    }
    try:
        search = request.GET['search']
        # DB에서 작품명 또는 작가명으로 검색
    except:
        search = ''
    context = {
        'memberid': memberid,
        'search': search
    }
    return render(request, 'myApp/search.html', context)

def createSearchCon(request, webtoonid):
    # 웹툰 저장
    return redirect(f'/user/')

def deleteSearchCon(request, webtoonid):
    # 웹툰 삭제
    return redirect(f'/user/')

def webtoon(request, webtoonid):
    # webtoon으로 작품 검색
    global memberid
    context = {
        'memberid': memberid,
        'webtoonid': webtoonid
    }
    return render(request, 'myApp/webtoon.html', context)

def createComment(request, webtoonid):
    global memberid
    context = {
        'memberid': memberid,
        'webtoonid': webtoonid
    }
    return render(request, 'myApp/createComment.html', context)

def createCommentCon(request, webtoonid):
    # id, webtoonid으로 코멘트 수정
    global memberid
    context = {
        'memberid': memberid,
        'webtoonid': webtoonid,
    }
    return redirect(f'/user/webtoon/{webtoon}/')

def updateComment(request, webtoonid):
    # id, webtoonid으로 코멘트 검색
    global memberid
    context = {
        'memberid': memberid,
        'webtoonid': webtoonid,
        'comment': 'Test'
    }
    return render(request, 'myApp/updateComment.html', context)

def updateCommentCon(request, webtoonid):
    # id, webtoonid으로 코멘트 수정
    global memberid
    context = {
        'memberid': memberid,
        'webtoonid': webtoonid,
    }
    return redirect(f'/user/webtoon/{webtoon}/')

def deleteCommentCon(request, webtoonid):
    global memberid
    # id, webtoonid으로 코멘트 삭제
    return redirect(f'/user/webtoon/{webtoon}/')