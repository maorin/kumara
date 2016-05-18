kill $(cat twistd.pid)
twistd --logfile=$PWD/start.log -epoll -y main.py
tail -f start.log
