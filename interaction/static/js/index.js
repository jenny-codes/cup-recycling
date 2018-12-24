window.onscroll = function() {myFunction()};

var navbar = document.querySelector(".navbar");
console.log(navbar);
var navbar_height = navbar.offsetHeight;

function myFunction() {
  if (window.pageYOffset >= navbar_height) {
    navbar.classList.add("navbar_fixed")
  } else {
    navbar.classList.remove("navbar_fixed");
  }
}

document.querySelector('#nav-toggle').addEventListener('click',function(){
  document.querySelector('.menu').classList.toggle('toggle_menu')
})

// $(document).ready(function() {
//     $('dropdown-toggle').dropdown()
// });


$(document).ready(function() {
  $(".mySlides:first").fadeIn()
});

$( ".mySlides" ).click(function() {
  console.log($( this ))
  console.log($(this).next().length)
  if ( $( this ).next().length != 0 ){
    $( this ).slideUp();
    $( this ).next().slideDown();
  } else{  
    $("html, body").scrollTop($("#sec_cooperation").offset().top);
  }
});

// animate function: https://api.jquery.com/animate/
// traversing: https://www.w3schools.com/jquery/jquery_ref_traversing.asp


