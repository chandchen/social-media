function encode(which_video){
  var source = which_video.getAttribute('href');
  var placeholder = document.getElementById('placeholder');
  placeholder.setAttribute('src', source);
  document.getElementById('placeholder').play();
}
