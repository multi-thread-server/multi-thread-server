from cgi_bin.cgi import method_get, method_post

class Calculator:

    def __init__(self, a=None, b=None, op=None, result=None):
        self.a, self.b, self.op, self.result = a, b, op, result

    def build_html(self):
        '''根据参数a、b、op、result生成网页'''
        return '''<!DOCTYPE html>
        <html>
        <head>
        <meta charset="utf-8">
        <title>calculator</title>
        </head>
        <body>
        <form action="/cgi_bin/calculator.py" method="post">

        第一个数字: <input type="text" name="num1" />  <br/>

        第二个数字: <input type="text" name="num2" />  <br/><br/>

        请选择使用的算法:
            <input type="radio" name="symbol" id="additon">加法
            <input type="radio" name="symbol" id="subtaction">减法
            <input type="radio" name="symbol" id="multiplication">乘法
            <input type="radio" name="symbol" id="division">除法

        <input type="submit" value="计算" />

        最终的结果为：<input type="text" name="result" />
        </form>
        </body>
        </html>'''

@method_get('/cgi_bin/calculator.py')
def get(cgi_environ):
    return '200 OK', 'text/html', Calculator().build_html()

@method_post('/cgi_bin/calculator.py')
def post(cgi_environ):
    print(cgi_environ)    # 输入参数信息
    # 根据post内容生成新的网页返回
    a, b, op, result = cgi_environ['CONTENT'].split('&')
    a, b = int(a.split('=')[1]), int(b.split('=')[1])
    op = op.split('=')[1]
    print('a={}, b={}, op=?'.format(a, b))
    return '200 OK', 'text/html', Calculator(a, b, op, result).build_html()
