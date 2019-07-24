$( document ).ready(function() { //required for jQuery to work

//all javascript and jquery code here
function getRandomPokemonLeft() {
  pokemons = $.get(`https://pokeapi.co/api/v2/pokemon/15`)
//   i = 0;
//     for (i = 0; i < pokemons.length; i++) {
//       pokemons[i] + "<br>";
// }
//     print(pokemons[i]);
  // console.log("hi")
  // console.log(pokemons.response)
  // };
//
// console.log("hello")
//
// function getRandomPokemonLeft() {
//   let randomNumber = Math.floor(Math.random() * 800) + 1;
//   $.get(`https://pokeapi.co/api/v2/pokemon/${randomNumber}`).then(function(pokeData){
//     console.log("Left Pokemon Data: ", pokeData);
//   });
// }

 getRandomPokemonLeft()



}); //required for jQuery to work
