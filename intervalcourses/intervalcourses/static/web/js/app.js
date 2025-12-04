(function (window, document) {
    var $ = jQuery,
        htmlElement = $(window),
        documentElement = $(document),
        bodyElement = $('body'),
        htmlDocumentElement = $('html');

    var eduCore = {
        init: function () {
            eduCore.bindEvents();
            eduCore.initMethods();
        },

        bindEvents: function () {
            this.window = $(window);
            this.document = $(document);
            this.body = $('body');
            this.html = $('html');
        },

        initMethods: function () {
            eduCore.backgroundMarquee();
            eduCore.sitePreloader();
            eduCore.toolTip();
            eduCore.magnifyPopup();
            eduCore.widgetToggle();
            eduCore.counterUp();
            eduCore.masonryActivation();
            eduCore.lightboxActivation();
            eduCore.qtyButton();
            eduCore.mouseMoveAnimation();
            eduCore.popupMobileMenu();
            eduCore.searchPopup();
            eduCore.filterClickButton();
            eduCore.svgVivusAnimation();
            eduCore.radialProgress();
            eduCore.contactForm();
            eduCore.swiperSlider();
            eduCore.salActive();
            eduCore.countdownInit('.countdown', '2024/12/30');
            eduCore.countdownInit('.coming-countdown', '2024/12/30');
        },

        backgroundMarquee: function () {
            $('.background-marque').each(function () {
                var currentPosition = 0,
                    increment = 1,
                    element = $(this);

                setInterval(function () {
                    currentPosition += increment;
                    element.css('background-position-x', -currentPosition + 'px');
                }, 10);
            });
        },

        sitePreloader: function () {
            jQuery(window).load(function () {
                jQuery('#edublink-preloader').fadeOut();
            });

            $('.preloader-close-btn').on('click', function (event) {
                event.preventDefault();
                jQuery('#edublink-preloader').fadeOut();
            });
        },

        toolTip: function () {
            Tipped.create('.rn-btn', 'options!', {
                'skin': 'light',
                'position': 'right'
            });
        },

        stickyHeaderMenu: function () {
            $(window).on('scroll', function () {
                if ($('body').hasClass('sticky-header')) {
                    var placeholder = $('#edu-sticky-placeholder'),
                        mainMenu = $('.header-mainmenu'),
                        menuHeight = mainMenu.outerHeight(),
                        topBarHeight = $('.header-top-bar').outerHeight() || 0,
                        scrollThreshold = topBarHeight + 200;

                    if ($(window).scrollTop() > scrollThreshold) {
                        mainMenu.addClass('edu-sticky');
                        placeholder.height(menuHeight);
                    } else {
                        mainMenu.removeClass('edu-sticky');
                        placeholder.height(0);
                    }
                }
            });
        },

        salActive: function () {
            sal({
                'threshold': 0.01,
                'once': true
            });
        },

        magnifyPopup: function () {
            $(document).on('ready', function () {
                $('.video-popup-activation').magnificPopup({
                    'type': 'iframe'
                });
            });
        },

        widgetToggle: function () {
            $('.widget-toggle').on('click', function () {
                var toggleButton = $(this),
                    courseWidget = toggleButton.closest('.edu-course-widget');

                if (!courseWidget.hasClass('collapsed')) {
                    courseWidget.addClass('collapsed');
                    toggleButton.next('.content').slideUp(400);
                } else {
                    courseWidget.removeClass('collapsed');
                    toggleButton.next('.content').slideDown(400);
                }
            });

            $('.toggle-btn').on('click', function (event) {
                var targetId = $(this).parent().attr('data-filter'),
                    parentElement = $(this).parent();

                $(targetId).slideToggle();
                $(parentElement).toggleClass('active');
            });
        },

        swiperSlider: function () {
            // Hero Slider
            const heroSlider = new Swiper('.university-activator', {
                'slidesPerView': 1,
                'spaceBetween': 0,
                'loop': true,
                'pagination': false,
                'grabCursor': true,
                'draggable': true,
                'effect': 'fade',
                'speed': 1000,
                'autoplay': {
                    'delay': 5500
                },
                'navigation': {
                    'nextEl': '.slide-next',
                    'prevEl': '.slide-prev'
                },
                'lazy': {
                    'loadPrevNext': true,
                    'loadPrevNextAmount': 1
                }
            });

            // Transform origin for images
            $('.university-activator .swiper-slide img').each(function () {
                var transformOrigin = $(this).attr('transform-origin');
                if (transformOrigin != undefined) {
                    $(this).css({
                        'transform-origin': transformOrigin
                    });
                }
            });

            // Digital Marketing Slider
            var digitalMarketingMain = new Swiper('.digital-marketing-activator', {
                'spaceBetween': 0,
                'speed': 1000,
                'autoplay': {
                    'delay': 5000,
                    'disableOnInteraction': false
                },
                'loop': true,
                'loopedSlides': 1,
                'direction': 'vertical',
                'thumbs': {
                    'swiper': digitalMarketingThumbs
                },
                'navigation': {
                    'nextEl': '.slide-next',
                    'prevEl': '.slide-prev'
                }
            });

            var digitalMarketingThumbs = new Swiper('.digital-marketing-testimonial-thumbs', {
                'spaceBetween': 10,
                'centeredSlides': true,
                'slidesPerView': 1,
                'touchRatio': 0.2,
                'slideToClickedSlide': true,
                'loop': true
            });

            // Controller connection
            if ($('.digital-marketing-activator')[0]) {
                digitalMarketingMain.controller.control = digitalMarketingThumbs;
                digitalMarketingThumbs.controller.control = digitalMarketingMain;
            }

            // Background image handler
            var allElements = $('*');
            allElements.each(function (index) {
                if ($(this).attr('data-background')) {
                    $(this).css('background', 'url(' + $(this).attr('data-background') + ')');
                }
            });

            // Photography Slider
            const photographySlider = new Swiper('.photography-activator', {
                'slidesPerView': 1,
                'spaceBetween': 0,
                'loop': true,
                'pagination': false,
                'grabCursor': true,
                'draggable': true,
                'effect': 'fade',
                'speed': 1000,
                'autoplay': {
                    'delay': 8000
                },
                'navigation': {
                    'nextEl': '.slide-next',
                    'prevEl': '.slide-prev'
                },
                'lazy': {
                    'loadPrevNext': true,
                    'loadPrevNextAmount': 1
                },
                'pagination': {
                    'el': '.swiper-pagination',
                    'type': 'fraction'
                }
            });

            // Transform origin for photography images
            $('.photography-activator .swiper-slide img').each(function () {
                var transformOrigin = $(this).attr('transform-origin');
                if (transformOrigin != undefined) {
                    $(this).css({
                        'transform-origin': transformOrigin
                    });
                }
            });

            // Home Testimonial Slider
            const homeTestimonialSlider = new Swiper('.home-one-testimonial-activator', {
                'slidesPerView': 1,
                'spaceBetween': 0,
                'loop': true,
                'pagination': false,
                'grabCursor': true,
                'speed': 1500,
                'autoplay': {
                    'delay': 3500
                },
                'breakpoints': {
                    577: {
                        'slidesPerView': 2
                    }
                }
            });

            // Health Slider
            const healthSlider = new Swiper('.home-health-testimonial-activator', {
                'loop': true,
                'speed': 500,
                'slidesPerView': 1,
                'centeredSlides': true,
                'effect': 'coverflow',
                'grabCursor': true,
                'autoplay': false,
                'autoplay': {
                    'delay': 3500
                },
                'breakpoints': {
                    575: {
                        'slidesPerView': 2
                    }
                },
                'coverflowEffect': {
                    'rotate': 0,
                    'slideShadows': false,
                    'depth': 180,
                    'stretch': 80
                },
                'pagination': {
                    'el': '.swiper-pagination',
                    'type': 'bullets',
                    'clickable': true
                }
            });

            // Language Testimonial Slider
            const languageTestimonialSlider = new Swiper('.home-language-testimonial-activator', {
                'slidesPerView': 1,
                'spaceBetween': 0,
                'loop': true,
                'grabCursor': true,
                'speed': 1000,
                'autoplay': {
                    'delay': 3000
                },
                'breakpoints': {
                    768: {
                        'slidesPerView': 2
                    },
                    992: {
                        'slidesPerView': 3
                    }
                },
                'pagination': {
                    'el': '.swiper-pagination',
                    'type': 'bullets',
                    'clickable': true
                }
            });

            // Additional testimonial sliders with similar patterns...
            const testimonialSlider2 = new Swiper('.testimonial-activation-2', {
                'slidesPerView': 2,
                'spaceBetween': 0,
                'loop': true,
                'grabCursor': true,
                'speed': 1000,
                'autoplay': {
                    'delay': 3000
                },
                'breakpoints': {
                    768: {
                        'slidesPerView': 1
                    },
                    992: {
                        'slidesPerView': 2
                    }
                },
                'pagination': {
                    'el': '.swiper-pagination',
                    'type': 'bullets',
                    'clickable': true
                }
            });

            const testimonialSlider3 = new Swiper('.testimonial-activation-3', {
                'slidesPerView': 2,
                'spaceBetween': 0,
                'loop': true,
                'grabCursor': true,
                'speed': 2000,
                'autoplay': {
                    'delay': 3000
                },
                'breakpoints': {
                    1: {
                        'slidesPerView': 1
                    },
                    800: {
                        'slidesPerView': 2
                    }
                },
                'pagination': {
                    'el': '.swiper-pagination',
                    'type': 'bullets',
                    'clickable': true
                },
                'navigation': {
                    nextEl: '.swiper-button-prev',
                    prevEl: '.swiper-button-prv'
                }
            });

            // Continue with other slider configurations...
            // Business Course Slider
            const businessCourseSlider = new Swiper('.business-course-activation', {
                'slidesPerView': 1,
                'spaceBetween': 0,
                'loop': true,
                'grabCursor': true,
                'speed': 1000,
                'autoplay': {
                    'delay': 3000
                },
                'navigation': {
                    'nextEl': '.swiper-btn-nxt',
                    'prevEl': '.swiper-btn-prv'
                },
                'breakpoints': {
                    577: {
                        'slidesPerView': 2
                    }
                }
            });

            // More slider configurations would follow the same pattern...
        },

        counterUp: function () {
            $('.counter-item').each(function () {
                $(this).waypoint(function (direction) {
                    if (direction === 'entered') {
                        for (var i = 0; i < document.querySelectorAll('.odometer').length; i++) {
                            var odometerElement = document.querySelectorAll('.odometer')[i];
                            odometerElement.innerHTML = odometerElement.getAttribute('data-odometer-final');
                        }
                    }
                });
            });
        },

        masonryActivation: function () {
            $('.isotope-wrapper').imagesLoaded(function () {
                $('.isotop-filter').on('click', 'button', function () {
                    var filterValue = $(this).attr('data-filter');
                    masonryGrid.isotope({
                        'filter': filterValue
                    });
                });

                var masonryGrid = $('.isotope-list').isotope({
                    'itemSelector': '.isotope-item',
                    'percentPosition': true,
                    'transitionDuration': '0.7s',
                    'layoutMode': 'fitRows',
                    'masonry': {
                        'columnWidth': 1
                    }
                });
            });

            $('.isotop-filter').on('click', 'button', function (event) {
                $(this).siblings('.is-checked').removeClass('is-checked');
                $(this).addClass('is-checked');
                event.preventDefault();
            });

            var masonryGallery = $('#masonry-gallery');
            if (masonryGallery.length) {
                var galleryMasonry = masonryGallery.imagesLoaded(function () {
                    galleryMasonry.isotope({
                        'itemSelector': '.masonry-item',
                        'masonry': {
                            'columnWidth': '.masonry-item'
                        }
                    });
                });
            }
        },

        lightboxActivation: function () {
            lightGallery(document.getElementById('animated-thumbnials'), {
                'thumbnail': true,
                'animateThumb': false,
                'showThumbByDefault': false
            });
        },

        qtyButton: function () {
            $('.pro-qty').prepend('<span class="dec qtybtn">-</span>');
            $('.pro-qty').append('<span class="inc qtybtn">+</span>');

            $('.qtybtn').on('click', function () {
                var button = $(this),
                    currentInput = button.parent().find('input'),
                    currentValue = currentInput.val();

                if (button.hasClass('inc')) {
                    var newValue = parseFloat(currentValue) + 1;
                } else {
                    if (currentValue > 0) {
                        var newValue = parseFloat(currentValue) - 1;
                    } else {
                        newValue = 0;
                    }
                }
                button.parent().find('input').val(newValue);
            });
        },

        mouseMoveAnimation: function () {
            $('.scene').each(function () {
                new Parallax($(this)[0]);
            });
        },

        popupMobileMenu: function () {
            $('.hamberger-button').on('click', function (event) {
                $('.popup-mobile-menu').addClass('active');
            });

            $('.close-menu').on('click', function (event) {
                $('.popup-mobile-menu').removeClass('active');
                $('.popup-mobile-menu .mainmenu .has-droupdown > a').siblings('.submenu, .mega-menu').removeClass('active').slideToggle('400');
                $('.popup-mobile-menu .mainmenu .has-droupdown > a').removeClass('open');
            });

            $('.popup-mobile-menu .mainmenu .has-droupdown > a').on('click', function (event) {
                event.preventDefault();
                $(this).siblings('.submenu, .mega-menu').toggleClass('active').slideToggle('400');
                $(this).toggleClass('open');
            });

            $('.popup-mobile-menu, .splash-mobile-menu .mainmenu li a').on('click', function (event) {
                if (event.target === this && $('.popup-mobile-menu').hasClass('active') && $('.popup-mobile-menu .mainmenu .has-droupdown > a').siblings('.submenu, .mega-menu').removeClass('active').slideToggle('400') && $('.popup-mobile-menu .mainmenu .has-droupdown > a').removeClass('open'));
            });
        },

        searchPopup: function () {
            $('.search-trigger').on('click', function () {
                $('.edu-search-popup').addClass('open');
            });

            $('.close-trigger').on('click', function () {
                $('.edu-search-popup').removeClass('open');
            });

            $('.edu-search-popup').on('click', function () {
                $('.edu-search-popup').removeClass('open');
            });

            $('.edu-search-popup .edublink-search-popup-field').on('click', function (event) {
                event.stopPropagation();
            });
        },

        filterClickButton: function () {
            $('#slider-range').slider({
                'range': true,
                'min': 10,
                'max': 500,
                'values': [100, 300],
                'slide': function (event, ui) {
                    $('#amount').val('$' + ui.values[0] + ' - $' + ui.values[1]);
                }
            });
            $('#amount').val('$' + $('#slider-range').slider('values', 0) + ' - $' + $('#slider-range').slider('values', 1));
        },

        svgVivusAnimation: function () {
            SVGInject(document.querySelectorAll('img.svgInject'), {
                'makeIdsUnique': true,
                'afterInject': function (img, svg) {
                    new Vivus(svg, {
                        'duration': 80
                    });
                }
            });

            $('.edublink-svg-animate').hover(function () {
                var svgElement = $(this).find('svg')[0];
                new Vivus(svgElement, {
                    'duration': 50
                });
            });
        },

        countdownInit: function (selector, targetDate) {
            var countdownElement = $(selector);
            if (countdownElement.length) {
                countdownElement.countdown(targetDate, function (event) {
                    $(this).html(event.strftime('<div class=\'countdown-section\'><div><div class=\'countdown-number day\'>%D</div> <div class=\'countdown-unit\'>Day%!D</div> </div></div><div class=\'countdown-section\'><div><div class=\'countdown-number hour\'>%H</div> <div class=\'countdown-unit\'>Hrs%!H</div> </div></div><div class=\'countdown-section\'><div><div class=\'countdown-number minute\'>%M</div> <div class=\'countdown-unit\'>Mints</div> </div></div><div class=\'countdown-section\'><div><div class=\'countdown-number second\'>%S</div> <div class=\'countdown-unit\'>Sec</div> </div></div>'));
                });
            }
        },

        radialProgress: function () {
            $('.radial-progress').waypoint(function () {
                $('.radial-progress').easyPieChart({
                    'lineWidth': 10,
                    'scaleLength': 0,
                    'rotate': 0,
                    'trackColor': false,
                    'lineCap': 'round',
                    'size': 170
                });
            }, {
                'triggerOnce': true,
                'offset': 'bottom-in-view'
            });
        },

        contactForm: function () {
            $('.rwt-dynamic-form').on('submit', function (event) {
                event.preventDefault();

                var form = $(this),
                    formInputs = form.closest('.form-group').find('input,textarea');

                form.closest('.form-group').find('input,textarea').removeAttr('style');
                form.find('.error-msg').remove();
                form.closest('.form-group').find('button[type="submit"]').attr('disabled', 'disabled');

                var formData = $(this).serialize();

                $.ajax({
                    'url': 'mail.php',
                    'type': 'post',
                    'dataType': 'json',
                    'data': formData,
                    'success': function (response) {
                        form.closest('.form-group').find('button[type="submit"]').removeAttr('disabled');

                        if (response.code == false) {
                            form.closest('.form-group').find('[name="' + response.field + '"]');
                            form.find('.error-msg').html('<div class="error-msg"><p>*' + response.err + '</p></div>');
                        } else {
                            $('.success-msg').hide();
                            $('.form-group').removeClass('focused');
                            form.find('.error-msg').html('<div class="success-msg"><p>' + response.success + '</p></div>');
                            form.closest('.form-group').find('input,textarea').val('');

                            setTimeout(function () {
                                $('.success-msg').fadeOut('slow');
                            }, 5000);
                        }
                    }
                });
            });
        }
    };

    // Tab functionality
    const tabNavItems = document.querySelectorAll('.feature-card');
    tabNavItems.forEach(tabItem => {
        tabItem.addEventListener('mouseover', () => {
            tabNavItems.forEach(item => item.classList.remove('active'));
            tabItem.classList.add('active');
        });
    });

    // Gym tab functionality
    $('.gym-tab-nav li').click(function () {
        $('.tab-slider-body').hide();
        $('.tab-slider-body:first').show();
    });

    $('.gym-tab-nav li').click(function () {
        $('.tab-slider-body').hide();
        var targetTab = $(this).attr('rel');
        $('#' + targetTab).fadeIn();

        if ($(this).attr('rel') == 'tab2') {
            $('.gym-tab-slider-tabs').addClass('animated');
        } else {
            $('.gym-tab-slider-tabs').removeClass('animated');
        }

        $('.gym-tab-nav li').removeClass('active');
        $(this).addClass('active');
    });

    // Initialize the core functionality
    eduCore.init();

}(window, document, jQuery));