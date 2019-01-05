function calculate(param){
  return Number.parseFloat(parseInt($( "#customer-cup-count" ).text())*param/52).toFixed(1);
}

$(document).ready(function() {
  $( ".a3-1" ).text((calculate(780/160)));
  $( ".a3-2" ).text(calculate(39.9));
  $( ".a3-3" ).text(calculate(13.3));
  $( ".a3-4" ).text(calculate(18.2));
  $( ".a3-5" ).text(calculate(1.37));
});
