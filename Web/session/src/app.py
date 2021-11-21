#coding=utf-8
from flask import Flask,render_template,url_for,render_template_string,redirect,request,current_app,session,abort,send_from_directory
import random
from urllib import parse
app=Flask(__name__)
app.secret_key="x1ct34myydsytstflglgjhdfhsh"

@app.route("/")
def index():
    "欢迎来到0xgame2021"
    return render_template("index.html")

@app.route("/login",methods=['GET'])
def log():
    return render_template("index.html")
@app.route("/login",methods=['POST'])
def login():
    if request.form['username']!='admin':
        username=request.form['username']
        session['name']=username
        session['uid']=str(random.randint(1,100))
        return render_template('login.html',username=username)
    print('no admin')
    return render_template("index.html")    
@app.route("/admin",methods=['GET'])
def admin():
    if 'name' not in session:
        return redirect('/')
    if 'uid' not in session:
        return "Hacker!!!!"
    if session['uid']=='1' and session['name']=='admin':
        flag = open('/flag','rb').read()
        return '''
                <h1>flag ls h3r3</h1>
                <h1>%s</h1>
                '''%(flag)
    return "你不是admin，只有admin可以看这个宝贝"

@app.errorhandler(404)
def page_not_found(e):
    def safe_jinja(s):
        blacklist = ['[',']','|','+','session','import','getattr','os','class','subclasses','mro','request','args','eval','if','for',' subprocess','file','open','popen','builtins','compile','execfile','from_pyfile','local','self','item','getitem','getattribute','func_globals']
        for no in blacklist:
            while True:
                if no in s:
                    s =s.replace(no,'')
                else:
                    break
        a =  ['enter', 'self']
        return ''.join(['{{% set {}=None%}}'.format(c) for c in a])+s
    template = '''
{%% block body %%}
    <div class="center-content error">
        <h1>Oops! That page doesn't exist.</h1>
        <h3>%s</h3>
    </div> 
{%% endblock %%}
''' % (parse.unquote(request.url))
    return render_template_string(safe_jinja(template)), 404
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)  
        
        
 
