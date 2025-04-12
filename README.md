# my_first_docker_project

git clone https://github.com/chelbaev/my_first_docker_project.git

cd my_first_docker_project

в этой папке должен быть .env с такими данными:

SQLALCHEMY_DATABASE_URI=postgresql://postgres:password@mypostgres:5432/mydb

SQLALCHEMY_TRACK_MODIFICATIONS=False

docker network create your-network

docker run --name mypostgres --network=your-network -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=password -e POSTGRES_DB=mydb -p 5432:5432 -d postgres:13

docker run --name table --network=your-network -p 5000:4000 -e FLASK_ENV=development --add-host=db_host:172.17.0.2 --env-file .env -d chelbaev/table:1.0.0

docker ps 

смотрим запущенный контейнеры, берём CONTAINER ID для контейнера table. путь он будет xxx

docker logs xxx

там будут две строчки вида:

Running on http://172.18.0.3:4000

копируем http второй строчки и переходим в браузер

запушить url в бд: http://172.18.0.3:4000/push?url=your.url

посмотреть все url: http://172.18.0.3:4000/get
