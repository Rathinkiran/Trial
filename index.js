const express=require("express");
const bodyParser=require("body-parser");
const app = express();
const port = 3000
app.post('/conversations',function(req,res){
  console.log(req.headers["authorization"]);
  res.send({
    msg:"rathin"
  })
})
app.use(bodyParser.json());


app.get('/', function(req, res)  {
  res.send('Hello World!')
})

app.listen(port,function(req,res){

})