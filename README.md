# d03
# D03 - Network Segmentation and Firewalling


# Steps

# Clone Code:
- git clone https://github.com/yuvaraju1/d03.git
- cd d03
# Build Docker images:
- docker build -t webapp ./webapp
- docker build -t backend ./backend
- docker build -t admin ./admin
# Tag docker images:
- docker tag webapp yuvaraju11/d03:webapp
- docker tag backend yuvaraju11/d03:backend
- docker tag admin yuvaraju11/d03:admin
# Push images to  registry:
- ocker login
- docker push yuvaraju11/d03:webapp
- docker push yuvaraju11/d03:backend
- docker push yuvaraju11/d03:admin
# Create a Docker network
- docker network create network1
# Run containers in same network:
- docker run -d --name container1 --network network1 -p 5000:5000 yuvaraju11/d03:webapp
- docker run -d --name container2 --network network1 -p 6000:6000 yuvaraju11/d03:backend
- docker run -d --name container3 --network network1 -p 7000:7000 yuvaraju11/d03:admin
# Exploit: (demonstrate lack of network segmentation)
- docker exec -it container1 sh
- apt update && apt install -y curl
- curl https://5000-port-3ncto2ucv3kgoe7j.labs.kodekloud.com/
* output: 
- Webapp says hello!
# How to fix it (basic network segmentation)
# Create networks
- docker network create webapp-net
- docker network create backend-net
- docker network create admin-net

# Attach new networks & remove old network

- docker network connect webapp-net container1
- docker network disconnect network1 container1

- docker network connect backend-net container2
- docker network disconnect network1 container2

- docker network connect admin-net container3
- docker network disconnect network1 container3
