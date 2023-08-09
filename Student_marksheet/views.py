from django.shortcuts import render
from Student_marksheet.models import student_info, student_marks

# Create your views here.

def index(request):
    return render(request, 'index.html')


def marksheet(request):
    return render(request, 'marksheet.html')


def saveinfo(request):
    name = request.POST['txtname']
    fname = request.POST['txtfname']
    inst_name = request.POST['txtins']
    batch = request.POST['txtbatch']

    dlt_info = student_info.objects.all()
    dlt_info.delete()
 
    info_obj =  student_info(Name = name, F_name = fname, I_name = inst_name, Batch = batch) 
    info_obj.save()

    sub1 = request.POST['txtoffice'] 
    sub2 = request.POST['txtweb'] 
    sub3 = request.POST['txtit'] 
    sub4 = request.POST['txtc'] 

    dlt_marks = student_marks.objects.all()
    dlt_marks.delete()

    marks_obj = student_marks(Sub1 = sub1, Sub2 = sub2, Sub3 = sub3, Sub4 = sub4)
    marks_obj.save()

    info_obj = student_info.objects.all()
    marks_obj=student_marks.objects.all()
   
    Total = int(sub1) + int(sub2) + int(sub3) + int(sub4)

    percentage = (Total / 400)*100 

    if percentage >= 75:
        grade = 'A'
    elif percentage < 75 and percentage >= 50:
        grade = 'B'
    elif percentage < 50 and percentage >= 25:   
        grade = 'C'
    else:
        grade = 'D'  

    return render(request, 'index.html', {'info_obj':info_obj, 'marks_obj':marks_obj, 'Total':Total, 'percentage':percentage, 'grade' : grade})


 
    
