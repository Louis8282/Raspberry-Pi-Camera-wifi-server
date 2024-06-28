# Raspberry-Pi-Camera-wifi-server

Instructions:

Connect a Raspbery Pi camera Rev. 1.3 to a Raspberry Pi running raspbian.
Setup the raspberry pi to create a hotspot (I do this via an external wifi antenna for extra range).

Place the files camera_capture.py and server_for_images.py in a folder called home/your_username/camera_script.
In server.py you will need to change     
os.chdir('/home/louis/camera_script')  # Change to your images directory
In camera_capture.py you will need to change:
 directory = "/home/louis/camera_script" # change to your directory

If you want these scripts to run automatically on startup you can place camera_capture.service and http_server.service in etc/systemd/system and enable the services using sudo systemctl enable camera_capture and enable http_server.

Then, connect your laptop to the hotspot and click on Boat_camera.html that you can place on your desktop. Images from the camera should be displayed in your browser. It works on chrome in windows. Other browsers might have issues with cors.

The images should switch instantaneously in the browser that's why there are always several images present on the raspberry pi.
