from django.shortcuts import redirect, render
# 추가
from django.http import HttpResponse
# 모델 임포트 추가
from .models import Student, City
# Create your views here.
# /, /myApp/ 연결 뷰함수
def index(request):
    return HttpResponse('<h1 align="center">Hello World!</h1>')

def sub1(request):
    return render(request, 'myApp/sub1.html')

def sub2(request):
    return render(request, 'myApp/sub2.html')
    
def sub3(request):
    context = {
        'name': '임영웅',
        'id': 'YYY',
        'age': 34,
        'grade': [90, 85, 77]
    }
    return render(request, 'myApp/sub3.html', context)

def sub4(request):
    book_info = [
        ('title', '어린왕자'),
        ('writer', '생텍쥐페리'),
        ('price', 15000),
        ('ISBN', '483731-849-90'),
    ]
    student_info = [
        ('홍길동', '남', '부산', 23),
        ('고길동', '남', '전주', 28),
        ('윤길동', '남', '서울', 23),
        ('박길동', '남', '마산', 23),
        ('정길순', '여', '울산', 22),
    ]
    context = {
        'book_info':book_info,
        'student_info':student_info,
        'numList': range(1, 101, 2)
    }
    return render(request, 'myApp/sub4.html', context)

def sub5(request):
    book_list = [
        ('파이썬 도장', 33000),
        ('C언어', 23000),
        ('JAVA', 43000),
    ]
    context = {
        'book_list':book_list
    }
    return render(request, 'myApp/sub5.html', context)

def sub6(request):
   return render(request, 'myApp/sub6.html')

def numberCon(request):
    number = request.GET['number']
    try:
        number = int(number)
    except:
        result = '숫자가 아닙니다.'
    else:
        if number%2 == 0:
            result = '짝수'
        else:
            result = '홀수'
    # return HttpResponse(result)
    context = {
        'result': result,
        'number': number
    }
    return render(request, 'myApp/sub6_result.html', context)

def sub7(request):
    return render(request, 'myApp/sub7.html')

def animalCon(request):
    animal_list = ['원숭이', '닭', '개', '돼지', '쥐', '소', '범', '토끼', '용', '뱀', '말', '양']
    birth = request.GET['birth']
    animal = animal_list[int(birth)%12]
    context = {
        'animal': animal,
        'birth': birth
    }
    return render(request, 'myApp/sub7_result.html', context)

def sub8(request):
    return render(request, 'myApp/sub8.html')

def messageCon(request):
    userName = request.POST['userName']
    result = f'{userName} 님... 오늘도 편안한 하루 되세요'
    context = {
        'result': result
    }
    return render(request, 'myApp/sub8_result.html', context)

def sub9(request):
    return render(request, 'myApp/sub9.html')

def calculatorCon(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    if num2 == 0:
        result4 = '0으로 나눌 수 없습니다.'
    else:
        result4 = f'{num1} / {num2} = {round(num1/num2, 2)}'
    context = {
        'result1': f'{num1} + {num2} = {num1+num2}',
        'result2': f'{num1} - {num2} = {num1-num2}',
        'result3': f'{num1} * {num2} = {num1*num2}',
        'result4': result4
    }
    return render(request, 'myApp/sub9_result.html', context)

def sub10(request):
    return render(request, 'myApp/sub10.html')

def sub11(request):
    return render(request, 'myApp/sub11.html')

def sub12(request):
    return render(request, 'myApp/sub12.html')

def all(request):
    # Student 테이블 모델 레크드 저장
    student_list = Student.objects.all()
    context = {
        'student_list': student_list
    }
    return render(request, 'myApp/all.html', context)

def detail(request, id):
    student = Student.objects.get(id = id)
    context = {
        'student': student
    }
    return render(request, 'myApp/detail.html', context)

def register(request):
    return render(request, 'myApp/register.html')

def registerCon(request):
    name = request.POST['name']
    major = request.POST['major']
    age = request.POST['age']
    grade = request.POST['grade']
    gender = request.POST['gender']

    student = Student(s_name = name, s_major = major, s_age = age, s_grade = grade, s_gender = gender)
    student.save()

    return redirect('/myApp/all/')

def wipe(request, id):
    student = Student.objects.get(id = id)
    student.delete()

    return redirect('/myApp/all/')


def modify(request, id):
    student = Student.objects.get(id = id)
    context = {
        'student': student
    }
    return render(request, 'myApp/modify.html', context)

def modifyCon(request):
    id = request.POST['id']
    name = request.POST['name']
    major = request.POST['major']
    age = request.POST['age']
    grade = request.POST['grade']
    gender = request.POST['gender']
    
    student = Student.objects.get(id = id)
    student.s_name = name
    student.s_major = major
    student.s_age = age
    student.s_grade = grade
    student.s_gender = gender
    student.save()

    return redirect('/myApp/all/')

def city(request):
    city_list = City.objects.all()
    context = {
        'city_list': city_list
    }
    return render(request, 'myApp/city.html', context)