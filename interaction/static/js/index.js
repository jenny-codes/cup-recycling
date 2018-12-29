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
    // frame.slideUp();
    frame.hide()
    frame.next().slideDown();
  } else{  
    $("html, body").scrollTop($("#sec_cooperation").offset().top);
  }
};

// 遊戲互動區
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
var slider_initialized = false
function set_original_vals() {
  original_vals = $( ".game-scalable" ).map(function() {
    return $( this ).text();
  }).get()
}
slider.oninput = function() {
  scaler = this.value/50;
  if (slider_initialized == false) {
    set_original_vals();
    slider_initialized = true;
  }
  $( ".game-scalable" ).each(function(idx) {
    original = original_vals[idx];
    $( this ).text((original*scaler).toPrecision(2));
  });
}

// 換燈秀區
var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("plan_img");
  var dots = document.getElementsByClassName("link_dot");
  if (n > slides.length) {slideIndex = 1} 
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none"; 
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block"; 
  dots[slideIndex-1].className += " active";
}







