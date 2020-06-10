const scramble_333=require("./lib/scramble_333_edit");
module.exports = {
	name: 'zbll',
  aliases: [],
	execute(client,message, args) {
    if(args[0]===undefined){
      args[0]=1
    }
    let scrambleArr = [];
    let scramble="" 
    let scramlen=parseInt(args[0])
    if(scramlen>12){
      scramlen=12
      for (i = 0; i < scramlen; i++){
        scramble=scramble_333.getZBLLScramble()
        scrambleArr.push(scramble)
        scrambleArr[i]=(i+1)+") "+scrambleArr[i]
      }
      message.channel.send(scrambleArr.join("\n"));
      message.channel.send("12 scrambles is the maximum amount.")
    }
    else{
      for (i = 0; i < scramlen; i++){
        scramble=scramble_333.getZBLLScramble()
        scrambleArr.push(scramble)
        scrambleArr[i]=(i+1)+") "+scrambleArr[i]
      }
      message.channel.send(scrambleArr.join("\n"));
    }
	},
};
