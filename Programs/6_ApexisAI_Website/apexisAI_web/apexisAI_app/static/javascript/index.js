const mobileMenuBtn = document.getElementById('mobile-menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });

        
        // Hero Section Slider Functionality
        // Mobile menu toggle
        
        const bgSlider = document.getElementById('bg-slider');
        const bgImages = bgSlider.querySelectorAll('.slider-item');
        const prevBtn = document.getElementById('prev-btn');
        const nextBtn = document.getElementById('next-btn');
        let currentIndex = 0;
        let intervalId;

        function showSlide(index) {
            const slideWidth = window.innerWidth;
            const transformValue = -index * slideWidth;
            bgSlider.style.transform = `translateX(${transformValue}px)`;
        }
        function nextSlide() {
            currentIndex = (currentIndex + 1) % bgImages.length;
            showSlide(currentIndex);
        }
        function prevSlide() {
            currentIndex = (currentIndex - 1 + bgImages.length) % bgImages.length;
            showSlide(currentIndex);
        }
        function startAutoSlide() {
            clearInterval(intervalId);
            intervalId = setInterval(nextSlide, 5000);
        }
        prevBtn.addEventListener('click', () => {
            clearInterval(intervalId);
            prevSlide();
            startAutoSlide();
        });
        nextBtn.addEventListener('click', () => {
            clearInterval(intervalId);
            nextSlide();
            startAutoSlide();
        });
        window.addEventListener('resize', () => {
            showSlide(currentIndex);
        });

        // Dashboard Slider Functionality
        const dashboardSliderWrapper = document.getElementById('dashboard-slider-wrapper');
        const dashboardSlider = document.getElementById('dashboard-slider');
        const dashboardSlides = dashboardSlider.querySelectorAll('.dashboard-slide');
        const dashboardPrevBtn = document.getElementById('dashboard-prev-btn');
        const dashboardNextBtn = document.getElementById('dashboard-next-btn');
        let dashboardCurrentIndex = 0;

        function showDashboardSlide(index) {
            const slideWidth = dashboardSlides[0] ? dashboardSlides[0].offsetWidth : 0;
            const transformValue = -index * slideWidth;
            if (dashboardSlider) {
                dashboardSlider.style.transform = `translateX(${transformValue}px)`;
            }
        }
        function nextDashboardSlide() {
            if (dashboardSlides.length > 0) {
                dashboardCurrentIndex = (dashboardCurrentIndex + 1) % dashboardSlides.length;
                showDashboardSlide(dashboardCurrentIndex);
            }
        }
        function prevDashboardSlide() {
            if (dashboardSlides.length > 0) {
                dashboardCurrentIndex = (dashboardCurrentIndex - 1 + dashboardSlides.length) % dashboardSlides.length;
                showDashboardSlide(dashboardCurrentIndex);
            }
        }
        function updateDashboardSlideWidth() {
            if (dashboardSlides.length > 0) {
                showDashboardSlide(dashboardCurrentIndex);
            }
        }
        dashboardNextBtn.addEventListener('click', nextDashboardSlide);
        dashboardPrevBtn.addEventListener('click', prevDashboardSlide);
        window.addEventListener('resize', updateDashboardSlideWidth);

        // Testimonial Slider Functionality
        const testimonialSlider = document.getElementById('testimonial-slider');
        const testimonialSlides = testimonialSlider.querySelectorAll('.testimonial-slide');
        const testimonialPrevBtn = document.getElementById('testimonial-prev-btn');
        const testimonialNextBtn = document.getElementById('testimonial-next-btn');
        let testimonialCurrentIndex = 0;

        function showTestimonialSlide(index) {
            const slideWidth = testimonialSlides[0] ? testimonialSlides[0].offsetWidth : 0;
            const transformValue = -index * slideWidth;
            if (testimonialSlider) {
                testimonialSlider.style.transform = `translateX(${transformValue}px)`;
            }

            // Disable/Enable buttons based on the current index
            if (index === 0) {
                testimonialPrevBtn.disabled = true;
                testimonialPrevBtn.classList.add('opacity-50', 'cursor-not-allowed');
            } else {
                testimonialPrevBtn.disabled = false;
                testimonialPrevBtn.classList.remove('opacity-50', 'cursor-not-allowed');
            }

            if (index === testimonialSlides.length - 1) {
                testimonialNextBtn.disabled = true;
                testimonialNextBtn.classList.add('opacity-50', 'cursor-not-allowed');
            } else {
                testimonialNextBtn.disabled = false;
                testimonialNextBtn.classList.remove('opacity-50', 'cursor-not-allowed');
            }
        }
        function nextTestimonialSlide() {
            if (testimonialCurrentIndex < testimonialSlides.length - 1) {
                testimonialCurrentIndex++;
                showTestimonialSlide(testimonialCurrentIndex);
            }
        }
        function prevTestimonialSlide() {
            if (testimonialCurrentIndex > 0) {
                testimonialCurrentIndex--;
                showTestimonialSlide(testimonialCurrentIndex);
            }
        }
        function updateTestimonialSlideWidth() {
             if (testimonialSlides.length > 0) {
                showTestimonialSlide(testimonialCurrentIndex);
            }
        }
        testimonialNextBtn.addEventListener('click', nextTestimonialSlide);
        testimonialPrevBtn.addEventListener('click', prevTestimonialSlide);
        window.addEventListener('resize', updateTestimonialSlideWidth);


        // Run on page load
        document.addEventListener('DOMContentLoaded', () => {
            showSlide(0);
            startAutoSlide();
            updateDashboardSlideWidth();
            updateTestimonialSlideWidth(); // Initialize the testimonial slider
        });