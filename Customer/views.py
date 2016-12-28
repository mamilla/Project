from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from . models import Customer, Transaction

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

from collections import defaultdict

def upload_file(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
          
            words= request.FILES['files'].read()
            num = int(form.cleaned_data["number"])
            print(type(words))
            print(type(num))
            
            d = defaultdict(int)
            for word in words.split():
                d[word] += 1
            print(d)
            d1={}
            T=True
            for i in d:
                if d[i]==num:
                    d1[i]=d[i]
            return render(request, 'uploadfile.html', {'d1': d1,'T':T,'num':num})
		    #return HttpResponseRedirect('home/')
            #return render(request, 'showdata.html', {'d1': d1,"num":num})

    else:
        form = UploadFileForm()
    return render(request, 'uploadfile.html', {'form': form})


def transactiondetail(request):
	data = Transaction.objects.all()
	context = {"data":data}
	return render(request, "transactiondetail.html",context)

# def customerdetail(request):
#     data = Customer.objects.all()
#     context = {"data": data}
#     return render(request, "customerdetail.html", context)
