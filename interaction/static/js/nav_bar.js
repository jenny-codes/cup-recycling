// 畫面滑動會發生的事情
// window.onscroll = function(){
//   scrollNav();
// }

// 畫面滑動後navbar固定
// var prevScrollpos = window.pageYOffset;
// function scrollNav() {
//   var currentScrollPos = window.pageYOffset;
//   if (prevScrollpos > currentScrollPos) {
//     document.querySelector(".navbar").style.top = "0";
//   } else {
//     document.querySelector(".navbar").style.top = "-50px";
//   }
//   prevScrollpos = currentScrollPos;
// }

// 手機版點選漢堡後，menu出現
document.querySelector('#nav-toggle').addEventListener('click',function(){
  document.querySelector('.menu').classList.toggle('toggle_menu')
})

// navbar下拉選單出現，並且可點選
document.querySelector('#navbarDropdown').addEventListener('mouseover',function(){
  document.querySelector('.dropdown-menu').style.height='';
  var dropdownItem = document.querySelectorAll('.dropdown-item');
  for(i=0;i<dropdownItem.length;i++){
    dropdownItem[i].classList.toggle('click'); // pointEvent = none/auto;
  }
})