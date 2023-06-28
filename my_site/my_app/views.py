from django.shortcuts import render

# Create your views here.

def example_view(request):
    # my_app/templates/my_app/example.html
    return render(request, 'my_app/example.html')


def variable_view(request):
    
    
    
    my_var = {'first_name': 'John','last_name': 'Doe',  # 딕셔너리 형태로 변수를 만들어서 템플릿에 전달
              'some_list':[1,2,3],  'some_dict':{'inside_key':'inside_value'} } 
    
    return render(request, 'my_app/variable.html', context=my_var)  # (요청 객체, 템플릿 파일, 딕셔너리 형태의 변수)