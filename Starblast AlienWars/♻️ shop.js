// Ajouter sorts et pieges





this.options = {
    // see documentation for options reference
    root_mode: "survival",
    map_size: 30
  };
  
      var secondaries = ["Torpedo","Missile","Defense","Attack ","Trap   ","Spell  ","Defense 8","Defense 4"];
      var prices = ["550","270","130","130","50","100","25","50"];
      var setShop = function(ship) {
        for (let i = 0; i < 4;i++) {
          var component = {
            id: secondaries[i],
            position: [15 + i*15,40,14,8],
            shortcut: `${i + 4}`,
            visible: true,
            clickable:true,
            components: [
              { type: "box",position:[0,0,100,100],fill:"#9D9D9D",stroke:"#787878",width:15},
              { type: "text",position:[2,25,50,35],color:"#CDE",align:"center",value:`${secondaries[i]}`},
              { type: "box",position:[61,34,35.5,50],stroke:"#CDE",width:5},
              { type: "text",position:[54.5,45,50,35],color:"#CDE",align:"center",value:prices[i] + " 💎"},
              ]
          };
          ship.setUIComponent(component);
        }
        for (let i_ = 4; i_ < 8;i_++) {
          var component2 = {
            id: secondaries[i_],
            position: [15 + (i_ - 4)*15,50,14,8],
            shortcut: `${i_ + 4}`,
            visible: true,
            clickable:true,
            components: [
              { type: "box",position:[0,0,100,100],fill:"#9D9D9D",stroke:"#787878",width:15},
              { type: "text",position:[2,25,50,35],color:"#CDE",align:"center",value:`${secondaries[i_]}`},
              { type: "box",position:[61,34,35.5,50],stroke:"#CDE",width:5},
              { type: "text",position:[54.5,45,50,35],color:"#CDE",align:"center",value:prices[i_] + " 💎"},
              ]
          };
          ship.setUIComponent(component2);
        }
      };
        
      this.tick = function(game) {
        if (game.step % 15 === 0) {
          for (let ship of game.ships) {
              setShop(ship);
          }
        }
      }
      
      
      var IDS  = [12,11,42,41,null,null,20,21];
      this.event = function(event,game) {
        var ship = event.ship;
        var component = event.id;
        switch (event.name) {
          case "ui_component_clicked":
            for (let secondarie in secondaries) {
                if (component === secondaries[secondarie]) {
                    var gems = prices[secondarie];
                    if (ship.crystals >= gems) {
                    ship.set({
                        crystals:ship.crystals - parseInt(gems)
                    })
                    game.addCollectible({
                        code:IDS[secondarie],
                        x: ship.x,y:ship.y
                    })
                  } else {
                      console.error(`ERROR: ${ship.name} does not have enough gems (${ship.crystals}) to get a market element (costs ${gems}).`)
                  }
                }
            }
            break ;
        }
      };