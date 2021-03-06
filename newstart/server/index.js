const express = require('express');
const cors=require('cors');
const mysql=require('mysql');
const app=express();
const SELECT_ALL_QUERY='SELECT * FROM SAFEX_INFORMATION';
const connection=mysql.createConnection({
  host:'localhost',
  user:'abdo',
  password:'test123',
  database:'TESTDB'

});

connection.connect(err => {
  if(err){
    return err;
  }
});
console.log(connection);
app.use(cors());

app.get('/',(req,res)=>{
  res.send('go to other urls to see other stuff')
});

app.get('/select_all',(req,res)=>{
  connection.query(SELECT_ALL_QUERY,(err,results)=>{
    if(err){
      return res.send(err);
    }
    else{
      return res.json({
        data:results
      })
    }
  });

});


app.get('/select_range',(req,res)=>{
const{comm,date,date2}=req.query;
let selectQuery = 'SELECT * FROM ?? WHERE ?? = ? AND ?? BETWEEN ? AND ?';
let SELECT_CUSTOM_QUERY = mysql.format(selectQuery,["SAFEX_INFORMATION","COMMODITY",comm,"DATE",date,date2])
console.log(comm);
connection.query(SELECT_CUSTOM_QUERY,(err,results)=>{
  if(err){
    return res.send(err);
  }
  else{
    return res.json({
      data:results
    })
  }
});
});


app.get('/select_date',(req,res)=>{
const{comm,date}=req.query;
let selectQuery = 'SELECT * FROM ?? WHERE ?? = ? AND ?? = ?';
let SELECT_CUSTOM_QUERY = mysql.format(selectQuery,["SAFEX_INFORMATION","COMMODITY",comm,"DATE",date])
console.log(comm);
connection.query(SELECT_CUSTOM_QUERY,(err,results)=>{
  if(err){
    return res.send(err);
  }
  else{
    return res.json({
      data:results
    })
  }
});
});

app.listen(4000,()=>{
  console.log('Server listning on port 4000')
});
