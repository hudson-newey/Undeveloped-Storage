// ==UserScript==
// @name         Firefox Edit
// @include      *://*
// ==/UserScript==
document.onmouseup=function(){
    var temps = window.getSelection();
    if(temps==""||temps==null){document.activeElement.blur();}
};
