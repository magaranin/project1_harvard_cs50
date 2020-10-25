from django.shortcuts import render
from . import util
import markdown2
    
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

