const scramble_444 =  require("./lib/scramble_444");
module.exports = {
	name: '4x4',
  aliases: ['4'],
	execute(client,message, args) {
    if(args[0]===undefined){
      args[0]=1
    }
    let scramlen=parseInt(args[0])
    let scrambleArr=[]
    let scramble=""
    for (i = 0; i < scramlen; i++){
      scramble=scramble_444.getRandomScramble()
      scrambleArr.push(scramble)
    }

    if(scramlen>5){
      scramlen=5 
      for (i = 0; i < scramlen; i++){
        scrambleArr[i]=(i+1)+") "+scrambleArr[i]
      }
      message.channel.send(scrambleArr.join("\n"));
      message.channel.send("5 scrambles is the maximum amount.")
    }
    else{
      for (i = 0; i < scramlen; i++){
        scrambleArr[i]=(i+1)+") "+scrambleArr[i]
      }
      message.channel.send(scrambleArr.join("\n"));
    }
	},
};
