from django.shortcuts import render
from django.http import HttpResponse
from .models import BackgroundImages, TransvocalDashboard, Status, Testimonial, AllHeadingAndDescription, Footer, AboutUs, MissionAndVisionandTeam, WhatWeDo, WhyChooseApexisAI, Team, ContactUs, GetInTouchAndLetsWorkTogether, ContactUsForm, WhyReachOutToUs

# Create your views here.

def MyPlatform(request):
    image = BackgroundImages.objects.all()
    dashboard = TransvocalDashboard.objects.all()
    status = Status.objects.all()
    testimon = Testimonial.objects.all()
    head_desc = AllHeadingAndDescription.objects.first()
    footer = Footer.objects.first()
    
    # print(testimon)
    all_items = {
        "all_image": image,
        "all_dashboard": dashboard,
        "all_status": status,
        "all_testimonial": testimon,
        "all_head_desc": head_desc,
        "all_footer": footer,
    }
    return render(request, "apexisAI_app/index.html", all_items)
    # return HttpResponse("WOW")
    
    
def MyAboutus(request):
    about_us = AboutUs.objects.first()
    mvt = MissionAndVisionandTeam.objects.first()
    wwd = WhatWeDo.objects.all()
    wcaai = WhyChooseApexisAI.objects.all()
    team = Team.objects.all()
    footer = Footer.objects.first()
    
    all_items = {
        "all_about_us": about_us,
        "all_mvt": mvt,
        "all_whatwedo": wwd,
        "all_wcaai": wcaai,
        "all_team": team,
        "all_footer": footer,
    }
    return render(request, "apexisAI_app/aboutus.html", all_items)
    # return HttpResponse("WOW")
    
def MyContactus(request):
    contact_us = ContactUs.objects.first()
    touch = GetInTouchAndLetsWorkTogether.objects.first()
    reach = WhyReachOutToUs.objects.all()
    footer = Footer.objects.first()
    
    if request.method == "POST":
        full_name = request.POST.get("full-name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        company = request.POST.get("company", "")
        project = request.POST.get("project-type", "")
        detail = request.POST.get("details", "")
    
    
        if ContactUsForm.objects.filter(full_name=full_name, email=email, phone=phone, business=company, project=project, details=detail).exists():
            message = "Thank you for contacting us!"
            all_items = {
                "all_contact_us": contact_us,
                "all_touch": touch,
                "all_reach": reach,
                "all_footer": footer,
                "contact_message": message,
            }
            return render(request, "apexisAI_app/contactus.html", all_items)

        else:
            create_table = ContactUsForm.objects.create(full_name=full_name, email=email, phone=phone, business=company, project=project, details=detail)
            create_table.save()
            message = "Thank you for contacting us"
            all_items = {
                "all_contact_us": contact_us,
                "all_touch": touch,
                "all_reach": reach,
                "all_footer": footer,
                "contact_message": message,
            }
            return render(request, "apexisAI_app/contactus.html", all_items)
    
    all_items = {
        "all_contact_us": contact_us,
        "all_touch": touch,
        "all_reach": reach,
        "all_footer": footer,
    }
    return render(request, "apexisAI_app/contactus.html", all_items)
    # return HttpResponse("WOW")