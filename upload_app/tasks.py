from celery.decorators import task
from celery.utils.log import get_task_logger

from .utils import encode_mp4_to

logger = get_task_logger(__name__)


@task(name="transcode_video_task")
def transcode_video_task(file_id, hd):
    """Transcode a video when file form is filled successfully"""
    logger.info("Transcode video success")
    return encode_mp4_to(file_id, hd)
