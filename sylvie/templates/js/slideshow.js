var slide_pos = 1;

function switch_slide() {
    slide_pos += 1;
    let slide = document.getElementById("slide")
    slide.classList.toggle("fade");
    slide.src = "/static/srcs/slides/slide" + String(slide_pos) + ".jpg";
    setTimeout(() => {slide.classList.toggle("fade");}, 4200);
    if (slide_pos == 5) {slide_pos = 0};
    setTimeout(switch_slide, 5000);
}
setTimeout(() => {slide.classList.toggle("fade");}, 4200);
setTimeout(switch_slide, 5000)

