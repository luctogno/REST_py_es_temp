# REST_py_es_temp
DOCKER COMMAND

docker run \
 -d \
 --name py_es_temp \
 -v /home/pi/docker/py_es_temp/app:/opt/app/ \
 --restart always \
 hypriot/rpi-python:latest \
 pip install elasticsearch>=2.0.0,<3.0.0 ; pip install interruptingcow ; python /opt/app/main.py