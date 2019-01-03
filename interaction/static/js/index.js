// 畫面滑動會發生的事情
window.onscroll = function(){
  scrollNav();
  toTopShow();
}

// 畫面滑動後navbar固定
var prevScrollpos = window.pageYOffset;
function scrollNav() {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.querySelector(".navbar").style.top = "0";
  } else {
    document.querySelector(".navbar").style.top = "-50px";
  }
  prevScrollpos = currentScrollPos;
}

// 手機版點選漢堡後，menu出現
document.querySelector('#nav-toggle').addEventListener('click',function(){
  document.querySelector('.menu').classList.toggle('toggle_menu')
})

// navbar下拉選單出現，並且可點選
document.querySelector('#navbarDropdown').addEventListener('mouseover',function(){
  document.querySelector('.dropdown-menu').classList.toggle('show');
  var dropdownItem = document.querySelectorAll('.dropdown-item');
  for(i=0;i<dropdownItem.length;i++){
    dropdownItem[i].classList.toggle('click');
    // pointEvent = none/auto;
  }
})

var top_button = document.getElementById("top_button");
function toTopShow(){
  if (document.documentElement.scrollTop > 50){
    top_button.style.display = "block";
    } else{
    top_button.style.display = "none";
    }
}
function toTop(){
  document.documentElement.scrollTop = 0;
}

// gif
function gifFunc() {
  var gif = document.querySelector('.animation');
  setTimeout(function(){ gif.add('disappear');}, 1000);
}

// 遊戲互動區
$(document).ready(function() {
  $(".game-slide:first").fadeIn()
});

function changeFrame(item){
  var frame = item.closest( ".game-slide" );
  if ( frame.next().length != 0 ){
    frame.hide()
    frame.next().slideDown();
  } else{  
    $("html, body").scrollTop($("#sec_cooperation").offset().top);
  }
};

$( "#q1-1, #q1-2, #q2" ).click(function() {
  changeFrame($( this ));
});

// 選身高與每週杯數
$( "#q2-2" ).click(function() {
  var n_drinks = $( "#q2-drinks" ).val();
  var height = $( "#q2-height" ).val();
  $( ".a3-1" ).text((n_drinks*780/height).toPrecision(2));
  $( ".a3-2" ).text((n_drinks*39.9).toPrecision(2));
  $( ".a3-3" ).text((n_drinks*13.3).toPrecision(2));
  $( ".a3-4" ).text((n_drinks*1.82).toPrecision(2));
  $( ".a3-5" ).text((n_drinks*1.37).toPrecision(2));

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



