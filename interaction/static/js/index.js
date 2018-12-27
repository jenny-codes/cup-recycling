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