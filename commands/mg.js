const scrambler = require('scrambler-util');
const scramble_444 =  require("./lib/scramble_444");
module.exports = {
	name: 'mg',
  aliases: ['miniguildford'],
	execute(client,message, args) {
    let scrambles=[];
    let scramble2=scrambler("222",1);
    let scramble3=scrambler("333",1);
    let scramble4=scramble_444.getRandomScramble();
    let scramble5=scrambler("555",1);
    let scrambleoh=scrambler("333",1);
    let scramblesq1=scrambler('sq1',1);
    let scrambleskewb=scrambler('skewb',1);
    let scramblemega=scrambler('megaminx',1);
    let scrambleclock=scrambler('clock',1);
    let scramblepyra=scrambler('pyra',1);

    let scramble22="2x2: "+scramble2[0];
    let scramble33="3x3: "+scramble3[0];
    let scramble44="4x4: "+scramble4;
    let scramble55="5x5: "+scramble5[0];
    let scrambleoh1="OH: "+ scrambleoh[0];
    let scramblersq1="Sq-1: "+scramblesq1[0];
    let scramblerskewb="Skewb: "+scrambleskewb[0];
    let scramblermega="Megaminx: "+scramblemega[0];
    let scramblerclock="Clock: "+scrambleclock[0];
    let scramblerpyra="Pyraminx: "+scramblepyra[0];

    scrambles.push(scramble22,scramble33,scramble44,scramble55,scrambleoh1,scramblersq1,scramblerskewb,scramblermega,scramblerclock,scramblerpyra);
    message.channel.send(scrambles.join("\n"));
	},
};
