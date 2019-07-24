$( document ).ready(function() { //required for jQuery to work

//all javascript and jquery code here
$(document).ready(function(){
let leftPokemon;
//starter function to pull a random pokemon from the PokeAPI
  function getRandomPokemonLeft() {
    let randomNumber = Math.floor(Math.random() * 800) + 1;
    $.get(`https://pokeapi.co/api/v2/pokemon/${randomNumber}`).then(function(pokeData){
    console.log("Left Pokemon Data: ", pokeData);

leftPokemon = pokeData;

let leftPokemonDisplay =`
<h2  >${leftPokemon['name']}</h2>
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
     return `<h3>Types 2: ${leftPokemon['types'] [1] ['type'] ['name']}</h3>`
   } else{
     return ``
   }

}()}
<br>
<h3>Shiny form: </h3>
<img class="pokemon-img2" src="${leftPokemon['sprites']['front_shiny']}">
<br>
<h3></h3>
<br>
<button value="Refresh Page" onClick="window.location.reload();">Click me to get another pokemon</buttoN>
<h1 class="rainbow-text">Thx to David, Asrid, and coach Bella for making this possible</h1>
`
console.log(leftPokemon)
$("#left").empty();
$("#left").append(leftPokemonDisplay);
    });
  }


$("#leftButton").click(getRandomPokemonLeft)

})

}); //required for jQuery to work
