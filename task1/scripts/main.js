var main = function(){
  var c = $('.colorMe');
  c[0].style.color = 'blue';

  $('.colorToggle').click(function(){

    if (c[0].style.color === 'yellow'){
      c[0].style.color = 'blue';
    }
    else{
      c[0].style.color = 'yellow';
    }
  });
};


$(document).ready(main);
