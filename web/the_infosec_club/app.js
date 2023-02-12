const express = require("express");
const app = express();
var cookieParser = require('cookie-parser');
app.use(cookieParser());

const PORT = 8001 || process.env.PORT
app.get("/",(req,res)=>{
    const cookies = req.cookies;
    const user = cookies['user'];
    if(user==undefined || user==null){
        res.cookie("user","n00b")
    }
    else{
        if(user=="admin"){
            res.send("VULNTINE{c00k1e_m4n1pul4t10n_1s_th3_k3y}");
            return;
        }
    }
    res.sendFile(__dirname+"/index.html");
})


app.listen(PORT,()=>{
    console.log(`Started server at port ${PORT}`)
});