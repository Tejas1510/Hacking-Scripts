// gamestates
const gameStates={
    paused:0,
    running:1,
    menu:2,
    gameover:3,
    newlevel:4
}
// handles all the input from the user
class inputHandler{
    constructor(paddle,game)
    {
        document.addEventListener('keydown',(e)=>{
            // alert(e.keyCode)
            switch(e.keyCode)
            {
                case 37:
                    paddle.moveLeft()
                    break
                case 39:
                    paddle.moveRight()
                    break
                case 27:
                    game.tooglepause()
                    break
                case 13:
                    game.start()
                    break
            }
        })
        document.addEventListener('keyup',(e)=>{
            switch(e.keyCode)
            {
                case 37:
                    if(paddle.speed<0)
                        paddle.stop()
                    break
                case 39:
                    if(paddle.speed>0)
                        paddle.stop()
            }
        })
    }
}
class paddle{
    constructor(game)
    {
        this.gamewidth=game.gamewidth
        this.width=150;
        this.height=30;
        this.speed=0
        this.game=game
        this.maxspeed=7
        this.position={
            x:game.gamewidth/2-this.width/2,
            y:game.gameheight-this.height-10
        };
    }
    draw(ctx)
    {
        // console.log("called")
        cxt.fillStyle="#F00"
        ctx.fillRect(this.position.x,this.position.y,this.width,this.height)
    }
    update(deltatime)
    {
        // #so its gonna go 5time show much the time has passed
        this.position.x+=this.speed
        if(this.position.x<0)
        this.position.x=0
        if(this.position.x+this.width>this.gamewidth)
        this.position.x=this.gamewidth-this.width
        // console.log(this.position.x)
    }
    moveLeft()
    {
        this.speed=-this.maxspeed;
    }
    moveRight()
    {
        this.speed=this.maxspeed
    }
    stop()
    {
        this.speed=0
    }
}
class ball{
    constructor(game)
    {
        this.image=document.getElementById("ballimage")
        this.game=game
        this.gamewidth=game.gamewidth
        this.gameheight=game.gameheight
        this.size=30
        this.reset()
    }
    reset()
    {
        this.speed={
            x:10,
            y:-4
        }
        this.position={
            x:10,
            y:400
        }
    }
    update(deltatime){
        this.position.x+=this.speed.x
        this.position.y+=this.speed.y
        //gameover
        if(this.position.y>this.gameheight-this.size){
            this.game.lives--
            this.reset()}
        //checks if it hits the wall
        if(this.position.x>this.gamewidth-this.size||this.position.x<0)
            this.speed.x=-this.speed.x
        //checks if the hits the ends
        if(this.position.y<0)
            this.speed.y=-this.speed.y
        //to check if it hits the paddle
        if(collisionDetection(this,this.game.p))
        {
            this.speed.y=-this.speed.y
            this.position.y=this.game.p.position.y-this.size
        }
    }
    draw(ctx)
    {
        ctx.drawImage(this.image,this.position.x,this.position.y,this.size,this.size)
    }
}
class Game{
    constructor(gamewidth,gameheight){
        this.gamewidth=gamewidth;
        this.gameheight=gameheight
        this.gamestate=gameStates.menu
        this.p=new paddle(this)
        this.b=new ball(this)
        new inputHandler(this.p,this)
        this.gameObjects=[]
        this.lives=3
        this.bricks=[]
        this.level=[level1,level2]
        this.currentlevel=0
    }
    // when the game starts we instantiate the paddle and the ball
    start()
    {
        // let bricks=brickLevel(this,level1)
        // let brick=new Brick(this,{x:10,y:20})
        //bug fix
        if(this.gamestate!=gameStates.menu||this.gamestate==gameStates.newlevel) return
        this.b.reset()
        this.bricks=brickLevel(this,this.level[this.currentlevel])
        this.gameObjects=[
            this.b,this.p
        ]
        this.gamestate=gameStates.running
    }
    update(deltatime)
    {
        if(this.lives==0)
            this.gamestate=gameStates.gameover
        if(this.gamestate==gameStates.paused||this.gamestate==gameStates.menu||this.gamestate==gameStates.gameover)
            return
        if(this.bricks.length===0){
            this.currentlevel++
            this.gamestate=gameStates.newlevel
            this.start()
        }
        [...this.gameObjects,...this.bricks].forEach(obj=>obj.update(deltatime))
        this.bricks=this.bricks.filter(gameObj=>!gameObj.markedfordeletion)
    }
    draw(ctx)
    {
        [...this.gameObjects,...this.bricks].forEach(onj=>{
            onj.draw(ctx)
        })
        if(this.gamestate==gameStates.paused){
            ctx.rect(0,0,this.gamewidth,this.gameheight)
            ctx.fillStyle="rgba(0,0,0,.5)"
            ctx.fill()
            ctx.font="30px Arial"
            ctx.fillStyle="white"
            ctx.textAlign="center"
            ctx.fillText("Paused",gamewidth/2,gameheight/2)
        }
        if(this.gamestate==gameStates.menu)
        {
            ctx.rect(0,0,this.gamewidth,this.gameheight)
            ctx.fillStyle="rgba(0,0,0,1)"
            ctx.fill()
            ctx.font="30px Arial"
            ctx.fillStyle="white"
            ctx.textAlign="center"
            ctx.fillText("Press enter to start",gamewidth/2,gameheight/2)
        }
        if(this.gamestate==gameStates.gameover)
        {
            ctx.rect(0,0,this.gamewidth,this.gameheight)
            ctx.fillStyle="rgba(0,0,0,1)"
            ctx.fill()
            ctx.font="30px Arial"
            ctx.fillStyle="white"
            ctx.textAlign="center"
            ctx.fillText("Game Over!\n Refresh to restart.",gamewidth/2,gameheight/2)
        }
    }
    tooglepause()
    {
        //tells the game the situation of the game
        // whether it is paused or not
        if(this.gamestate==gameStates.paused)
            this.gamestate=gameStates.running
        else
            this.gamestate=gameStates.paused

    }
}
// to make the bricks
class Brick{
    constructor(game,position) {
        this.image=document.getElementById("brick")
        this.game=game
        this.position=position
        this.size=20
        this.width=80
        this.height=24
        this.markedfordeletion=false
    }
    update()
    {
        if(collisionDetection(this.game.b,this)){
            this.game.b.speed.y=-this.game.b.speed.y
            this.markedfordeletion=true}
    }
    draw(ctx)
    {
        ctx.drawImage(this.image,this.position.x,this.position.y,this.width,this.height) 
    }
}
//for levels in the game
const level1=[
    [0,1,0,1,0,1,0,1,0,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1]
]
const level2=[
    [0,1,1,0,0,0,0,1,1,0],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1]
]
function brickLevel(game,level)
{
    let bricks=[]
    level.forEach((row,rowIndex)=>{
        row.forEach((brick,brickindex)=>{
            if(brick==1){
                let position={
                    x:80*brickindex,
                    y:100+24*rowIndex
                }
                bricks.push(new Brick(game,position))}
        })
    })
    return bricks
}
function collisionDetection(ball,gameobject)
{
    let ballbottom=ball.position.y+ball.size
    let balltop=ball.position.y
    let topOfobject=gameobject.position.y
    let leftsideobject=gameobject.position.x
    let rightsideobject=gameobject.position.x+gameobject.width
    let bottomsideobject=gameobject.position.y+gameobject.height
    if(ballbottom>=topOfobject&&balltop<=bottomsideobject&&ball.position.x>=leftsideobject&&ball.position.x+ball.size<rightsideobject)
    {
        return true
    }
    else
        false
}
let canvas=document.getElementById("gamescreen")
let cxt=canvas.getContext("2d")
const gameheight=600
const gamewidth=800

let lastTime=0
// let imageball=document.getElementById('ballimage')
let game=new Game(gamewidth,gameheight)
// game.start()
function gameloop(timestamp){
    let deltatime=timestamp-lastTime
    lastTime=timestamp
    cxt.clearRect(0,0,gamewidth,gameheight)
    game.update(deltatime)
    game.draw(cxt)
    //first 2 are position co-ordinates
    // the remaining two are the size of the coordinates
    requestAnimationFrame(gameloop)
}
requestAnimationFrame(gameloop)
// const input=new inputHandler(p)