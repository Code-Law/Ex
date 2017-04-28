#!/usr/bin/env python
import pickle, os, sys, logging
from httplib import HTTPConnection, socket
from smtplib import SMTP


def email_alert(message, status):
    fromaddr = 'abc@163.com'
    toaddrs = 'def@abc.com'

    server = SMTP('smtp.163.com:25')
    server.starttls()
    server.login('xxxxx', 'xxxx')
    server.sendmail(fromaddr, toaddrs, 'Subject: %s\r\n%s' % (status, message))
    server.quit()


def get_site_status(url):
    response = get_response(url)
    try:
        if getattr(response, 'status') == 200:
            return 'up'
    except AttributeError:
        pass
    return 'down'


def get_response(url):
    try:
        conn = HTTPConnection(url)
        conn.request('HEAD', '/')
        return conn.getresponse()
    except socket.error:
        return None
    except:
        logging.error('Bad URL:', url)
        exit(1)


def get_headers(url):
    response = get_response(url)
    try:
        return getattr(response, 'getheaders')()
    except AttributeError:
        return 'Headers unavailable'


def compare_site_status(prev_results):
    def is_status_changed(url):
        status = get_site_status(url)
        friendly_status = '%s is %s' % (url, status)
        print
        friendly_status
        if url in prev_results and prev_results[url] != status:
            logging.warning(status)
            email_alert(str(get_headers(url)), friendly_status)
        prev_results[url] = status

    return is_status_changed


def is_internet_reachable():
    if get_site_status('www.baidu.com') == 'down' and get_site_status('www.qq.com') == 'down':
        return False
    return True


def load_old_results(file_path):
    pickledata = {}
    if os.path.isfile(file_path):
        picklefile = open(file_path, 'rb')
        pickledata = pickle.load(picklefile)
        picklefile.close()
    return pickledata


def store_results(file_path, data):
    output = open(file_path, 'wb')
    pickle.dump(data, output)
    output.close()


def main(urls):
    logging.basicConfig(level=logging.WARNING, filename='checksites.log',
                        format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    pickle_file = 'data.pkl'
    pickledata = load_old_results(pickle_file)
    print
    pickledata

    if is_internet_reachable():
        status_checker = compare_site_status(pickledata)
        map(status_checker, urls)
    else:
        logging.error('Either the world ended or we are not connected to the net.')

    store_results(pickle_file, pickledata)


if __name__ == '__main__':
    main(sys.argv[1:])