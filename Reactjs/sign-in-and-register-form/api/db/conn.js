const mongoose=require('mongoose');
const connectDB = async()=>{
    try{
        const conn = await mongoose.connect(process.env.MONGO_URI,{
            useUnifiedTopology: true,
            useNewUrlParser: true,
            useCreateIndex: true,
            useFindAndModify:false,       
        })
        console.log(`mongo database is conn`);
    }catch(err){
        console.log(`Error:${err}`)
        process.exit(1);
    }
}

module.exports=connectDB;
