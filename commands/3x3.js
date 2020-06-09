const scrambler = require('scrambler-util');
module.exports = {
	name: '3x3',
  aliases: ['3','oh'],
	execute(client,message, args) {
    if(args[0]===undefined){
      args[0]=1
    }
    let scramlen=parseInt(args[0])
    if(scramlen>12){
      scramlen=12
      let scrambleArr = scrambler("333",scramlen ); 
      for (i = 0; i < scramlen; i++){
        scrambleArr[i]=(i+1)+") "+scrambleArr[i]
      }
      message.channel.send(scrambleArr.join("\n"));
      message.channel.send("12 scrambles is the maximum amount.")
    }
    else{
      let scrambleArr = scrambler("333",scramlen ); 
      for (i = 0; i < scramlen; i++){
        scrambleArr[i]=(i+1)+") "+scrambleArr[i]
      }
      message.channel.send(scrambleArr.join("\n"));
    }
	},
};
