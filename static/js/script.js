document.addEventListener("DOMContentLoaded", function() {
    var dropdownToggle = document.querySelector(".dropdown-toggle");
    var dropdownMenu = document.querySelector(".dropdown-menu");

    dropdownToggle.addEventListener("click", function() {
        if (dropdownMenu.style.display === "none") {
            dropdownMenu.style.display = "block";
        } else {
            dropdownMenu.style.display = "none";
        }
    });
});


/*slider*/
const sliderContainer = document.querySelector('.slider-container');
const imageFon = document.querySelector('.image_fon');
const leftArrow = document.querySelector('.left-arrow');
const rightArrow = document.querySelector('.right-arrow');
const images = document.querySelectorAll('.image_fon img');
const imageWidth = images[0].clientWidth;
let counter = 0;

function nextSlide() {
    counter++;
    if (counter >= images.length) {
        counter = 0;
    }
    imageFon.style.transform = `translateX(-${imageWidth * counter}px)`;
}

function prevSlide() {
    counter--;
    if (counter < 0) {
        counter = images.length - 1;
    }
    imageFon.style.transform = `translateX(-${imageWidth * counter}px)`;
}

leftArrow.addEventListener('click', prevSlide);
rightArrow.addEventListener('click', nextSlide);

// Автоматическое переключение слайдов каждые 3 секунды
setInterval(nextSlide, 3000);


/*новости переключение*/
document.getElementById("announcement-button").addEventListener("click", function() {
    var newsContent = document.querySelector(".news-content");
    var newsContent1 = document.querySelector(".news-content1");
    
    // Проверяем видимость первого блока, чтобы понять, какой блок показывать
    if (newsContent.style.display !== "none") {
        newsContent.style.display = "none";
        newsContent1.style.display = "block";
    } else {
        newsContent1.style.display = "none";
        newsContent.style.display = "block";
    }
});

/*видео*/

    


