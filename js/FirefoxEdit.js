// ==UserScript==
// @name         Firefox Edit
// @include      *://*
// ==/UserScript==
<<<<<<< HEAD

(function() {
    'use strict';
    document.getElementsByTagName("video").setAttribute("loop", "");
})();

document.onmouseup = function(){
    var temps = window.getSelection();
    if (temps == "" || temps == null) {
        document.activeElement.blur();
    }
=======
document.onmouseup=function(){
    var temps = window.getSelection();
    if(temps==""||temps==null){document.activeElement.blur();}
>>>>>>> fd8b9fa11b0db12721228c45a21ca1b8678e8c5f
};
