import express from "express";
const app = express()
const port = 3000;




app.get("/",(req,res)=>{
    
const d = new Date();
const day = d.getDay();

    if(day == 6 || day==0){
        res.render("index.ejs",{
            daytime: " its Weekend!!!"
        })
       
    }else{
        res.render("index.ejs",{
            daytime: " its Weekday ;-;"
            
        })
       
    }

    
    
})


app.listen(port,()=>{
    console.log(`running on ${port}`)
})

