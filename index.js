const express=require("express");
const upload=require("express-fileupload");
const bodyparser=require("body-parser");
const  ffmpeg = require('ffmpeg');
const app=express();
app.use(upload());

app.use(express.static("public"));



app.get("/",function(req,res){
  res.sendFile(__dirname+"/index.html");
})


app.post("/",function(req,res){
  const video=req.files.file;
  const filename=video.name;


video.mv("./"+filename,function(err){
  if(err){
    console.log(err);
  }
  else{
    const {spawn} = require("child_process");

     // Parameters passed in spawn -
     // 1. type_of_script
     // 2. list containing Path of the script
     //    and arguments for the script

     // E.g : http://localhost:3000/name?firstname=Mike&lastname=Will
     // so, first name = Mike and last name = Will
     const process = spawn('python',["convert.py",filename] );

     // Takes stdout data from script which executed
     // with arguments and send this data to res object
     process.stdout.on('data', function(data) {
         console.log(`stdout :${data}`);
     })

     process.stderr.on('data',(data)=>{
      console.log(`stderr : ${data}`);
  })
  
  process.on('close',(code)=>{
      console.log(`child process exited with code ${code}`)
  })
 }
})


setTimeout(function(){ res.sendFile(__dirname+"/down.html"); }, 50000);











});




app.listen(3000,function(){
  console.log("Successfully connected to server");
})
