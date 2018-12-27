var navbar = document.querySelector(".navbar");
var navbar_height = navbar.offsetHeight;

function myFunction() {
  if (window.pageYOffset >= navbar_height) {
    navbar.classList.add("navbar_fixed");
  } else {
    navbar.classList.remove("navbar_fixed");
  }
}

document.querySelector('#nav-toggle').addEventListener('click',function(){
  document.querySelector('.menu').classList.toggle('toggle_menu')
})

document.querySelector('#navbarDropdown').addEventListener('click',function(){
  document.querySelector('.dropdown-menu').classList.toggle('show');
  var dropdownItem = document.querySelectorAll('.dropdown-item');
  console.log(dropdownItem);
  for(i=0;i<dropdownItem.length;i++){
    dropdownItem[i].classList.toggle('click');
  }
})


window.onscroll = function(){
  scrollDown();
  myFunction()};

var top_button = document.getElementById("top_button");

function scrollDown(){
  if (document.documentElement.scrollTop > 50){
    top_button.style.display = "block";
    } else{
    top_button.style.display = "none";
    }
}

function toTop(){
  document.documentElement.scrollTop = 0;
}

$(document).ready(function() {
  $(".game-slide:first").fadeIn()
});

function changeFrame(item){
  var frame = item.closest( ".game-slide" );
  if ( frame.next().length != 0 ){
    frame.slideUp();
    frame.next().slideDown();
  } else{  
    $("html, body").scrollTop($("#sec_cooperation").offset().top);
  }
};

$( "#q1-1, #q1-2" ).click(function() {
  changeFrame($( this ));
});

$( "#q2" ).click(function() {
  var n_drinks = $( "#q2-drinks" ).val();
  $( ".a3-1" ).text(n_drinks*3);
  $( ".a3-2" ).text(n_drinks*3);
  $( ".a3-3" ).text(n_drinks*3);
  $( ".a3-4" ).text(n_drinks*3);
  $( ".a3-5" ).text(n_drinks*3);

  changeFrame($( this ));
});

$( "#q3" ).click(function() {
  changeFrame($( this ));
});

// slider 功能
var slider = document.getElementById("slider");
slider.oninput = function() {
  scaler = this.value/50;
  $( ".game-scalable" ).each(function() {
    original = $( this ).text();
    $( this ).text(original*scaler);
  });
}

