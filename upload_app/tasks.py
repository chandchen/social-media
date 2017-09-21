from Auth_System.celery import app

from celery.utils.log import get_task_logger

from .utils import encode_mp4, generate_thumbnail

logger = get_task_logger(__name__)


@app.task
def greet_every_15_seconds():
    logger.info('Greet every 15 seconds success')
    print('Hello world!')


@app.task(name="transcode_video_task")
def transcode_video_task(file_id, hd):
    logger.info("Transcode video success")
    return encode_mp4(file_id, hd)


@app.task(name="generate_thumbnail_task")
def generate_thumbnail_task(file_id):
    logger.info("Generate thumbnail success")
    return generate_thumbnail(file_id)
