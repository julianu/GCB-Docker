### 2. Lesson: Use Docker Compose to create a persistent todo service

1. Change your current directory to the third lesson

~~~BASH
cd GCB-Docker-master/3_lesson
~~~

2. The directory contains this [Dockerfile](Dockerfile)

3. Build your compose docker

~~~BASH
docker-compose build 
~~~

4. Start your docker containers in background

~~~BASH
docker-compose up -d
~~~

5. Check your running containers

~~~BASH
docker ps
~~~

6. Add a todo

~~~BASH
curl -X POST -d '{"description":"test_description", "name":"test_name"}' http://localhost:5000/new
~~~

7. List saved todos 

~~~BASH
curl http://localhost:5000
~~~

8. Stop the service

~~~BASH
docker stop $(docker ps -lq)
~~~
