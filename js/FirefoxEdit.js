// ==UserScript==
// @name         Firefox Edit
// @include      *://*
// ==/UserScript==

(function() {
    'use strict';
    document.getElementsByTagName("video").setAttribute("loop", "");
})();

document.onmouseup = function(){
    var temps = window.getSelection();
    if (temps == "" || temps == null) {
        document.activeElement.blur();
    }
};
