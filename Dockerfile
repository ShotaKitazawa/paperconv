FROM python:3
WORKDIR /usr/src/app
ADD requirements.txt .
ADD translate.py .
RUN pip install --no-cache-dir -r requirements.txt && wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 && tar xf phantomjs-2.1.1-linux-x86_64.tar.bz2 && rm -f phantomjs-2.1.1-linux-x86_64.tar.bz2 && mv phantomjs-2.1.1-linux-x86_64/bin/phantomjs . && rm -rf phantomjs-2.1.1-linux-x86_64
ENTRYPOINT [ "python", "translate.py", "input.txt" ]
