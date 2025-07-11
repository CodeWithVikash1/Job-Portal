from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date
# Create your views here.

def index(request):
    return render(request,'index.html')

def admin_login(request):
    error =""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"

    return render(request,'admin_login.html',{'error':error})

def recruiter_login(request):
    error = ""
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email,password=password)
        if user:
            try:
                user1 = Recruiter.objects.get(user=user)
                if user1.type == "recruiter" and user1.status!="Pending":
                    login(request,user)
                    error = "no"
                else:
                    error = "not"
            except:
                error = "yes"
        else:
            error = "yes"
    return render(request,'recruiter_login.html',{'error':error})

def user_login(request):
    error = ""
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email,password=password)
        if user:
            try:
                user1 = StudentUser.objects.get(user=user)
                if user1.type == "student":
                    login(request,user)
                    error = "no"
                else:
                    error = "yes"
            except:
                error = "yes"
        else:
            error = "yes"
    return render(request,'user_login.html',{'error':error})

def user_signup(request):
    error = ""
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        gender = request.POST.get('gender')
        image = request.FILES.get('image')

        try:
          user =  User.objects.create_user(first_name=first_name,last_name=last_name,username=email,password=password)
          StudentUser.objects.create(user=user,mobile=contact,image=image,gender=gender,type="student")
          error = "no"
        except Exception as e:
            print(e)
            error = "yes"

    return render(request,'user_signup.html',{'error':error})

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = request.user
    student = StudentUser.objects.get(user=user)
    error = ""
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        contact = request.POST.get('contact')        
        gender = request.POST.get('gender')
        

        student.user.first_name = first_name
        student.user.last_name = last_name
        student.mobile = contact
        student.gender = gender
        try:
            student.save()
            student.user.save()
            error = "no"
        except Exception as e:
            print(e)
            error = "yes"
        if 'image' in request.FILES:
            image = request.FILES.get('image')
            student.image = image
        try:
            student.save()
            error = "no"
        except:
            pass
    return render(request,'user_home.html',{'error':error,'student':student})

def Logout(request):
    logout(request)
    return redirect('index')

def recruiter_signup(request):
    error = ""
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        contact = request.POST.get('contact')
        company = request.POST.get('company')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        gender = request.POST.get('gender')
        image = request.FILES.get('image')

        try:
          user =  User.objects.create_user(first_name=first_name,last_name=last_name,username=email,password=password)
          Recruiter.objects.create(user=user,mobile=contact,company=company,image=image,gender=gender,type="recruiter",status="Pending")
          error = "no"
        except Exception as e:
            print(e)
            error = "yes"
    return render(request,'recruiter_signup.html',{'error':error})

def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    error = ""
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        contact = request.POST.get('contact')        
        gender = request.POST.get('gender')
        

        recruiter.user.first_name = first_name
        recruiter.user.last_name = last_name
        recruiter.mobile = contact
        recruiter.gender = gender
        try:
            recruiter.save()
            recruiter.user.save()
            error = "no"
        except Exception as e:
            print(e)
            error = "yes"
        if 'image' in request.FILES:
            image = request.FILES.get('image')
            recruiter.image = image
        try:
            recruiter.save()
            error = "no"
        except:
            pass

    return render(request,'recruiter_home.html',{'recruiter':recruiter,'error':error})

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    rcount = Recruiter.objects.all().count()
    ucount = StudentUser.objects.all().count()
    return render(request,'admin_home.html',{'rcount':rcount,'ucount':ucount})

def view_users(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = StudentUser.objects.all()
    return render(request,'view_users.html',{'data':data})

def delete_user(request,pk):
    student = User.objects.get(id=pk)
    student.delete()    
    return redirect('view_users')

def pending_recruiters(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status="Pending")
    return render(request,'pending_recruiters.html',{'data':data})

def change_status(request,pk):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    recruiter = Recruiter.objects.get(id=pk)
    if request.method == "POST":
        status = request.POST.get('status')
        recruiter.status = status
        try:
            recruiter.save()
            error = "no"
        except:
            error = "yes"
    return render(request,'change_status.html',{'recruiter':recruiter, 'error':error})

def accepted_recruiters(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status="Accept")
    return render(request,'accepted_recruiters.html',{'data':data})

def rejected_recruiters(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status="Reject")
    return render(request,'rejected_recruiters.html',{'data':data})

def all_recruiters(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.all()
    return render(request,'all_recruiters.html',{'data':data})

def delete_recruiter(request,pk):
    recruiter = User.objects.get(id=pk)
    recruiter.delete()
    return redirect('all_recruiters')

def change_password_admin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method == "POST":
        currentpassword = request.POST.get('currentpassword')
        newpassword = request.POST.get('newpassword')
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(currentpassword):
                u.set_password(newpassword)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"    
    return render(request,'change_password_admin.html',{'error':error})

def change_password_user(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error = ""
    if request.method == "POST":
        currentpassword = request.POST.get('currentpassword')
        newpassword = request.POST.get('newpassword')
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(currentpassword):
                u.set_password(newpassword)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"    
    return render(request,'change_password_user.html',{'error':error})

def change_password_recruiter(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error = ""
    if request.method == "POST":
        currentpassword = request.POST.get('currentpassword')
        newpassword = request.POST.get('newpassword')
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(currentpassword):
                u.set_password(newpassword)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"    
    return render(request,'change_password_recruiter.html',{'error':error})

def add_job(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login') 
    try:
        recruiter = Recruiter.objects.get(user=request.user)
    except Recruiter.DoesNotExist:
        return redirect('recruiter_signup')
    error = ""
    if request.method == "POST":
        title = request.POST.get('jobtitle')
        start_date = request.POST.get('sdate')
        end_date = request.POST.get('edate')
        salary = request.POST.get('salary')
        company_logo = request.FILES.get('logo')
        experience = request.POST.get('experience')
        location = request.POST.get('location')
        skills = request.POST.get('skills')
        description = request.POST.get('description')
        try:
            Job.objects.create(recruiter=recruiter,title=title,start_date=start_date,end_date=end_date,salary=salary,company_logo=company_logo,experience=experience,location=location,skills=skills,description=description,creation_date=date.today())
            error = "no"
        except:
            error = "yes"
    return render(request,'add_job.html',{'error':error})

def job_list(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    data = Job.objects.filter(recruiter=recruiter)
    return render(request,'job_list.html',{'data':data})

def delete_job(request,pk):
    job = Job.objects.get(id=pk)
    job.delete()
    return redirect('job_list')

def edit_job_detail(request,pk):
    if not request.user.is_authenticated:
        return redirect('recruiter_login') 
    error = ""
    job = Job.objects.get(id=pk)
    if request.method == "POST":
        title = request.POST.get('jobtitle')
        start_date = request.POST.get('sdate')
        end_date = request.POST.get('edate')
        salary = request.POST.get('salary')
        experience = request.POST.get('experience')
        location = request.POST.get('location')
        skills = request.POST.get('skills')
        description = request.POST.get('description')

        job.title = title
        job.salary = salary
        job.experience = experience
        job.location = location
        job.skills = skills
        job.description = description
        try:
            job.save()
            error = "no"
        except:
            error = "yes"
        
        if start_date:
            try:
                job.start_date = start_date
                job.save()
            except:
                pass
        else:
            pass

        if end_date:
            try:
                job.end_date = end_date
                job.save()
            except:
                pass
        else:
            pass

    return render(request,'edit_job_detail.html',{'error':error,'job':job})

def change_company_logo(request,pk):
    if not request.user.is_authenticated:
        return redirect('recruiter_login') 
    error = ""
    job = Job.objects.get(id=pk)
    if request.method == "POST":
        company_logo = request.FILES.get('logo')
        job.company_logo = company_logo
        try:
            job.save()
            error = "no"
        except:
            error = "yes"
        

    return render(request,'change_company_logo.html',{'error':error,'job':job})

def latest_jobs(request):
    data = Job.objects.all().order_by('-start_date')
    return render(request,'latest_jobs.html',{'data':data})

def job_list_user(request):
    job = Job.objects.all().order_by('-start_date')
    user = request.user
    student = StudentUser.objects.get(user=user)
    data = Apply.objects.filter(student=student)
    list = []
    for d in data:
        list.append(d.job.id)
    return render(request,'job_list_user.html',{'job':job,'list':list})

def job_detail(request,pk):
    if not request.user.is_authenticated:
        return redirect('user_login') 
    data = Job.objects.get(id=pk)
    return render(request,'job_detail.html',{'data':data})

def apply_for_job(request,pk):
    if not request.user.is_authenticated:
        return redirect('user_login') 
    error = ""
    user = request.user
    student = StudentUser.objects.get(user=user)
    job = Job.objects.get(id=pk)
    date1 = date.today()
    if job.end_date < date1:
        error = "close"
    elif job.start_date > date1:
        error = "notopen"
    else:
        if request.method == "POST":
            resume = request.FILES.get('resume')
            Apply.objects.create(job=job, student=student, resume=resume, apply_date = date.today())
            error = "done"
    return render(request,'apply_for_job.html',{'error':error})

def candidate_applied(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login') 
    data = Apply.objects.all()
    return render(request,'candidate_applied.html',{'data':data})

def delete_candidate_application(request,pk):
    apply = Apply.objects.get(id=pk)
    apply.delete()
    return redirect('candidate_applied')

def contact(request):
    return render(request,'contact.html')