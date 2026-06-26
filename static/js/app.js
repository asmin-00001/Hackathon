// =======================================
// TourGenie JavaScript
// =======================================

console.log("TourGenie Loaded Successfully!");

// Smooth scroll (for future use)
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function (e) {
        e.preventDefault();

        const target = document.querySelector(this.getAttribute("href"));

        if (target) {
            target.scrollIntoView({
                behavior: "smooth"
            });
        }
    });
});

// Navbar shadow on scroll
window.addEventListener("scroll", () => {

    const navbar = document.querySelector(".navbar");

    if (!navbar) return;

    if (window.scrollY > 50) {

        navbar.style.boxShadow = "0 5px 20px rgba(0,0,0,0.15)";

    } else {

        navbar.style.boxShadow = "0 3px 15px rgba(0,0,0,0.08)";

    }

});

// Button click animation
const buttons = document.querySelectorAll(".btn");

buttons.forEach(button => {

    button.addEventListener("mouseenter", () => {

        button.style.transform = "scale(1.05)";

    });

    button.addEventListener("mouseleave", () => {

        button.style.transform = "scale(1)";

    });

});