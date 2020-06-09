const scrambler = require('scrambler-util');
module.exports = {
	name: '4x4',
  aliases: ['4'],
	execute(client,message, args) {
    console.log(args)
    if(args[0]===undefined){
      args[0]=1
    }
    let scramlen=parseInt(args[0])
    if(scramlen>5){
      scramlen=5
      let scrambleArr = scrambler("444",scramlen ); 
      for (i = 0; i < scramlen; i++){
        scrambleArr[i]=(i+1)+") "+scrambleArr[i]
      }
      message.channel.send(scrambleArr.join("\n"));
      message.channel.send("5 scrambles is the maximum amount.")
    }
    else{
      let scrambleArr = scrambler("444",scramlen ); 
      for (i = 0; i < scramlen; i++){
        scrambleArr[i]=(i+1)+") "+scrambleArr[i]
      }
      message.channel.send(scrambleArr.join("\n"));
    }
  console.log(scrambleArr)
	},
};
