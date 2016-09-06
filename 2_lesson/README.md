### 2. Lesson: Use a Dockerfile 

1. Download the source code

~~~BASH
wget https://github.com/pbelmann/GCB-Docker/archive/master.zip
~~~

2. Unzip the files

~~~BASH
unzip master.zip
~~~

3. Change your current directory

~~~BASH
cd GCB-Docker-master/2_lesson
~~~

4. The directory contains this [Dockerfile](Dockerfile)

5. Build your image

~~~BASH
docker build -t webservice2 .
~~~

6. Start your service 

~~~BASH
docker run -p 5000:5000 -d webservice2
~~~

7. You can inspect logs with docker logs

~~~BASH
docker logs $(docker ps -lq)
~~~

8. Send a request to your webservice

~~~BASH
curl localhost:5000
~~~

9. Stop the service

~~~BASH
docker stop $(docker ps -lq)
~~~
