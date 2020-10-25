from http import HttpRequest, HttpResponse

def http_request_test():
    chunks = [
        b'GET /index.html ',
        b'HTTP/1.1\r\nHost',
        b': localhost:5000',
        b'\r\nUser-Agent: ',
        b'curl/7.69.1\r\nA',
        b'ccept: */*\r\nco',
        b'ntent-length: 12',
        b'\r\n\r\nhello wo',
        b'rld!'
    ]
    http_request = HttpRequest()
    for data in chunks:
        assert not http_request.is_parse_completed
        http_request.feed_data(data)
    assert http_request.is_parse_completed
    assert http_request.get_method() == b'GET'
    assert http_request.get_url() == b'/index.html'
    assert http_request.get_version() == b'HTTP/1.1'
    assert http_request.get_headers() == {
        b'Host': b'localhost:5000',
        b'User-Agent': b'curl/7.69.1',
        b'Accept': b'*/*',
        b'content-length': b'12'
    }
    assert http_request.get_content_length() == 12
    assert http_request.get_content() == b'hello world!'

def http_response_test():
    pass

def test(test_unit):
    print('{}: [START]'.format(test_unit.__name__))
    test_unit()
    print('{}: [OK]'.format(test_unit.__name__))

def main():
    test(http_request_test)
    test(http_response_test)

if __name__ == '__main__':
    main()
