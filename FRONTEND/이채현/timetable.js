// https://liufeier.tistory.com/22
// https://velog.io/@real-bird/Javascript-클릭한-div만-색상-바꾸기

console.log("시작")
const allButtons = document.querySelectorAll(".date_btn");

function handleClick(event) {
    console.log("작동")
}

allButtons.forEach((e) => {
    e.addEventListener("click", handleClick);
});

// const allButtons = document.querySelectorAll(".date_btn");

// function handleClick(event) {
//     allButtons.forEach((btn) => {
//         btn.classList.remove("clicked");
//     });

//     event.target.classList.add("clicked");
// }

// allButtons.forEach((e) => {
//     e.addEventListener("click", handleClick);
// });
