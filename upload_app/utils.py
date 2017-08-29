from .models import FileModel
import os
import subprocess

from Auth_System import settings


def encode_mp4_to(file_id, hd):
    video = FileModel.objects.get(pk=file_id)
    input_file_path = video.file.path
    filename = os.path.basename(input_file_path)
    output_file_name = os.path.join('upload_file/file/' + hd,  '{}_{}.mp4'.format(filename, hd))
    output_file_path = os.path.join(settings.MEDIA_ROOT, output_file_name)

    subprocess.call(['/usr/bin/ffmpeg', '-i', input_file_path, '-c:a', 'copy', '-s', hd, output_file_path])

    if hd == 'hd480':
        video.mp4_480 = output_file_name
        video.save(update_fields=['mp4_480'])
    elif hd == 'hd720':
        video.mp4_720 = output_file_name
        video.save(update_fields=['mp4_720'])
    else:
        video.mp4_360 = output_file_name
        video.save(update_fields=['mp4_360'])
