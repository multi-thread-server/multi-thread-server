import os, datetime
log_dir = os.getcwd() + '/log/log.txt'

def log(msg):
    now = datetime.datetime.now()
    msg = '{} - {}'.format(now, msg)
    print(msg)
    with open(log_dir, 'a') as log_file:
        log_file.write(msg)
