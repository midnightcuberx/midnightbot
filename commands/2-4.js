const scrambler = require('scrambler-util');
const scramble_444 =  require("./lib/scramble_444");
module.exports = {
	name: '2-4',
  aliases: ['234','234 relay'],
	execute(client,message, args) {
    let scrambles=[];
    let scramble2=scrambler("222",1);
    let scramble3=scrambler("333",1);
    let scramble4=scramble_444.getRandomScramble();
    let scramble22="2x2: "+scramble2[0];
    let scramble33="3x3: "+scramble3[0];
    let scramble44="4x4: "+scramble4;
    scrambles.push(scramble22,scramble33,scramble44);
    message.channel.send(scrambles.join("\n"));
	},
};
