from .models import FileModel
import os
import subprocess

from Auth_System import settings


def encode_mp4(file_id, hd):
    video = FileModel.objects.get(pk=file_id)
    input_file_path = video.file.path
    filename = os.path.basename(input_file_path)
    output_file_name = os.path.join('upload_file/file/' + hd, '{}_{}.mp4'.format(filename, hd))
    output_file_path = os.path.join(settings.MEDIA_ROOT, output_file_name)
    subprocess.call(['/usr/bin/ffmpeg', '-i', input_file_path, '-c:a', 'copy', '-s', hd, output_file_path])

    output_file_name_logo = os.path.join('upload_file/file/' + hd, '{}_{}_logo.mp4'.format(filename, hd))
    output_file_path_logo = os.path.join(settings.MEDIA_ROOT, output_file_name_logo)
    logo_path = os.path.join(settings.MEDIA_ROOT, 'upload_file/logo.png')
    # subprocess.call(['/usr/bin/ffmpeg', '-i', output_file_path, '-i', logo_path, '-c:a', 'copy',
    #                  '-filter_complex', 'overlay=W-w', output_file_path_logo])
    if hd == "hd480":
        logo_hight = 48 * 2
        logo_pos = 480 / 10
    elif hd == "hd720":
        logo_hight = 72 * 2
        logo_pos = 720 / 10
    elif hd == "640X360":
        logo_hight = 36 * 2
        logo_pos = 360 / 10
    else:
        logo_hight = 50
        logo_pos = 20
    utils = 'movie=' + logo_path + ',scale=' + str(logo_hight) + ':' + str(logo_hight) + \
            '[logo];[in][logo]overlay=W-w-' + str(logo_pos) + ':' + str(logo_pos) + '[out]'

    subprocess.call(['/usr/bin/ffmpeg', '-i', output_file_path, '-i', logo_path, '-c:a', 'copy', '-y',
                     '-vf', utils, output_file_path_logo])

    if hd == 'hd480':
        video.mp4_480 = output_file_name_logo
        video.save(update_fields=['mp4_480'])
    elif hd == 'hd720':
        video.mp4_720 = output_file_name_logo
        video.save(update_fields=['mp4_720'])
    else:
        video.mp4_360 = output_file_name_logo
        video.save(update_fields=['mp4_360'])


def generate_thumbnail(file_id):
    file = FileModel.objects.get(pk=file_id)
    input_file_path = file.file.path
    filename = os.path.basename(input_file_path)
    output_image_name = os.path.join('upload_file/file/thumbnail/', '{}.jpg'.format(filename))
    output_image_path = os.path.join(settings.MEDIA_ROOT, output_image_name)
    subprocess.call(['/usr/bin/ffmpeg', '-i', input_file_path, '-y', '-f',
                     'image2', '-ss', '10', '-t', '0.001', '-s', '320*240', output_image_path])

    file.thumbnail = output_image_name
    file.save(update_fields=['thumbnail'])
