const scrambler = require('scrambler-util');
const scramble_444 =  require("./lib/scramble_444");
module.exports = {
	name: '2-5',
  aliases: ['235 relay'],
	execute(client,message, args) {
    let scrambles=[];
    let scramble2=scrambler("222",1);
    let scramble3=scrambler("333",1);
    let scramble4=scramble_444.getRandomScramble();
    let scramble5=scrambler("555",1);
    let scramble22="2x2: "+scramble2[0];
    let scramble33="3x3: "+scramble3[0];
    let scramble44="4x4: "+scramble4;
    let scramble55="5x5: "+scramble5[0];
    scrambles.push(scramble22,scramble33,scramble44,scramble55);
    message.channel.send(scrambles.join("\n"));
	},
};
