var megaScrambler = require("./lib/megascramble");
module.exports = {
	name: '5x5',
  aliases: ['5'],
	execute(client,message, args) {
    if(args[0]===undefined){
      args[0]=1
    }
    let scrambleArr=[]
    let scramble=""
    let scramlen=parseInt(args[0])
    if(scramlen>5){
      scramlen=5 
      for (i = 0; i < scramlen; i++){
        scramble=megaScrambler.get555WCAScramble(60)
        scrambleArr.push(scramble)
        scrambleArr[i]=(i+1)+") "+scrambleArr[i]
      }
      message.channel.send(scrambleArr.join("\n"));
      message.channel.send("5 scrambles is the maximum amount.")
    }
    else{
      for (i = 0; i < scramlen; i++){
        scramble=megaScrambler.get555WCAScramble(60)
        scrambleArr.push(scramble)
        scrambleArr[i]=(i+1)+") "+scrambleArr[i]

      }
      message.channel.send(scrambleArr.join("\n"));
    }
	},
};
