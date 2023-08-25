import subprocess
import ffmpeg
import sys
import os

def convert_mp4_to_webp(mp4_path, output_path):
    try:
        subprocess.run(['./bin/ffmpeg.exe', '-i', mp4_path, '-c:v', 'libwebp', '-an', '-vsync', '0', '-loop', '0', '-f', 'webp', output_path])
        print("Conversion successful!")
    except Exception as e:
        print("Conversion failed:", e)

def is_mp4_file(file_path):
    return file_path.lower().endswith('.mp4')

if len(sys.argv) > 1:
    exe_path = os.path.abspath(sys.argv[0])
    script_directory = os.path.dirname(exe_path)
    for mp4_path in sys.argv[1:]:
        if os.path.isfile(mp4_path) and is_mp4_file(mp4_path):
            mp4_path = os.path.abspath(mp4_path)
            file_path = os.path.splitext(mp4_path)[0] + ".webp"
            file_path = os.path.basename(file_path)
            full_path = os.path.join(script_directory,file_path)
            print(mp4_path)
            convert_mp4_to_webp(mp4_path, full_path)
