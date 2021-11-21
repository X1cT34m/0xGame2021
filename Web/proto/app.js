const fs = require('fs')
const express = require('express')
const app = express()
var crypto = require('crypto');
global.code = undefined
const delay = ms => new Promise(resolve => setTimeout(resolve, ms));
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
async function makecode() {
    var num="";
    for(var i=0;i<4;i++){
	    num+=Math.floor(Math.random()*10)
    }
    global.code = num
    await delay(200)
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
            let m1saka = new Webdog()
            Poria = JSON.parse(req.query.a)
            lovelove(m1saka,Poria)
            if (m1saka.girlfriend == "fmyy"){
                res.end("0xGame{do_u_like_these_diao_pictures}") //set flag
            }else{
                res.end("qwq")
            }
        }else {
            res.end("欧拉欧拉欧拉欧拉！")
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
            var file = "./images/"+req.query.file;
            res.download(file);
            makecode()
        }else {
            res.send("验证码错误")
        }
    }
    else {
        res.send("木大木大木大！")
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