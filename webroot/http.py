class HttpRequest:

    def __init__(self):
        self.is_parse_completed = False
        self.data, self.headers = '', {}
        self.parse = self.parse_startline

    def feed_data(self, data):
        self.data += data.decode('utf-8')
        while self.parse(): pass

    def parse_startline(self):
        if len(split_result := self.data.split('\r\n', 1)) <= 1:
            return False
        startline, self.data = split_result
        method, url, version = startline.strip().split()
        self.set_method(method)
        self.set_url(url)
        self.set_version(version)
        self.parse = self.parse_headerline
        return True

    def parse_headerline(self):
        if len(split_result := self.data.split('\r\n', 1)) <= 1:
            return False
        headerline, self.data = split_result
        if headerline:
            key, value = headerline.strip().split(':', 1)
            self.add_header(key.strip(), value.strip())
            return True
        self.content_length, self.content_type = 0, ''
        if 'Content-Length' in self.headers:
            self.content_length = int(self.headers['Content-Length'])
        if 'Content-Type' in self.headers:
            self.content_type = self.headers['Content-Type']
        self.parse = self.parse_content
        return True

    def parse_content(self):
        if len(self.data) < self.content_length:
            return False
        self.content = self.data
        self.parse = lambda : False
        self.is_parse_completed = True
        return True

    def set_method(self, method):
        self.method = method

    def set_url(self, url):
        self.url = url

    def set_version(self, version):
        self.version = version

    def add_header(self, key, value):
        self.headers[key] = value

    def set_content(self, content):
        self.content = content

    def get_method(self):
        return self.method

    def get_url(self):
        return self.url

    def get_version(self):
        return self.version

    def get_headers(self):
        return self.headers

    def get_content_length(self):
        return self.content_length

    def get_content_type(self):
        return self.content_type

    def get_content(self):
        return self.content

class HttpResponse:

    def __init__(self, status, content_type, content):
        self.version, self.status = 'HTTP/1.1', status
        self.content_type = content_type
        self.content = content.encode('utf-8')
        self.content_length = len(self.content)
        self.headers = {}   # TODO: more information

    def set_status(self, status):
        self.status = status

    def add_head(self, key, value):
        self.headers[key] = value

    def set_content_type(self, content_type):
        self.content_type = content_type

    def set_content(self, content):
        self.content = content.encode('utf-8')
        self.content_length = len(self.content)

    def build_http(self):
        data = '{} {}\r\n'.format(self.version, self.status)
        data += 'Content-Length: {}\r\n'.format(self.content_length)
        data += 'Content-Type: {}\r\n'.format(self.content_type)
        for key in self.headers:
            data += '{}: {}\r\n'.format(key, self.headers[key])
        data = (data + '\r\n').encode('utf-8')
        return data + self.content
