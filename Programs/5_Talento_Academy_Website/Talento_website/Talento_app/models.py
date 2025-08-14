from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

# Hero Section
class HeroSection(models.Model):
    title = models.CharField(verbose_name="Title", max_length=50)
    text = models.TextField(verbose_name="Title", max_length=500)
    image1 = models.ImageField(verbose_name="Image 1", upload_to='images/') # 'images/' is the subdirectory within MEDIA_ROOT
    image2 = models.ImageField(verbose_name="Image 2", upload_to='images/') # 'images/' is the subdirectory within MEDIA_ROOT
    image3 = models.ImageField(verbose_name="Image 3", upload_to='images/') # 'images/' is the subdirectory within MEDIA_ROOT
    image4 = models.ImageField(verbose_name="Image 4", upload_to='images/') # 'images/' is the subdirectory within MEDIA_ROOT
    
    def __str__(self):
        return f"Title and Images of Hero Section"
    
# Status Model
class Status(models.Model):
    value = models.CharField(verbose_name="Value", max_length=10, default="10K")
    text = models.TextField(verbose_name="Text", max_length=200, default="Active Students On Website")
    
    def __str__(self):
        return f"{self.value} {self.text}"
    
# Certificate Section
class CertificateSection(models.Model):
    title = models.CharField(verbose_name="Title", max_length=50)
    text = models.TextField(verbose_name="Title", max_length=500)
    simage1 = models.ImageField(verbose_name="Student 1 Image", upload_to='images/') # 'images/' is the subdirectory within MEDIA_ROOT
    simage2 = models.ImageField(verbose_name="Student 2 Image", upload_to='images/') # 'images/' is the subdirectory within MEDIA_ROOT
    cerimage = models.ImageField(verbose_name="Certificate Image", upload_to='images/') # 'images/' is the subdirectory within MEDIA_ROOT
    fbrimage = models.ImageField(verbose_name="FBR Image", upload_to='images/') # 'images/' is the subdirectory within MEDIA_ROOT
    fbrtitle = models.CharField(verbose_name="FBR Title", max_length=50, default="FBR Certificate") # 'images/' is the subdirectory within MEDIA_ROOT
    fbrlink = models.URLField(verbose_name="FBR Link", max_length=100, default="https://fbr.gov.pk/") # 'images/' is the subdirectory within MEDIA_ROOT
    secpimage = models.ImageField(verbose_name="SECP Image", upload_to='images/') # 'images/' is the subdirectory within MEDIA_ROOT
    secptitle = models.CharField(verbose_name="SECP Title", max_length=50, default="SCEP Certificate") # 'images/' is the subdirectory within MEDIA_ROOT
    secplink = models.CharField(verbose_name="SECP Link", max_length=100, default="https://www.secp.gov.pk/") # 'images/' is the subdirectory within MEDIA_ROOT
    
    def __str__(self):
        return f"Certificate Section"
    
# Teacher Model
class Teachers(models.Model):
    id = models.AutoField(verbose_name="ID", primary_key=True)
    name = models.CharField(verbose_name="Name", max_length=100)
    course = models.TextField(verbose_name="Course", max_length=100)
    teacher_image = models.ImageField(verbose_name="Teacher Image", upload_to='images/') # 'images/' is the subdirectory within MEDIA_ROOT
    phone = models.CharField(verbose_name="Phone Number", db_comment="Please start with country code") # 'images/' is the subdirectory within MEDIA_ROOT
    lesson = models.IntegerField(verbose_name="Total Lesson", default=0) # 'images/' is the subdirectory within MEDIA_ROOT
    
    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        if self.phone.startswith("+"):
            return super().save(*args, **kwargs)
        
        else:
            raise ValidationError("Phone number must start with '+'.")
        
    
    
# Course Model
class Courses(models.Model):
    FRESHMAN = "Paid"
    SOPHOMORE = "Unpaid"
    Status_Choice = {
        FRESHMAN: "Paid",
        SOPHOMORE: "Unpaid",
    }
    
    id = models.AutoField(verbose_name="ID", primary_key=True)
    title = models.CharField(verbose_name="Course Name", max_length=50)
    image = models.ImageField(verbose_name="Image", upload_to='images/') # 'images/' is the subdirectory within MEDIA_ROOT
    students = models.IntegerField(verbose_name="Total Students", default=1)
    desc = models.TextField(verbose_name="Description", max_length=2000, default="Right your text here.")
    status = models.CharField(verbose_name="Status", choices=Status_Choice)
    price = models.FloatField(verbose_name="Price", max_length=20)
    teacher = models.ForeignKey(verbose_name="Teacher", on_delete=models.CASCADE, to=Teachers)
    
    def __str__(self):
        return f"{self.title} teach by {self.teacher}"
    
# Workshops and Webinars Model
class Webinars(models.Model):
    id = models.AutoField(verbose_name="ID", primary_key=True)
    name = models.CharField(verbose_name="Webinar Name", max_length=50)
    text = models.CharField(verbose_name="Description", max_length=300) 
    image = models.ImageField(verbose_name="Image", upload_to='images/') # 'images/' is the subdirectory within MEDIA_ROOT
    
    def __str__(self):
        return f"{self.name}"
    

class FrequentlyAskedQuestions(models.Model):
    id = models.AutoField(verbose_name="ID", primary_key=True)
    question = models.TextField(verbose_name="Question", max_length=200)
    answer = models.TextField(verbose_name="Answer", max_length=5000)
        
    def __str__(self):
        return f"{self.question}"
    
    
class ContactUs(models.Model):
    id = models.AutoField(verbose_name="ID", primary_key=True)
    name = models.CharField(verbose_name="Name", max_length=50)
    email_address = models.EmailField(verbose_name="Email Address", max_length=100)
    phone = models.CharField(verbose_name="Phone Number", help_text="Please start with country code") # 'images/' is the subdirectory within MEDIA_ROOT
    comments = models.TextField(verbose_name="Comments", max_length=5000)
        
    def __str__(self):
        return f"{self.name}"
    
    
class Testimonial(models.Model):
    id = models.AutoField(verbose_name="ID", primary_key=True)
    name = models.CharField(verbose_name="Student Name", max_length=50)
    course = models.CharField(verbose_name="Course", max_length=100)
    rating = models.IntegerField(verbose_name="Rating", default=0, validators=[MinValueValidator(0), MaxValueValidator(5)], help_text="Please Enter rating between 0 to 5")
    testimon = models.TextField(verbose_name="Testimonial", max_length=1000)
        
    def __str__(self):
        return f"Testimonial by {self.name}"
    
    
class FooterModel(models.Model):
    URL_Choice = {
        "allcourses": "Courses",
        "allwebinars": "Webinars & Events",
        "aboutus": "About Us",
    }
    
    URL_Choice_2 = {
        "#faq-section": "FAQs",
        "#contactus": "Contact Us",
    }
    
    Text_Choice = {
        "Course": "Course",
        "Events": "Events",
        "About": "About",
    }
    
    Text_Choice_2 = {
        "FAQs": "FAQs",
        "Contact Us": "Contact Us",
    }
    
    id = models.AutoField(verbose_name="ID", primary_key=True)
    text_information = models.CharField(verbose_name="Information text", max_length=50)
    image_1 = models.ImageField(verbose_name="Image 1", upload_to='images/')
    image_2 = models.ImageField(verbose_name="Image 2", upload_to='images/')
    image_3 = models.ImageField(verbose_name="Image 3", upload_to='images/')
    link_1_of_image_1 = models.URLField(verbose_name="Link of Image 1", max_length=500, default="No link")
    link_2_of_image_2 = models.URLField(verbose_name="Link of Image 2", max_length=500, default="No link")
    link_3_of_image_3 = models.URLField(verbose_name="Link of Image 3", max_length=500, default="No link")
    phone_num = models.CharField(verbose_name="Phone Number", max_length=50)
    email = models.EmailField(verbose_name="Email", max_length=50)
    quick_link_text_1 = models.CharField(verbose_name="Quick Link 1", max_length=20, default="No link", choices=Text_Choice)
    quick_link_text_2 = models.CharField(verbose_name="Quick Link 2", max_length=20, default="No link", choices=Text_Choice)
    quick_link_text_3 = models.CharField(verbose_name="Quick Link 3", max_length=20, default="No link", choices=Text_Choice_2)
    quick_link_text_4 = models.CharField(verbose_name="Quick Link 4", max_length=20, default="No link", choices=Text_Choice_2)
    quick_link_text_5 = models.CharField(verbose_name="Quick Link 5", max_length=20, default="No link", choices=Text_Choice)
    quick_link_1 = models.CharField(verbose_name="Quick Link Url 1", max_length=20, default="No link", choices=URL_Choice)
    quick_link_2 = models.CharField(verbose_name="Quick Link Url 2", max_length=20, default="No link", choices=URL_Choice)
    quick_link_3 = models.CharField(verbose_name="Quick Link Url 3", max_length=20, default="No link", choices=URL_Choice_2)
    quick_link_4 = models.CharField(verbose_name="Quick Link Url 4", max_length=20, default="No link", choices=URL_Choice_2)
    quick_link_5 = models.CharField(verbose_name="Quick Link Url 5", max_length=20, default="No link", choices=URL_Choice)
        
    def __str__(self):
        return f"Web Footer"
    




    
    
#     def __str__(self):
#         return f"Title and Images of Hero Section"
# class HeroSection(models.Model):
#     title = models.CharField(verbose_name="Title", max_length=50)
#     text = models.TextField(verbose_name="Title", max_length=500)
#     image1 = models.ImageField(upload_to='images/') # 'images/' is the subdirectory within MEDIA_ROOT
#     image2 = models.ImageField(upload_to='images/') # 'images/' is the subdirectory within MEDIA_ROOT
#     image3 = models.ImageField(upload_to='images/') # 'images/' is the subdirectory within MEDIA_ROOT
#     image4 = models.ImageField(upload_to='images/') # 'images/' is the subdirectory within MEDIA_ROOT
    
#     def __str__(self):
#         return f"Title and Images of Hero Section"
# class HeroSection(models.Model):
#     title = models.CharField(verbose_name="Title", max_length=50)
#     text = models.TextField(verbose_name="Title", max_length=500)
#     image1 = models.ImageField(upload_to='images/') # 'images/' is the subdirectory within MEDIA_ROOT
#     image2 = models.ImageField(upload_to='images/') # 'images/' is the subdirectory within MEDIA_ROOT
#     image3 = models.ImageField(upload_to='images/') # 'images/' is the subdirectory within MEDIA_ROOT
#     image4 = models.ImageField(upload_to='images/') # 'images/' is the subdirectory within MEDIA_ROOT
    
#     def __str__(self):
#         return f"Title and Images of Hero Section"
