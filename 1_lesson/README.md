### 1. Lesson: Create a simple webservice

1. Start docker container

~~~BASH
docker run -i -t ubuntu:14.04 /bin/bash
~~~

2. Install libraries

~~~BASH
apt-get update -y && apt-get install -y python-pip python-dev build-essential wget unzip
~~~

3. Download files for the webservice

~~~BASH
wget https://github.com/pbelmann/GCB-Docker/archive/master.zip
~~~

4. Unzip source code

~~~BASH
unzip master.zip
~~~

5. Change directory

~~~BASH
cd GCB-Docker-master/2_lesson
~~~

6. Install all Python libraries

~~~BASH
pip install -r requirements.txt
~~~

7. Logout

~~~BASH
exit
~~~

8. Show the latest created container 

~~~BASH
docker ps -al
~~~

9. Use the container id showed in step 8 to create a new image

~~~BASH
docker commit <id> webservice
~~~

10. Start the webservice in background

~~~BASH
docker run -p 5000:5000 -d webservice python /GCB-Docker-master/2_lesson/app.py
~~~

11. You can inspect logs with docker logs

~~~BASH
docker logs $(docker ps -lq)
~~~

11. You can inspect logs with docker logs

~~~BASH
docker logs $(docker ps -lq)
~~~

12. Send a request to your webservice

~~~BASH
curl localhost:5000
~~~

13. Stop the service

~~~BASH
docker stop $(docker ps -lq)
~~~
