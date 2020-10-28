from cgi_bin.cgi import method_get, method_post

class Calculator:

    def __init__(self, a="", b="", op="", result=""):
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

        第一个数字: <input type="text" name="num1" value="%s" />   <br/>

        第二个数字: <input type="text" name="num2" value="%s"/>  <br/><br/>

        请选择使用的算法:
            <input type="radio" name="symbol1" id="additon">加法
            <input type="radio" name="symbol2" id="subtaction">减法
            <input type="radio" name="symbol3" id="multiplication">乘法
            <input type="radio" name="symbol4" id="division">除法


        <input type="submit" value="计算" />

        最终的结果为：<input type="text" name="res" value="%s"/>
        </form>
        </body>
        </html>''' %(self.a,self.b,self.result)

@method_get('/cgi_bin/calculator.py')
def get(cgi_environ):
    return '200 OK', 'text/html', Calculator().build_html()

@method_post('/cgi_bin/calculator.py')
def post(cgi_environ):
    a, b, op, result = cgi_environ['CONTENT'].split('&')

    a, b = int(a.split('=')[1]), int(b.split('=')[1])
    op = op.split('=')[0]
    op_num=int(op[6])

    if op_num == 1:
        result = a + b
    elif op_num == 2:
        result = a - b
    elif op_num == 3:
        result = a * b
    elif op_num == 4:
        result = a / b
    
    print(result)

    #op_num = op[6];
    #print(op_num)

    #print('a={}, b={}, op={}'.format(a, b, op))
    return '200 OK', 'text/html', Calculator(a, b, op, result).build_html()
