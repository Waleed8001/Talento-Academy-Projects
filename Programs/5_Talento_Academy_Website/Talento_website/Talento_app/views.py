from django.shortcuts import render
from django.http import HttpRequest
from .models import HeroSection, CertificateSection, Status, Courses, Teachers, Webinars, Testimonial, FrequentlyAskedQuestions, ContactUs, FooterModel

# Create your views here.

def home(request):
    allpic = HeroSection.objects.first()
    stats = Status.objects.all()
    certificate = CertificateSection.objects.first()
    course = Courses.objects.all()[:6]
    webinar = Webinars.objects.all()[:3]
    testimonial = Testimonial.objects.all()
    faqs = FrequentlyAskedQuestions.objects.all()
    footer = FooterModel.objects.first()
    # print(footer.quick_link_1)
    
    mydict = {
        "pics": allpic,
        "stats": stats,
        "certificate": certificate,
        "courses": course,
        "webinars": webinar,
        "testimonial": testimonial,
        "faqs": faqs,
        "footer": footer,
    }
    
    
    return render(request, "Talento_app\\my.html", mydict)


def filteredcourse(request):
    courses = request.GET.get('course', ' ')
    footer = FooterModel.objects.first()
    
    all_course = Courses.objects.filter(title__icontains=courses)
    
        
    mydict = {
        "course": all_course,
        "footer": footer
    }
 
    return render(request, "Talento_app\\filteredcourse.html", mydict)

def Allcourse(request):    
    all_course = Courses.objects.all()
    footer = FooterModel.objects.first()
        
    mydict = {
        "course": all_course,
        "footer": footer,
    }
 
    return render(request, "Talento_app\\allcourses.html", mydict)

def selectedcourse(request, id):    
    all_course = Courses.objects.get(id=id)
    footer = FooterModel.objects.first()
    print(all_course)
        
    mydict = {
        "course": all_course,
        "footer": footer,
    }
 
    return render(request, "Talento_app\\selectedcourse.html", mydict)
        
def aboutus(request):
    teacher = Teachers.objects.all()
    footer = FooterModel.objects.first()
    
    mydict = {
        "teachers": teacher,
        "footer": footer
    }
    
    return render(request, "Talento_app\\aboutus.html", mydict)

def AllWebinars(request):
    webinars = Webinars.objects.all()
    footer = FooterModel.objects.first()
    
    mydict = {
        "webinars": webinars,
        "footer": footer
    }
    
    return render(request, "Talento_app\\allwebinars.html", mydict)

def Contact_Us(request):
    footer = FooterModel.objects.first()
    
    if request.method == "POST":
        name = request.POST.get('name', "")
        email_address = request.POST.get('email', "")
        phone = request.POST.get('phone', "")
        comments = request.POST.get('comments', "")

        contact = ContactUs(name=name, email_address=email_address, phone=phone, comments=comments)
        contact.save()
        
    return render(request, 'Talento_app\\contactus.html', {"footer": footer})

def AllTestimonial(request):
    testimonial = Testimonial.objects.all()
    footer = FooterModel.objects.first()
    
    mydict = {
        "testimonial": testimonial,
        "footer": footer
    }
        
    return render(request, 'Talento_app\\alltestimonial.html', mydict)