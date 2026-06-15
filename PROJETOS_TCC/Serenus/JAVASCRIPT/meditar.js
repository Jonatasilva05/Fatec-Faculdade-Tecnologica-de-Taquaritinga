const cards = document.querySelectorAll(".card");

    cards.forEach((card, index) => {
        const video = card.querySelector(".video");
        const audio = card.querySelector("audio");

        card.addEventListener("mouseover", () => {
            video.play();
            audio.play();
        });

        card.addEventListener("mouseleave", () => {
            video.pause();
            audio.pause();
            audio.currentTime = 0; 
        });
    });