class paddle{
    constructor(gamewidth,gameheight)
    {
        this.width=120;
        this.height=30;
        this.position={
            x:(gamewidth-this.width)/2,
            y:gameheight-this.height-10
        }
    }
    draw(ctx)
    {
        ctx.fillRect(this.position.x,this.position.y,this.width,this.height)
    }
}