    game.custom.players = {
      0:0,
      1:0,
      2:0,
      3:0
    };
    var numberPerTeams = 2;
    var preTeams = {
        colors: ["#DD23BB","#34E6DE","#45D11F","#E59529","#BED914","#EA3D13"],
        hues: [300,180,120,30,60,0],
        names: [" Pink "," Cyan ","Green ","Orange","Yellow"," Red "]
    };
    var afterTeams = {
        colors: {
            colors:[],
            full:[0,0,0,0]
        },
        hues: [],
        names: []
    };
    for (let i = 0; i<4;i++) {
        var color = preTeams.colors[~~(Math.random()*preTeams.colors.length)];
        var index = preTeams.colors.indexOf(color);
        var hue = preTeams.hues[index];
        var name_ = preTeams.names[index];
        afterTeams.colors.colors.push(color);
        afterTeams.hues.push(hue);
        afterTeams.names.push(name_);
        preTeams.colors.splice(index,1);
        preTeams.hues.splice(index,1);
        preTeams.names.splice(index,1);
    }
    //      color: afterTeams.colors[i]
    //      hue: afterTeams.hues[i]
    //      name: afterTeams.names[i]
var components = [];
var setColors = function(ship) {
    for (let i = 0;i<4;i++) {
      var component = {
        id: afterTeams.names[i],
        position: [30 + i*5 + i*4,75,8,14],
        visible: true,
        clickable:true,
        components: [
          { type: "box",position:[0,0,100,100],fill:afterTeams.colors.colors[i],stroke:"#6D6D6D",width:15},
          ]
      };
      if (components !== 4) {
        components.push(component.name)
      }
      ship.setUIComponent(component);
      for (let id in afterTeams.colors.full) {
        if (afterTeams.colors.full[id] >= 2) {
          
          component.components.push(
            { type: "text",position:[12.5,35,80,30],value:"FULL",color:"#CDE"}
          );
        } else if (afterTeams.colors.full[id] !== 2 && component.components[1] !== null) {
          component.components.splice(4 + id,1);
        }
      }
    }
  };
  var showText = function(ship,text,pos,pos1,color) {var myText = {id: "myText",position: pos,visible: true,components: [{ type: "text",value:text,position:pos1,color:color}]};ship.setUIComponent(myText);};
  

  this.tick = function(game) {
    if (game.step % 15 === 0) {
        for (let ship of game.ships) {
            // SHIP INIT:
            showText(ship,'Choose a color',[22.5,60,50,14],[15,50,70,40],"#CDE");
            if (ship.custom.init !== true) {
                setColors(ship);
                ship.set({
                  hue:preTeams.hues[0]
                })
                ship.custom.hue = preTeams.hues[0];
                ship.custom.init = true;
            }
        }
    }
  };

  var checkIfFull = function(id) {
    if (afterTeams.colors.full[id] !== numberPerTeams) {
      return true;
    } else {
      return false;
    }
  };
  this.event = function(event,game) {
    var ship = event.ship;
    var component = event.id;
    switch (event.name) {
      case "ui_component_clicked":
        for (let id in afterTeams.names) {
            if (component === afterTeams.names[id]) {
              var ifNotFull = checkIfFull(id);
              if (ifNotFull === true) {
                  game.custom.players[id]++;
                  afterTeams.colors.full[id]++;
                  if (ship.custom.hue !== preTeams.hues[0]) {
                    var a = afterTeams.hues.indexOf(ship.custom.hue)
                    afterTeams.colors.full[a]--;
                    game.custom.players[a]--;
                  }
                  for (let ship_ of game.ships) {
                    setColors(ship_)
                  }
                  ship.set({hue:afterTeams.hues[id],team:id});
                  ship.custom.hue = afterTeams.hues[id]
                  echo(afterTeams.colors.full)
              } else {
                console.error(`ERROR: ${ship.name} cannot be assignated to team ${id} " ${afterTeams.colors.names[id]} ".`);
              }
            }
        }
        break ;
    }
  };

