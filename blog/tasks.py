from celery.decorators import task
from celery.utils.log import get_task_logger
from django.core.mail import send_mail

logger = get_task_logger(__name__)


@task(name="send_post_email_task")
def send_post_email_task(subject, message, mail_from, mail_to):
    """sends an email when post form is filled successfully"""
    logger.info("Sent post email")
    return send_mail(subject, message, mail_from, mail_to)
