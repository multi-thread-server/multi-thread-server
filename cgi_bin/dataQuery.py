from cgi_bin.cgi import method_get, method_post
import PyMySQL

class StudentID:

    def __init__(self, id="", name="", banji=""):
        self.id, self.name, self.banji = id, name, banji

    def build_html(self):
        
        return '''

        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="utf-8">
        <title>infoQuery</title>
        </head>
        <body>
        <form action="/cgi_bin/dataQuery.py" method="post">

        请输入你想查询的学生ID: <input type="text" name="id" value="%s" />   <br/>

        <input type="submit" value="查询" /> <br/>

        你查询到的学生的姓名为  <input type="text" name="name" value="%s" /> 班级为 <input type="text" name="banji" value="%s" />
        </form>
        </body>
        </html>

        '''  % (self.id,self.name,self.banji)


@method_get('/cgi_bin/dataQuery.py')
def get(cgi_environ):
    return '200 OK', 'text/html', StudentID().build_html()

@method_post('/cgi_bin/dataQuery.py')
def post(cgi_environ):
    print(cgi_environ)    # 输入参数信息
    # 根据post内容生成新的网页返回
    id, name, banji = cgi_environ['CONTENT'].split('&')
    print(id+"&"+name+"&"+banji)


    return '200 OK', 'text/html', StudentID(id, name, banji).build_html()
