// 畫面滑動會發生的事情
window.onscroll = function(){
  toTopShow();
}

var top_button = document.getElementById("top_button");
function toTopShow(){
  if (document.documentElement.scrollTop > 50){
    top_button.style.bottom = "10px";
    } else{
    top_button.style.bottom = "-100px";
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
  $(".game-slide:first").fadeIn();
});

function changeFrame(item){
  var frame = item.closest( ".game-slide" );
  if ( frame.next().length != 0 ){
    frame.hide();
    frame.next().slideDown();
  } else{  
    $("html, body").scrollTop($("#sec_cooperation").offset().top);
  }
};

function calculate(param){
  var n_drinks = $( "#q2-drinks" ).val();
  return Number.parseFloat(n_drinks*param).toFixed(1);
}

$( "#q0-1, #q1-1, #q1-2, #q2" ).click(function() {
  changeFrame($( this ));
});

// 選身高與每週杯數
$( "#q2-2" ).click(function() {
  var height = $( "#q2-height" ).val();
  $( ".a3-1" ).text((calculate(780/height)));
  $( ".a3-2" ).text(calculate(39.9));
  $( ".a3-3" ).text(calculate(13.3));
  $( ".a3-4" ).text(calculate(18.2));
  $( ".a3-5" ).text(calculate(1.37));

  changeFrame($( this ));
});

$( "#q3" ).click(function() {
  var height = $( "#q2-height" ).val();
  $( ".a3-2" ).text(Number.parseFloat(calculate(39.9))+0.3);
  $( ".a3-3" ).text(Number.parseFloat(calculate(13.3))+1);
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
  scaler = this.value;
  if (slider_initialized == false) {
    set_original_vals();
    slider_initialized = true;
  }
  $( ".game-scalable" ).each(function(idx) {
    original = original_vals[idx];
    $( this ).text((original*scaler).toFixed(1));
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



