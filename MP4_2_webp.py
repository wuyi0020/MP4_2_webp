import subprocess
import os
import sys

def convert_mp4_to_webp(mp4_path, output_path,ffmpeg_path):
    try:
        subprocess.run([ffmpeg_path, '-i', mp4_path, '-c:v', 'libwebp', '-lossless', '1', '-an', '-vsync', '0', '-loop', '0', '-f', 'webp', output_path])
        print("Conversion successful!")
    except Exception as e:
        print("Conversion failed:", e)

def is_mp4_file(file_path):
    return file_path.lower().endswith('.mp4')

if len(sys.argv) > 1:
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

    for mp4_path in sys.argv[1:]:
        if os.path.isfile(mp4_path) and is_mp4_file(mp4_path):
            mp4_path = os.path.abspath(mp4_path)
            mp4_filename = os.path.basename(mp4_path)
            webp_filename = os.path.splitext(mp4_filename)[0] + ".webp"
            full_webp_path = os.path.join(script_directory, webp_filename)
            ffmpeg_path = os.path.join(script_directory,'./bin/ffmpeg.exe')
            convert_mp4_to_webp(mp4_path, full_webp_path,ffmpeg_path)
