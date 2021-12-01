this.tick = function(game) {
    if (game.step % 15 === 0) {
        for (let ship of game.ships) {
            if (ship.shield < 0) {
                ship.set({kill:true});
            }
        }
    }
}