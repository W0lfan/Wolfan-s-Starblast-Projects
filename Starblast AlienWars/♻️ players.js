this.options = {
    // see documentation for options reference
    root_mode: "survival",
    map_size: 30
  };
  game.custom.players = {
    0:0,
    1:0,
    2:0,
    3:0
  };
  var gamePhase = [
    0, // 
  ];
const sleep = (delay) => new Promise((resolve) => setTimeout(resolve,delay));

var count = function(minutes,seconds) {
  var p = minutes;
  var s = seconds;
  var p_ = "";
  var s_ = "";
   for (let i = s;i>=0;i--) {
    if (i <= 0 && p !== 0) {
      p--;
      s = 59;
    }
    if (i <= 0 && p === 0) {
      return true;
    }
    if (p < 10) {p_ = "0" + p;}else {p_ = p;}if (s < 10 ) {s_ = "0" + s;} else {s_ = s;}
    scoreboard.components[2].value = `${p_}:${s_}`;
    await sleep(1000);
   }
};

  var afterTeams = {
      colors: {
      colors:["#70ED7D","#E13131","#DCE131","#5EE131"],
    },
    hues: [120,0]
  };
  var scoreboard = {
    id: "scoreboard",
    components: [
      { type: "box",position:[10,10,80,25],stroke:"#CDE",width:10},
      { type: "text",position:[12,8,35,20],value: "",color:"#CDE",align:"right"},
      { type: "text",position:[65,18,20,20],value: "",color:"#CDE"},
      { type: "text",position:[37.5,62.5,30,20],value: "Players",color:"#CDE"},
    ]
  };
  
  var showBox = {
    id: "showBox",
    position: [70,0,15,10],
    visible: true,
    clickable:true,
    components: [
      { type: "box",position:[0,10,50,35],stroke:"#CDE",width:5},
      { type: "text",position:[5,18,40,20],value: "Players list",color:"#CDE"},
      ]
  };
  game.custom.arrayIDS = [];
  var setPlayerList = function(ship) {
    for (let i = 0; i < game.ships.length;i++) {
      var list = {
        id : game.ships[i].id,
        position : [69,5 + 5 * i,15,10],
        visible:true,
        components: [
          { type: "box",position:[0,10,60,35],stroke:afterTeams.colors.colors[afterTeams.hues.indexOf(game.ships[i].custom.hue)],width:5},
          { type: "player",position:[2,16,55,25],id:game.ships[i].id,color:"#CDE"},
        ]
      };
      ship.setUIComponent(list);
      game.custom.arrayIDS.push(list.id);
    }
  };
  
  
  
  
  var scoreboardBoxes = function(ship) {
    if (game.custom.boxed !== true) {
      game.custom.boxed = true;
      for (let i =0;i<4;i++) {
        scoreboard.components.push(
           { 
            type: "box",
            position:[25 + 15 * i,80,10,10],
            stroke:afterTeams.colors.colors[i],
            fill:afterTeams.colors.colors[i],
            width:15
           },
          { 
            type: "text",
            position:[25 + 15 * i,80,10,10],
            value: game.custom.players[i],
            color:"#6C6C6C"
          }
        );
      }
    }
  };
  var phase = "";
  var stade = 10;
  this.tick = function(game) {
    if (game.step % 15 === 0) {
      for (let ship of game.ships) {
        ship.setUIComponent(showBox);
        ship.setUIComponent(scoreboard);
        scoreboardBoxes(ship);
        if (ship.custom.hasNotSet !== true) {
          ship.set({team:1,hue:120});
          ship.custom.hue = 120;
          ship.custom.hasNotSet = true;
        }
        if (ship.custom.init !== true) {
          ship.custom.init = true;
          ship.custom.showList = false;
        } 
      }
    }
    if (game.step % 60 === 0) {
      game.addCrystal({x:0,y:0,value:stade});
    }
    if (game.step % 0) {
      count(5,0); // count * 2
      if (game.custom.crystal2 !== true) {
        game.custom.crystal2 = true;
        phase = "Crystals x2",
        stade = 20;
      }
    }
    if (game.step % 60 * 60 * 10 === 0) {
      count(5,0)
    }
    if (game.step % 60 * 60 * 15 === 0) {
      count(5,0)
    }
  };
  
    this.event = function(event,game) {
      var ship = event.ship;
      var component = event.id;
      switch (event.name) {
        case "ui_component_clicked":
          if (component === "showBox") {
            if (ship.custom.showList === false) {
              ship.custom.showList = true;
              setPlayerList(ship);
            } else {
              for (let i in game.custom.arrayIDS) {
                ship.setUIComponent({id:i,visible:false});
              }
              ship.custom.showList = false;
            }
          }
          break ;
      }
    };
  

    // Add crystals to the game, credits to BHPSNGUM
    ;(function() {
      var manageAliens = function (game) {
        try {
          if (game.custom.addCrystal_init) return;
          var modding = game.modding, internal_key = Object.keys(modding).find(key => {
            try {
              return typeof modding[key].alienCreated == "function" && key != "game";
            }
            catch(e) {
              return false;
            }
          }), internals = modding[internal_key];
          if (!internals.alienCreated.old) {
            let alienCreated =  function () {
              let args = arguments, tx = alienCreated.old.apply(this, args), t = args[0].request_id, alien = this.modding.game.findAlien(args[0].id);
              if (this.modding.game.aliens.find(alien => alien.request_id === t) && alien) {
                let tid = this.modding.game.custom.execAliens.indexOf(t);
                if (tid != -1) alien.set({kill: true});
              }
              return tx;
            };
            alienCreated.old = internals.alienCreated;
            internals.alienCreated = alienCreated;
          }
          if (!internals.eventReceived.old) {
            let eventReceived =  function () {
              let args = arguments, skipped;
              try {
                if (args[0].data.name == "alien_destroyed") skipped = this.modding.game.custom.execAliens.indexOf(this.modding.game.findAlien(args[0].data.alien).request_id) != -1;
              }
              catch (e) {
                skipped = false;
              }
              let context = this.modding.context, event = context.event;
              if (skipped) context.event = null;
              let x =  eventReceived.old.apply(this, args);
              context.event = event;
              return x;
            };
            eventReceived.old = internals.eventReceived;
            internals.eventReceived = eventReceived;
          }
          game.custom.execAliens = [];
          game.addCrystal = function(data)
          {
            data = data || {};
            let crystal = {x:data.x||0, y:data.y||0, value: data.value||0,
              toString: function(){return "Crystal:"+JSON.stringify(this)}
            };
            this.custom.execAliens.push(this.addAlien({code:13,x:crystal.x,y:crystal.y,crystal_drop:crystal.value}).request_id);
            return crystal;
          };
          game.custom.addCrystal_init = true;
        }
        catch (e) {
          console.error(e);
          game.modding.terminal.error(new Error("Failed to initialize 'game.addCrystal': Modding instances not found"));
        }
      }, tick = this.tick;
      this.tick = function () {
        this.tick = tick;
        try { manageAliens.apply(this, arguments) } catch (e) {}
        return typeof this.tick == "function" && this.tick.apply(this, arguments);
      };
    }).call(this);