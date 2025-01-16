from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FileUploadForm
# Create your views here.
@login_required
def view_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = request.user
            upload.save()
            return redirect('/')

        else:
            context = {'form': form}
            return render(request, 'upload/index.html', context)
    context = {'form':FileUploadForm()}

    return render(request, 'upload/index.html', context)