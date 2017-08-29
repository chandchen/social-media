from celery.decorators import task
from celery.utils.log import get_task_logger

from .utils import encode_mp4, generate_thumbnail

logger = get_task_logger(__name__)


@task(name="transcode_video_task")
def transcode_video_task(file_id, hd):
    logger.info("Transcode video success")
    return encode_mp4(file_id, hd)


@task(name="generate_thumbnail_task")
def generate_thumbnail_task(file_id):
    logger.info("Generate thumbnail success")
    return generate_thumbnail(file_id)
