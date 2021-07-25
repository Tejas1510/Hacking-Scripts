const router = require("express").Router();
const User = require("../model/User");
const bcrypt = require("bcrypt");

//REGISTER NEW USER

router.post("/register",async(req,res)=>{
    try{
        const sall = await bcrypt.genSalt(10);
        const hashPass = await bcrypt.hash(req.body.password,sall);
        const newUser = new User({
            username:req.body.username,
            email:req.body.email,
            password:hashPass,
        });
        const user = await newUser.save();
        res.status(200).json(user);
    }catch(err){
        res.status(500).json(err);
    }
});
//SIGN IN NEW USER

router.post("/signin",async(req,res)=>{
    try {
        const user = await User.findOne({ username: req.body.username });
        !user && res.status(400).json("Wrong credentials!");
    
        const validated = await bcrypt.compare(req.body.password, user.password);
        !validated && res.status(400).json("Wrong credentials!");
    
        const { password, ...others } = user._doc;
        res.status(200).json(others);
      } catch (err) {
        res.status(500).json(err);
      }
});
router.get('/getdata',(req,res)=>{
  res.send(req.body.username);
})
module.exports = router;