function initialize() {
    const texts = document.getElementsByClassName("map_select_tx")
    const text1 = document.getElementById("booth");
    const text2 = document.getElementById("food");
    const text3 = document.getElementById("stage");

    text1.onclick = function() {
        text1.style.color = '#F06786';
    }
    text2.onclick = function() {
        text2.style.color = '#FAD07C';
    }
    text3.onclick = function() {
        texts.style.color = "#000"
        text3.style.color = '#6C5C9C';
    }
}

// DOMContentLoaded 이벤트가 발생할 때 initialize 함수를 호출합니다.
document.addEventListener("DOMContentLoaded", initialize);