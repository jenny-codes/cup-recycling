function calculate(param){
  return Number.parseFloat(parseInt($( "#customer-cup-count" ).text())*param).toFixed(1);
}

$(document).ready(function() {
  $( ".a3-1" ).text((calculate(780/160/52)));
  $( ".a3-2" ).text(calculate(39.9/52));
  $( ".a3-3" ).text(calculate(13.3/52));
  $( ".a3-4" ).text(calculate(1.82/52));
  $( ".a3-5" ).text(calculate(1.37/52));
});
