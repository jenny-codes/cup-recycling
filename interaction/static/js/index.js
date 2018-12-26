window.onscroll = function() {myFunction()};

var navbar = document.querySelector(".navbar");
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

document.querySelector('#navbarDropdown').addEventListener('click',function(){
  document.querySelector('.dropdown-menu').classList.toggle('show');
})
