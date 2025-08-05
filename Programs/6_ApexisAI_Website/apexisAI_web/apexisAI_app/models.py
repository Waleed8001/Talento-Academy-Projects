from django.db import models

# Create your models here.

# Landing Page Models

class BackgroundImages(models.Model):
    id = models.AutoField(verbose_name="ID", primary_key=True)
    name = models.ImageField(verbose_name="Image", upload_to="images/")
    
    def __str__(self):
        return f"Image {self.id}"

class TransvocalDashboard(models.Model):
    id = models.AutoField(verbose_name="ID", primary_key=True)
    name = models.ImageField(verbose_name="Dashboard", upload_to="images/")
    
    def __str__(self):
        return f"Transvocal {self.id}"
    
class Status(models.Model):
    id = models.AutoField(verbose_name="ID", primary_key=True)
    status = models.CharField(verbose_name="Dashboard", max_length=20, default="200+")
    desc = models.CharField(verbose_name="Dashboard", max_length=50, default="Users Onboard")
    
    def __str__(self):
        return f"{self.status} {self.desc}"
    
class Testimonial(models.Model):
    id = models.AutoField(verbose_name="ID", primary_key=True)
    name = models.CharField(verbose_name="Name", max_length=100, default="Unknown")
    person_designation = models.CharField(verbose_name="Designation", max_length=100, default="Unknown")
    test = models.TextField(verbose_name="Testimonial", max_length=1000, default="Nothing")
    image = models.ImageField(verbose_name="Dashboard", upload_to="images/", default="images/profile logo.jpg", null=True)
    
    def __str__(self):
        return f"Testimonial by {self.name}"
    
class AllHeadingAndDescription(models.Model):
    id = models.AutoField(verbose_name="ID", primary_key=True)
    
    # Hero section
    hero_heading = models.CharField(verbose_name="Hero Section Heading", max_length=100)
    hero_desc = models.TextField(verbose_name="Hero Section Description", max_length=500)
    
    # Transvocal section
    transvocal_heading = models.CharField(verbose_name="Transvocal Heading", max_length=100)
    transvocal_desc = models.TextField(verbose_name="Transvocal Description", max_length=500)
    
    # Status section
    status_heading = models.CharField(verbose_name="Status Heading", max_length=100)
    status_desc = models.TextField(verbose_name="Status Description", max_length=500)
    
    # Marketplace section
    marketplace_heading = models.CharField(verbose_name="Marketplace Heading", max_length=100)
    marketplace_sub_heading = models.CharField(verbose_name="Marketplace Sub-Heading", max_length=100)
    marketplace_desc = models.TextField(verbose_name="Marketplace Description", max_length=500)
    
    # Insights section
    insights_heading = models.CharField(verbose_name="Insights Heading", max_length=100)
    insights_desc = models.TextField(verbose_name="Insights Description", max_length=300)
    
    def __str__(self):
        return f"Heading and Description"
    
class Footer(models.Model):
    spi = {
        "Transvocal": "Transvocal",
        "Interview AI": "Interview AI",
        "Insight": "Insight",
        "Marketplace": "Marketplace",
    }
    
    spi_link = {
        "#transvocal": "Transvocal",
        "#": "Interview AI",
        "#insights": "Insight",
        "#marketplace": "Marketplace",
    }
    
    ac = {
        "About Us": "About Us",
        "Contact Us": "Contact Us",
        "Case Study": "Case Study",
        "Blogs": "Blogs",
        "Events": "Events",
    }
    
    ac_link = {
        "aboutus": "About Us",
        "contactus": "Contact Us",
    }
    
    
    question = models.CharField(verbose_name="Question", max_length=100)
    answer = models.TextField(verbose_name="Answer", max_length=500)
    
    # Facebook
    facebook_logo = models.ImageField(verbose_name="Facebook Logo", upload_to="images/")
    facebook_link = models.URLField(verbose_name="Facebook URL", max_length=1000)
    
    # Twitter
    twitter_logo = models.ImageField(verbose_name="Twitter Logo", upload_to="images/")
    twitter_link = models.URLField(verbose_name="Twitter URL", max_length=1000)
    
    # LinkedIn
    linkedIn_logo = models.ImageField(verbose_name="LinkedIn Logo", upload_to="images/")
    linkedIn_link = models.URLField(verbose_name="LinkedIn URL", max_length=1000)
    
    # Youtube
    youtube_logo = models.ImageField(verbose_name="Youtube Logo", upload_to="images/")
    youtube_link = models.URLField(verbose_name="Youtube URL", max_length=1000)
    
    t = models.CharField(verbose_name="Transvocal Name", choices=spi)
    t_link = models.CharField(verbose_name="Transvocal Link", choices=spi_link)
    
    iai = models.CharField(verbose_name="Interview AI Name", choices=spi)
    iai_link = models.CharField(verbose_name="Interview AI Link", choices=spi_link)
    
    au = models.CharField(verbose_name="About Us Name", choices=ac)
    au_link = models.CharField(verbose_name="About Us Link", choices=ac_link)
    
    cu = models.CharField(verbose_name="Contact Us Name", choices=ac)
    cu_link = models.CharField(verbose_name="Contact Us Link", choices=ac_link)
    
    ins = models.CharField(verbose_name="Insights Name", choices=spi)
    ins_link = models.CharField(verbose_name="Insights Link", choices=spi_link)
    
    mk = models.CharField(verbose_name="Marketplace Name", choices=spi)
    mk_link = models.CharField(verbose_name="Marketplace Link", choices=spi_link)
    
    
    cs = models.CharField(verbose_name="Case Study Name", choices=ac)
    cs_link = models.CharField(verbose_name="Case Study Link", max_length=50, default="#")
    
    b = models.CharField(verbose_name="Blogs Name", choices=ac)
    b_link = models.CharField(verbose_name="Blog Link", max_length=50, default="#")
    
    ev = models.CharField(verbose_name="Events Name", choices=ac)
    ev_link = models.CharField(verbose_name="Events Link", max_length=50, default="#")
    
    con_location = models.CharField(verbose_name="Location", default="Karachi, Pakistan", max_length=50)
    con_email = models.CharField(verbose_name="Email", default="example@yourmail.com", max_length=50)
    con_phone = models.CharField(verbose_name="Phone Number", default="+92 000 000 000", max_length=50)
    
    def __str__(self):
        return f"Footer"

# About Us Page

class AboutUs(models.Model):
    image = models.ImageField(verbose_name="About Us Image", upload_to="images/")
    about_us_heading = models.CharField(verbose_name="About Us Heading", max_length=100, default="No Heading")
    about_us_desc = models.TextField(verbose_name="About Us Description", max_length=500, default="No Description")

    def __str__(self):
        return f"Image {self.about_us_heading}"
    
class MissionAndVisionandTeam(models.Model):
    mission_desc = models.TextField(verbose_name="Mission Description", max_length=1000)
    vision_desc = models.TextField(verbose_name="Vision Description", max_length=1000)
    team_desc = models.TextField(verbose_name="Team Description", max_length=1000)
    
    def __str__(self):
        return f"Mission and Vision and Team Description"
    
class WhatWeDo(models.Model):
    whatwedo_desc = models.TextField(verbose_name="What We Do Description", max_length=500)
    
    def __str__(self):
        return f"What We Do ?"
    
class WhyChooseApexisAI(models.Model):
    WhyChooseApexAI_desc = models.TextField(verbose_name="Why Choose Apexis AI Description", max_length=500)
    
    def __str__(self):
        return f"Why Choose ApexisAI ?"
    
class Team(models.Model):
    id = models.AutoField(verbose_name="ID", primary_key=True)
    image = models.ImageField(verbose_name="Image", upload_to="images/")
    name = models.CharField(verbose_name="Name", max_length=100, default="Unknown")
    designation = models.CharField(verbose_name="Designation", max_length=100, default="Unknown")

    def __str__(self):
        return f"{self.name}"

# Contact Us Page

class ContactUs(models.Model):
    image = models.ImageField(verbose_name="About Us Image", upload_to="images/")
    contact_us_heading = models.CharField(verbose_name="Contact Us Heading", max_length=100)
    contact_us_desc = models.TextField(verbose_name="Contact Us Description", max_length=1000)
    
    def __str__(self):
        return f"{self.contact_us_heading}"
    
class GetInTouchAndLetsWorkTogether(models.Model):
    getintouch_desc = models.TextField(verbose_name="Get In Touch Description", max_length=1000)
    email = models.CharField(verbose_name="Email", max_length=70, default="Email: contact@apexai.com")
    phone = models.CharField(verbose_name="Phone", max_length=70, default="Phone/WhatsApp: +92-XXX-XXXXXXX")
    lets_work_together_desc = models.TextField(verbose_name="Lets Work Together Description", max_length=1000)
    
    def __str__(self):
        return f"Get In Touch and Let\'s Work Together"
    
class ContactUsForm(models.Model):
    id = models.AutoField(verbose_name="ID", primary_key=True)
    full_name = models.CharField(verbose_name="Full Name", max_length=70)
    email = models.CharField(verbose_name="Email", max_length=100)
    phone = models.CharField(verbose_name="Phone Number", max_length=30)
    business = models.CharField(verbose_name="Business/Company Name", max_length=100)
    project = models.CharField(verbose_name="Project in Mind", max_length=100)
    details = models.TextField(verbose_name="Details", max_length=2000)
    
    def __str__(self):
        return f"{self.full_name}"
    
class WhyReachOutToUs(models.Model):
    whyreachouttous_desc = models.TextField(verbose_name="Why Reach Out To Us Description", max_length=300)
    
    def __str__(self):
        return f"Why Reach Out To Us ?"