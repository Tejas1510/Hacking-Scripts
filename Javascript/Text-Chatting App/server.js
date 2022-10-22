const http = require('http')
const bodyParser = require('body-parser')
const path = require('path')
const session = require('express-session')
const express = require('express')
const WebSocket = require('ws')


// rooms
var rooms = {}

// sever
const app = express()
const server = http.createServer(app)

// body-parser middleware
app.use(bodyParser.urlencoded({extended: true}))
app.use(bodyParser.json())

// static files 
app.use(express.static(__dirname+'/public'))

app.get('/start',(req,res)=>{
    res.sendFile("start.html" ,  { root: path.join(__dirname, '/public') })
})

app.get("/create-room",(req,res)=>{
    console.log("created room")
    const {roomId , userId} = req.query
    var checkRoom = 0
    if(Object.keys(rooms).length!==0){
        checkRoom = Object.keys(rooms).filter(rid=>{
            return rid===roomId
        }).length
    }

    if(checkRoom==0){
        console.log("success")
        res.send({status: "success"})
    }
    else{
        res.send({status: "error"})
    }
})

app.get("/enter-room",(req,res)=>{
    const {roomId , userId} = req.query
    var checkRoom = 0
    console.log("entered room")
    if(Object.keys(rooms).length!==0){
        checkRoom = Object.keys(rooms).filter(rid=>{
            return rid===roomId
        }).length
    }

    if(checkRoom>0){
        console.log("entry success")
        res.send({status: "success"})
    }
    else{
        res.send({status: "error"})
    }
})

app.get('/room/:roodId/:userId',(req,res)=>{
    res.sendFile("room.html",{ root: path.join(__dirname, '/public') })
})


// websocket
const ws = new WebSocket.Server({ server });


ws.on('connection',(conn)=>{
    console.log("user connected")
    conn.on('message',(msg)=>{
        let data = JSON.parse(msg);

        if(data.type==="join-room"){
            

            if(rooms.hasOwnProperty(data.roomId)){
                rooms[data.roomId][data.userId]=conn
                var ack = {type:"entered-room" , roomId: data.roomId, allUsers: Object.keys(rooms[data.roomId])}
                broadcast(ack,"")
            }

            else if(data.roomId){
                rooms[data.roomId]={}
                rooms[data.roomId][data.userId]=conn
                var ack = {type:"created-room" , roomId: data.roomId , userId: data.userId}
                send(ack,conn)
            }

            else{
                var ack = {type: "error" , userId: data.userId }
                send(ack,conn)
            }
        }

        else if(data.type==="send-text"){
            if(rooms.hasOwnProperty(data.roomId) && rooms[data.roomId].hasOwnProperty(data.userId)){
                console.log("revieved")
                var text = {type:"recieved-text" , text: data.text , userId: data.userId , roomId: data.roomId}
                broadcast(text,data.userId)
            }
        }

        else if(data.type==="leave-room"){
            if(rooms.hasOwnProperty(data.roomId) && rooms[data.roomId].hasOwnProperty(data.userId)){
                var leave = {type:"user-left" , roomId:data.roomId, userId:data.userId}
                delete rooms[data.roomId][data.userId]  
                broadcast(leave,"")
            }
        }

    })
})

setInterval(()=>{
    var r = Object.keys(rooms)
    for(const room of r){
        var u = Object.keys(rooms[room])
        for(const uid of u){
          if(rooms[room][uid].readyState !== WebSocket.OPEN){
            delete rooms[room][uid]
            broadcast({type:'user-left',roomId:room,userId:uid},"")
          }
        }
    }
  },5000)

function broadcast(message,userId) {
    var {roomId,userId}=message
    Object.keys(rooms[roomId]).forEach((uid) => {
        if(userId=="" || userId!=uid) send(message,rooms[roomId][uid]);
        
      }
    );
}

function send(message,conn) { 
    conn.send(JSON.stringify(message)); 
};

server.listen(3000)