from django.core.mail import send_mail,EmailMultiAlternatives
from slmApp.models import Classes
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# returns "successful" or "unsuccesful"
def send_grades(Cpk, grades, request):
    class_inst = Classes.objects.get(pk=Cpk)
    instructors = class_inst.instructor.all()

    subject = class_inst.name+" Grades"
    email_description = "Do not reploy to this email.  If you have questions, email: "
    for instructor in instructors:
        email_description += instructor.email+"  "

    sender = "noreply"
    receivers = []
    for student in class_inst.students.all():
        receivers.append(student.email)
    
    context = {'classes': class_inst, 'grades':grades, 'user':request.user,'email_description':email_description}
    html_content = render_to_string('gradebook_email.html',context) # render with dynamic value
    
    # remove all a tags from the "header" block


    text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.

    # create the email, and attach the HTML version as well.
    msg = EmailMultiAlternatives(subject, text_content, sender, receivers)
    msg.attach_alternative(html_content, "text/html")
    status = msg.send()

    if status==0:
        return "unsuccesful"
    else: 
        return "successful"