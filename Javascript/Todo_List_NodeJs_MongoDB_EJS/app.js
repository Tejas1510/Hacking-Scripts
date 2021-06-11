const express = require("express");
const bodyParser=require("body-parser");
const mongoose=require("mongoose");
const date=require(__dirname+"/date.js");
const _=require("lodash");

const app = express();

app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({extended:true}))
app.use(express.static("public"));

mongoose.connect("mongodb://localhost:27017/todolistDB",{useNewUrlParser:true,useUnifiedTopology: true});
const itemsSchema={
    name:String,
}
const Item=mongoose.model("Item",itemsSchema);

const item1 = new Item({
    name:"eat",
});
const item2 = new Item({
    name:"sleep",
});
const item3 = new Item({
    name:"repeat",
});
const defaultItems=[item1,item2,item3];

const listSchema={
    name:String,
    items:[itemsSchema]
};
const List = mongoose.model("list",listSchema);

app.get("/",function(req,res){

    //var day=date.getdate();
    Item.find({},function(err,results){
        if(results.length===0)
        {
            Item.insertMany(defaultItems,function(err){
                if(err){
                console.log(err);
                }
                else{
                    console.log("success");
                }
            });
        }
        res.render("list", {listtitle:"today",item:results});
       
    })
   
});
app.get("/:customname",function(req,res){
    const customlistname=_.capitalize(req.params.customname);
    List.findOne({name: customlistname},function(err,foundlist){
          if(!err)
          {
              if(!foundlist)
              {
                const list=new List({
                    name:customlistname,
                    items:defaultItems
                });
                list.save();
                res.redirect("/"+customlistname);
              }
              else
              {
                  res.render("list",{listtitle:foundlist.name,item:foundlist.items});
              }
              
          }
    });
   

});

app.post("/",function(req,res){
    var item= req.body.newitem;
    var listname=req.body.list;
   
        const item1=new Item ({
            name:item,
        });
        if(listname==="today")
        {
            item1.save();
            res.redirect("/");
        }
        else{
          List.findOne({name:listname},function(err,foundlist){
              if(err)
              {
               console.log(err);
              }
              else{
                  console.log(foundlist.items);
              foundlist.items.push(item1);
              foundlist.save();
              res.redirect("/"+listname);
              }
          })
        }
});
app.post("/delete",function(req,res){
    const listname=req.body.listname;
    const checkid=req.body.checkbox;
if(listname==="today")
{
    Item.findByIdAndRemove(req.body.checkbox,function(err){
        if(err)
        {
            console.log(err);
        }
        else{
            console.log("success");
            res.redirect("/");
        }
       });
}
else{
    List.findOneAndUpdate({name:listname},{$pull:{items:{_id:checkid}}},function(err,foundlist){
      if(!err)
      {
          res.redirect("/"+listname);
      }
    });
}

});

let port = process.env.PORT;
if (port == null || port == "") {
  port = 3000;
}

app.listen(port,function(){
console.log("started succesfully");
});