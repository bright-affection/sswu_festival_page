let slider = document.querySelector(".slider");
let innerSlider = document.querySelector(".slider-inner");
let pressed = false;
let startx;
let x;

slider.addEventListener("mousedown", e => {
  pressed = true;
  startx = e.clientX - innerSlider.offsetLeft; // 변경: offsetX 대신 clientX 사용
  slider.style.cursor = "grabbing";
});

slider.addEventListener("mouseenter", () => {
  slider.style.cursor = "grab";
});

slider.addEventListener("mouseup", () => {
  slider.style.cursor = "grab";
});

window.addEventListener("mouseup", () => {
  pressed = false;
});

slider.addEventListener("mousemove", e => {
  if (!pressed) return;
  e.preventDefault();
  x = e.clientX; // 변경: offsetX 대신 clientX 사용


  // 변경: 슬라이더의 크기에 맞게 이동 제한
  innerSlider.style.left = `${Math.min(0, Math.max(-(innerSlider.offsetWidth - slider.offsetWidth), x - startx))}px`;
});

function checkboundary() {
  // 변경: checkboundary 함수 제거
}
