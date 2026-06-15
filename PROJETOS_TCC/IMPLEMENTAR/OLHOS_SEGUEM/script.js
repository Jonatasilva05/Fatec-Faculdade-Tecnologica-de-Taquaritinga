const eyes = document.querySelectorAll('.eye');

document.addEventListener('mousemove', (event) => {
    eyes.forEach(eye => {
        const rect = eye.getBoundingClientRect();
        const eyeX = rect.left + rect.width / 2;
        const eyeY = rect.top + rect.height / 2;
        
        const deltaX = event.clientX - eyeX;
        const deltaY = event.clientY - eyeY;
        const angle = Math.atan2(deltaY, deltaX);
        
        const distance = Math.min(20, Math.sqrt(deltaX * deltaX + deltaY * deltaY));
        
        const pupil = eye.querySelector('.pupil');
        pupil.style.transform = `translate(${distance * Math.cos(angle)}px, ${distance * Math.sin(angle)}px)`;
    });
});
