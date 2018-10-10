# About

text -> md for Paper

# Setup

## For Linux

```
pip install -r requirements.txt
wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
tar xf phantomjs-2.1.1-linux-x86_64.tar.bz2 && rm -f phantomjs-2.1.1-linux-x86_64.tar.bz2
mv phantomjs-2.1.1-linux-x86_64/bin/phantomjs . && rm -rf phantomjs-2.1.1-linux-x86_64
```

## For Mac

```
pip install -r requirements.txt
wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-macosx.zip
tar xf phantomjs-2.1.1-linux-x86_64.tar.bz2 && rm -f phantomjs-2.1.1-linux-x86_64.tar.bz2
mv phantomjs-2.1.1-linux-x86_64/bin/phantomjs . && rm -rf phantomjs-2.1.1-linux-x86_64
```

## For Docker

```
docker build -t local/paperconv .
docker run -itd -v output.md:output.md --name paperconv local/paperconv
```

# Execute

```
python3 translate.py hoge.txt | tee hoge.md
```

