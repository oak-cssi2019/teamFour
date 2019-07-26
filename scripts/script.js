$( document ).ready(function() { //required for jQuery to work

//all javascript and jquery code here
$(document).ready(function(){
let leftPokemon;
//starter function to pull a random pokemon from the PokeAPI
  function getRandomPokemonLeft() {
    let randomNumber = Math.floor(Math.random() * 800) + 1;
    $.get(`https://pokeapi.co/api/v2/pokemon/${randomNumber}`).then(function(pokeData){
    console.log("Left Pokemon Data: ", pokeData);


function getRandoMove(){
  let maxMove = leftPokemon['moves'].length
  let randomMove = Math.floor(Math.random() * maxMove) + 1;
  return randomMove;
}
rightPokemon = JSON.stringify(pokeData)
leftPokemon = pokeData;
let pokeDataToPass = {"name": leftPokemon.name}

let leftPokemonDisplay =`
<h2 class="capitalize" >${leftPokemon['name']}</h2>
<img class="pokemon-img" src="${leftPokemon['sprites']['front_default']}">
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<h3>Type 1: ${leftPokemon['types'] [0] ['type'] ['name']}</h3>
${function(){
   if (leftPokemon['types'][1]){
     return `<h3>Type 2: ${leftPokemon['types'] [1] ['type'] ['name']}</h3>`
   } else{
     return ``
   }
}()}
<br>
<h3>Shiny form: </h3>
<img class="pokemon-img2" src="${leftPokemon['sprites']['front_shiny']}">
<br>
<h3>Speed: ${leftPokemon['stats'] [0] ['base_stat']} / Health: ${leftPokemon['stats'] [5] ['base_stat']}</h3>

<h3>Special Defense: ${leftPokemon['stats'] [1] ['base_stat']} / Defense: ${leftPokemon['stats'] [3] ['base_stat']}</h3>

<h3>Special Attack: ${leftPokemon['stats'] [2] ['base_stat']} / Attack: ${leftPokemon['stats'] [4] ['base_stat']}</h3></h3>

<br>
<h3>Move 1: ${leftPokemon['moves'] [getRandoMove()] ['move'] ['name']} / Move 2: ${leftPokemon['moves'] [getRandoMove()] ['move'] ['name']}</h3>

<h3>Move 3: ${leftPokemon['moves'] [getRandoMove()] ['move'] ['name']} / Move 4: ${leftPokemon['moves'] [getRandoMove()] ['move'] ['name']}</h3>
<button value="Refresh Page" onClick="window.location.reload();">Click me to get another pokemon</buttoN>

<form method="post">
  <input type="hidden" name="currentPokemonName" value=${leftPokemon['name']}>
  <input type="hidden" name="currentPokemonPic" value=${leftPokemon['sprites']['front_default']}>
  <input type="hidden" name="currentPokemonTY1" value=${leftPokemon['types'][0]['type']['name']}>
  <input type="hidden" name="currentPokemonTY2" value=${leftPokemon ['types'][1]['type']['name']}>
  <button type="submit">Save this Pokemon</button>
</form>
<h1 class="rainbow-text">Thx to Asrid, coach Bell, Dave Ung for making this possible</h1>
`
//console.log(leftPokemon)
$("#left").empty();
$("#left").append(leftPokemonDisplay);
    });
  }


$("#leftButton").click(getRandomPokemonLeft)

})

}); //required for jQuery to work
