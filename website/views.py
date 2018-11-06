from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter
def home(request):
    return render(request,'home.html')
def count(request):
    x=request.GET['text'].split()
    y=len(x)
    x=dict(Counter(x))
    print(x)
    max=0
    for i,j in x.items():
          if max<j:
              item=[i,j]
              max=j
    print(item)  
    print(x)          
    return render(request,'count.html',{'text':request.GET['text'],'w_count':y,'max_word':item[0],'word_count':item[1],'d':x})    
   