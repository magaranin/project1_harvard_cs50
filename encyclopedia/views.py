from django.shortcuts import render
from . import util
from django.http import HttpResponseRedirect
import markdown2
from django import forms
from django.urls import reverse

class new_entry_form(forms.Form):
    entry = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control col-md-8 col-lg-8'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control col-md-8 col-lg-10', 'rows' : 10}))
    
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, title):
    file_content = util.get_entry(title)
    if (file_content):
        file_content = markdown2.markdown(file_content)
    return render(request, "encyclopedia/entry_page.html", {
        "content": file_content
    })

def create_new_entry(request):
    if request.method == "POST":
        form = new_entry_form(request.POST)
        if form.is_valid():
            title = form.cleaned_data["entry"]
            content = form.cleaned_data["content"]
            if title.upper() in [element.upper() for element in util.list_entries()]:
                return error_page(request, "This entry already exists!")              
            else:
                util.save_entry(title,content)
                return HttpResponseRedirect(reverse("entry_page", kwargs={'title': title}))
    return render(request, "encyclopedia/create_new_entry.html", {
        "form": new_entry_form()
    })

def search(request):
    value = request.GET['q']
    if util.get_entry(value): #request=title
        return HttpResponseRedirect(reverse("entry_page", kwargs={'title': value}))
    else: #request !=title
        selected_values = []
        for entry in util.list_entries():
            if value.upper() in entry.upper():
                selected_values.append(entry)
        if len(selected_values)==0:
            return error_page(request, "No entry has been found!")
    return render(request, "encyclopedia/index.html", {
        "entries": selected_values
    })
        
def error_page(request, error):
    return render(request, "encyclopedia/error_page.html", {
        'error': error
    })


