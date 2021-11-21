const fs = require('fs')
const express = require('express')
const app = express()
const crypto = require('crypto');
global.code = undefined
function lovelove(target, source) {
    for (let key in source) {
        if (key in source && key in target) {
            lovelove(target[key], source[key])
        } else {
            target[key] = source[key]
        }
    }
}
function md5_encode(password) {
    var md5 = crypto.createHash('md5');
    return md5.update(password).digest('hex');
}
function makecode() {
    var num="";
    for(var i=0;i<4;i++){
	    num+=Math.floor(Math.random()*10)
    }
    global.code = num
}
app.all('/admin', (req, res) => {
    if (req.query.user == "admin" && req.query.passwd =="MDUwMg=="){
        if (req.query.a) {
            function Ctfer() {
                this.good_at    = undefined;
                this.team       = "X1cT34m"
                this.university = "NJUPT"
            }
            function Webdog() {
                this.status = "can not exit in the ctf world"
                this.character  = "scared"
            }
            Webdog.prototype = new Ctfer()
            let tyskill = new Webdog()
            let m1saka = new Webdog()
            let sxl = {}
            sxl = JSON.parse(req.query.a)
            lovelove(tyskill,sxl)
            if (m1saka.girlfriend == "fmyy"){
                res.send("0xGame{do_u_like_these_diao_pictures}")
            }else{

                res.send("qwq")
            }
        }else {
            res.send("欧拉欧拉欧拉欧拉！")
        }
    }else{
        res.send("呀卡马西！")
    }
})
app.post('/upload', function(req, res, next){
    res.send("此项服务已关闭")
});

app.get('/', function(req, res, next){
    var form = fs.readFileSync('./form.html', {encoding: 'utf8'});
    res.send(form);
});

app.get('/download', function(req, res){
    if (req.query.file && req.query.code) {
        if (req.query.code == global.code) {
            fs.readFile( "images/"+req.query.file,(err,data) =>{
                try{
                  if( err ){
                    throw err;
                  }else{
                    res.send( data.toString() );
                    makecode()
                  }
                }catch(e){
                  res.send( e );
                }
              } );
        }else {
            res.send("wrong verify code")
        }
    }
    else {
        res.send("just input something plz")
    }
});
app.get('/getcode', function(req, res){
    if (!global.code){
       makecode()
    }
    let x = md5_encode("X1cT34m_"+global.code)

    res.send('md5_encode("X1cT34m_"+xxxx).substring(4,10) == '+x.substring(4,10))
    //res.send(global.code)
})
app.listen(3000, () => console.log(`Example app listening on port 3000!`))
