import express from "express";
import bodyParser from "body-parser";
import { dirname } from "path";
import { fileURLToPath } from "url";
const __dirname = dirname(fileURLToPath(import.meta.url));

const app = express();
const port = 3000;


app.use(bodyParser.urlencoded({ extended: true }));
app.route("/")

.get((req,res)=>{
    res.sendFile(__dirname+"/public/index.html");
})

.post((req,res)=>{
const password = req.body.password;

if(password === "1234"){
     res.sendFile(__dirname+"/public/secret.html");
}else{
    res.redirect("/");
}
}
)

app.listen(port,()=>{
    console.log(`server on port ${port}`);
})
