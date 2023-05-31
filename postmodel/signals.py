from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post


@receiver(post_save, sender=Post)
def send_email_notification(sender, instance, created, **kwargs):
    if created:
        subject = 'New Post Created'
        message = f'A new post "{instance.title}" has been created by {instance.author}.'
        sender_email = 'your-email@example.com'
        recipient_email = instance.author.email
        send_mail(subject, message, sender_email, [recipient_email])
