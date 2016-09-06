### 2. Lesson: Use a Dockerfile 

1.Change your current directory to your home directory with

~~~BASH
cd
~~~

2.Download the source code

~~~BASH
wget https://github.com/pbelmann/GCB-Docker/archive/master.zip
~~~

3.Unzip the files

~~~BASH
unzip master.zip
~~~

4.Change your current directory

~~~BASH
cd GCB-Docker-master/2_lesson
~~~

5.The directory contains this [Dockerfile](Dockerfile)

6.Build your image

~~~BASH
docker build -t webservice2 .
~~~

7.Start your service 

~~~BASH
docker run -p 5000:5000 -d webservice2
~~~

8.You can inspect logs with docker logs

~~~BASH
docker logs $(docker ps -lq)
~~~

9.Send a request to your webservice

~~~BASH
curl localhost:5000
~~~

10.Stop the service

~~~BASH
docker stop $(docker ps -lq)
~~~
