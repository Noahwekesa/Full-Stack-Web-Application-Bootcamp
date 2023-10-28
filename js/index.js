function showReview(){
    document.querySelector(".review-con").classList.toggle("hover-review");
    document.querySelector(".product-img").classList.toggle("hover-img");
}
function hideReview(){
    document.querySelector(".review-con").classList.toggle("hover-review");
    document.querySelector(".product-img").classList.toggle("hover-img");
}
var productImg = document.querySelector(".product-img")
productImg.addEventListener("mouseover", showReview)
productImg.addEventListener("mouseout", hideReview)


var video = document.querySelector("video")
video.addEventListener("ended", function(){ console.log("The video ended.")})

var sun = document.getElementById("sun-icon")
var moon = document.getElementById("moon-icon")
var body = document.getElementsByTagName("body")[0]
var introText = document.querySelector("#intro p")
function darkMode(){
    sun.style.display="none"
    moon.style.display="block"
    body.classList.toggle("body-dark")
    introText.style.color="#EEEFF1"
}
function lightMode(){
    sun.style.display="block"
    moon.style.display="none"
    body.classList.toggle("body-dark")
    introText.style.color="#3C404A"
}
