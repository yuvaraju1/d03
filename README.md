# d03
D03 - Network Segmentation and Firewalling


Steps:
#Clone Code:
git clone https://github.com/yuvaraju1/d03.git
cd d03
#Build Docker images:
-docker build -t webapp ./webapp
-docker build -t backend ./backend
-docker build -t admin ./admin
#Tag docker images:
docker tag webapp yuvaraju11/d03:webapp
docker tag backend yuvaraju11/d03:backend
docker tag admin yuvaraju11/d03:admin
#Push images to  registry:
docker login
docker push yuvaraju11/d03:webapp
docker push yuvaraju11/d03:backend
docker push yuvaraju11/d03:admin
#Create a Docker network
docker network create network1
#Run containers in same network:
docker run -d --name container1 --network network1 -p 5000:5000 yuvaraju11/d03:webapp
docker run -d --name container2 --network network1 -p 6000:6000 yuvaraju11/d03:backend
docker run -d --name container3 --network network1 -p 7000:7000 yuvaraju11/d03:admin

