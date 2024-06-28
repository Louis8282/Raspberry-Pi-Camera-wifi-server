
import subprocess
import os
import time
import glob
import signal
import sys

# def capture_image(filename):
    # Use the mode that corresponds to the 640x480 resolution   1296   972
  #   proc = subprocess.Popen(['libcamera-still', '--nopreview', '-o', filename, '--width', '2592', '--height', '1944'])
    # return proc
# import subprocess

def capture_image(filename):
    # Use the mode that corresponds to the 2592x1944 resolution
    proc = subprocess.Popen(['raspistill', '-o', filename, '-w', '640', '-h', '480', '-n', '-t', '1'])
    return proc


def delete_old_files(directory, keep=4):
    files = sorted(glob.glob(os.path.join(directory, "*.jpg")), key=os.path.getmtime)
    files_to_delete = files[:-keep]
    for file in files_to_delete:
        os.remove(file)

def signal_handler(sig, frame):
    global running
    print("Terminating script...")
    running = False

def main():
    global running
    directory = "/home/louis/camera_script"
    toggle = False
    running = True
    signal.signal(signal.SIGINT, signal_handler)
    while running:
        timestamp = int(time.time())
        prefix = '1' if toggle else '2'
        filename = f"{directory}/{prefix}_{timestamp}.jpg"
        proc = capture_image(filename)
        # Wait for the image capture process to complete
        while proc.poll() is None and running:
            time.sleep(0.1)
        print("Captured image: " + filename)
        delete_old_files(directory)
        toggle = not toggle
        time.sleep(0.8)

if __name__ == "__main__":
    main()
