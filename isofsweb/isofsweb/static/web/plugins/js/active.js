// =========================================================================================
// * Project Name :  Eduna - Online Education Courses HTML5 Template.
// * File         :  JS Base
// * Version      :  1.0.0
// * Author       :  BizanTheme (https://themeforest.net/user/bizantheme)
// * Developer    :  Meheraj Hossain Sagar
// =========================================================================================

(function ($) {
  "use strict";
  $(document).on("ready", function () {
    /*======================================================================================
		  Header Sticky JS
	  =======================================================================================*/
    $(window).on("scroll", function (event) {
      var scroll = $(window).scrollTop();
      if (scroll < 100) {
        $(".ed-header").removeClass("sticky");
      } else {
        $(".ed-header").addClass("sticky");
      }
    });

    /*======================================================================================
      Wow JS
    =======================================================================================*/
    var window_width = $(window).width();
    if (window_width > 767) {
      new WOW().init();
    }

    /*======================================================================================
      CounterUp JS
   =======================================================================================*/
    $(".counter").counterUp({
      time: 1500,
    });

    /*======================================================================================
      Nice Select JS
   =======================================================================================*/
    $("select").niceSelect();

    /*======================================================================================
      Video Popup JS
   =======================================================================================*/
    $(".popup-video").magnificPopup({
      type: "iframe",
    });

    /*======================================================================================
      Hobble Effect JS
   =======================================================================================*/
    function hobbleEffect() {
      $(document)
        .on("mousemove", ".ed-hobble", function (event) {
          var halfW = this.clientWidth / 2;
          var halfH = this.clientHeight / 2;
          var coorX = halfW - (event.pageX - $(this).offset().left);
          var coorY = halfH - (event.pageY - $(this).offset().top);
          var degX1 = (coorY / halfH) * 8 + "deg";
          var degY1 = (coorX / halfW) * -8 + "deg";
          var degX3 = (coorY / halfH) * -15 + "px";
          var degY3 = (coorX / halfW) * 15 + "px";

          $(this)
            .find(".ed-hover-layer-1")
            .css("transform", function () {
              return (
                "perspective( 800px ) translate3d( 0, 0, 0 ) rotateX(" +
                degX1 +
                ") rotateY(" +
                degY1 +
                ")"
              );
            });
          $(this)
            .find(".ed-hover-layer-2")
            .css("transform", function () {
              return (
                "perspective( 800px ) translateX(" +
                degX3 +
                ") translateY(" +
                degY3 +
                ") scale(1.02)"
              );
            });
        })
        .on("mouseout", ".ed-hobble", function () {
          $(this).find(".ed-hover-layer-1").removeAttr("style");
          $(this).find(".ed-hover-layer-2").removeAttr("style");
        });
    }
    hobbleEffect();

    /*======================================================================================
      Hero Slider JS
    =======================================================================================*/
    $(".ed-hero__slider").owlCarousel({
      items: 1,
      autoplay: true,
      loop: true,
      margin: 0,
      touchDrag: false,
      mouseDrag: false,
      autoplayTimeout: 5000,
      autoplayHoverPause: false,
      animateOut: "fadeOut",
      animateIn: "fadeIn",
      smartSpeed: 500,
      merge: true,
      dots: false,
      nav: true,
      navText: [
        "<i class='fi fi-rs-arrow-left'></i>",
        "<i class='fi fi-rs-arrow-right'></i>",
      ],
    });

    /*======================================================================================
      Partner Slider JS
    =======================================================================================*/
    $(".ed-partner__slider").owlCarousel({
      items: 6,
      autoplay: true,
      loop: true,
      touchDrag: true,
      mouseDrag: true,
      autoplayTimeout: 2000,
      autoplayHoverPause: false,
      animateOut: "fadeOut",
      animateIn: "fadeIn",
      smartSpeed: 500,
      merge: true,
      dots: false,
      nav: false,
      margin: 20,
      responsive: {
        0: {
          items: 1,
        },
        300: {
          items: 2,
        },
        480: {
          items: 3,
        },

        768: {
          items: 4,
        },
        1024: {
          items: 6,
        },
        1200: {
          items: 6,
        },
      },
    });

    /*======================================================================================
      Partner Slider Two JS
    =======================================================================================*/
    const clientSliderTwo = new Swiper(".ed-partner__slider-2", {
      slidesPerView: 1,
      loop: true,
      speed: 5000,
      autoplay: {
        delay: 1,
        disableOnInteraction: false,
      },
      breakpoints: {
        360: {
          slidesPerView: 2,
        },
        576: {
          slidesPerView: 2,
        },
        768: {
          slidesPerView: 3,
        },
        992: {
          slidesPerView: 4,
        },
        1200: {
          slidesPerView: 3,
        },
      },
    });

    /*======================================================================================
      Partner Slider Three JS
    =======================================================================================*/
    const clientSliderThree = new Swiper(".ed-partner__slider-2-reverse", {
      slidesPerView: 1,
      loop: true,
      speed: 5000,
      autoplay: {
        delay: 1,
        disableOnInteraction: false,
        reverseDirection: true,
      },
      breakpoints: {
        360: {
          slidesPerView: 2,
        },
        576: {
          slidesPerView: 2,
        },
        768: {
          slidesPerView: 3,
        },
        992: {
          slidesPerView: 4,
        },
        1200: {
          slidesPerView: 3,
        },
      },
    });

    /*======================================================================================
      Testimonial Slider JS
     =======================================================================================*/
    $(".ed-testimonial__slider").owlCarousel({
      items: 1,
      autoplay: true,
      loop: true,
      touchDrag: true,
      mouseDrag: true,
      autoplayTimeout: 5000,
      autoplayHoverPause: false,
      smartSpeed: 500,
      merge: true,
      margin: 30,
      dots: false,
      nav: true,
      navText: [
        "<i class='fi fi-rs-arrow-left'></i>",
        "<i class='fi fi-rs-arrow-right'></i>",
      ],
    });

    /*======================================================================================
      Testimonial Slider Two JS
     =======================================================================================*/
    const testimonialSliderTwo = new Swiper(".ed-testimonial__slider-2", {
      // Optional parameters
      slidesPerView: 1,
      spaceBetween: 30,
      autoplay: {
        delay: 5000,
      },
      // If we need pagination
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },

      breakpoints: {
        576: {
          slidesPerView: 2,
        },
        768: {
          slidesPerView: 3,
        },
        1200: {
          slidesPerView: 4,
        },
      },
    });

    /*======================================================================================
      Testimonial Slider Three JS
     =======================================================================================*/
    const testimonialSliderThree = new Swiper(".ed-testimonial__slider-3", {
      // Optional parameters
      slidesPerView: 3,
      spaceBetween: 30,
      // autoplay: {
      //   delay: 5000,
      // },
      loop:true,
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },

      breakpoints: {
        360: {
          slidesPerView: 1,
        },
        576: {
          slidesPerView: 2,
        },
        768: {
          slidesPerView: 2,
        },
        1200: {
          slidesPerView: 3,
        },
      },
    
    });

    /*======================================================================================
      Category Slider JS
    =======================================================================================*/
    const categorySlider = new Swiper(".ed-category__slider", {
      // Optional parameters
      slidesPerView: 3,
      spaceBetween: 30,
      autoplay: {
        delay: 5000,
      },
      // If we need pagination
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
      // Navigation arrows
      navigation: {
        nextEl: ".slider-button-next",
        prevEl: ".slider-button-prev",
      },
      breakpoints: {
        576: {
          slidesPerView: 4,
        },
        992: {
          slidesPerView: 5,
        },
        1200: {
          slidesPerView: 6,
        },
        1600: {
          slidesPerView: 7,
        },
        1800: {
          slidesPerView: 8,
        },
      },
    });
  });

  /*======================================================================================
    Custom Cursor JS
  =======================================================================================*/
  function gsap_ed_custom_cursor() {
    var cursorBall = document.getElementById("cursor-ball");
    if (cursorBall) {
      let mouse = { x: 0, y: 0 };
      let pos = { x: 0, y: 0 };
      let ratio = 0.99;
      let active = false;
      gsap.set(cursorBall, {
        xPercent: -50,
        yPercent: -50,
        borderWidth: "1px",
        width: "40px",
        height: "40px",
      });
      document.addEventListener("mousemove", mouseMove);
      function mouseMove(e) {
        var scrollTop =
          window.pageYOffset || document.documentElement.scrollTop;
        mouse.x = e.pageX;
        mouse.y = e.pageY - scrollTop;
      }
      gsap.ticker.add(updatePosition);
      function updatePosition() {
        if (!active) {
          pos.x += (mouse.x - pos.x) * ratio;
          pos.y += (mouse.y - pos.y) * ratio;
          gsap.to(cursorBall, { duration: 0.4, x: pos.x, y: pos.y });
        }
      }

      // Common Area
      $("a, button, input[type=submit]").on("mouseenter", function (e) {
        gsap.to(cursorBall, {
          borderColor: "rgba(34, 34, 34, 0.05",
          scale: 1.7,
          opacity: 0.15,
          backgroundColor: "rgba(34, 34, 34, 0.2)",
        });
      });
      $("a, button, input[type=submit]").on("mouseleave", function (e) {
        gsap.to(cursorBall, {
          borderColor: "rgba(156, 156, 156, 0.5)",
          scale: 1,
          opacity: 1,
          backgroundColor: "transparent",
          width: "40px",
          height: "40px",
        });
        gsap.ticker.add(updatePosition);
      });
    }
  }
  gsap_ed_custom_cursor();
  /*======================================================================================
    Preloader JS
  =======================================================================================*/
  var prealoaderOption = $(window);
  prealoaderOption.on("load", function () {
    var preloader = jQuery(".ed-preloader");
    var preloaderArea = jQuery(".ed-preloader");
    preloader.fadeOut();
    preloaderArea.delay(350).fadeOut("slow");
  });

  /*======================================================================================
    Smooth Scroll JS
  =======================================================================================*/
  function smoothSctoll() {
    $(".smooth a").on("click", function (event) {
      var target = $(this.getAttribute("href"));
      if (target.length) {
        event.preventDefault();
        $("html, body")
          .stop()
          .animate(
            {
              scrollTop: target.offset().top - 120,
            },
            1000
          );
      }
    });
  }

  smoothSctoll();
  $(document).ready(function () {
    if ($("#smooth-wrapper").length && $("#smooth-content").length) {
      gsap.registerPlugin(
        ScrollTrigger,
        ScrollSmoother,
        TweenMax,
        ScrollToPlugin
      );
  
      gsap.config({
        nullTargetWarn: false,
      });
  
      let smoother = ScrollSmoother.create({
        smooth: 0.5,
        effects: true,
        smoothTouch: 0.5,
        normalizeScroll: false,
        ignoreMobileResize: true,
      });
    }
  });
  

  /*======================================================================================
    Split Text Animation JS
  =======================================================================================*/
  var st = $(".ed-split-text");
  if (st.length == 0) return;
  gsap.registerPlugin(SplitText);
  st.each(function (index, el) {
    el.split = new SplitText(el, {
      type: "lines,words,chars",
      linesClass: "tp-split-line",
    });
    gsap.set(el, { perspective: 400 });
    if ($(el).hasClass("right")) {
      gsap.set(el.split.chars, {
        opacity: 0,
        x: "50",
        ease: "Back.easeOut",
      });
    }
    if ($(el).hasClass("left")) {
      gsap.set(el.split.chars, {
        opacity: 0,
        x: "-50",
        ease: "circ.out",
      });
    }
    if ($(el).hasClass("up")) {
      gsap.set(el.split.chars, {
        opacity: 0,
        y: "80",
        ease: "circ.out",
      });
    }
    if ($(el).hasClass("down")) {
      gsap.set(el.split.chars, {
        opacity: 0,
        y: "-80",
        ease: "circ.out",
      });
    }
    el.anim = gsap.to(el.split.chars, {
      scrollTrigger: {
        trigger: el,
        start: "top 90%",
      },
      x: "0",
      y: "0",
      rotateX: "0",
      scale: 1,
      opacity: 1,
      duration: 0.4,
      stagger: 0.02,
    });
  });
})(jQuery);

/*======================================================================================
  Element Move JS
=======================================================================================*/
const elementWrapper = document.querySelector(".element-wrapper");
const elementMove = document.querySelectorAll(".element-move");
const elementMoveX = document.querySelectorAll(".element-move-x");

elementWrapper.addEventListener("mousemove", (e) => {
  const { clientX: mouseX, clientY: mouseY } = e;

  const centerX = elementWrapper.clientWidth / 2;
  const centerY = elementWrapper.clientHeight / 2;

  const offsetX = (mouseX - centerX) / 70;
  const offsetY = (mouseY - centerY) / 70;

  elementMove.forEach((image, index) => {
    const offset = index + 1;
    image.style.transform = `translate(${offsetX * offset}px, ${
      offsetY * offset
    }px)`;
  });
  elementMoveX.forEach((image, index) => {
    const offset = index + 2;
    image.style.transform = `translate(${offsetX * offset}px)`;
  });
});

/*======================================================================================
  Increment Decrement JS
=======================================================================================*/

// Function to handle quantity increment and decrement
const decreaseButtons = document.querySelectorAll(
  ".ed-cart__quantity-decrease"
);
const increaseButtons = document.querySelectorAll(
  ".ed-cart__quantity-increase"
);

// Only proceed if both decrease and increase buttons exist in the DOM
if (decreaseButtons.length > 0 && increaseButtons.length > 0) {
  decreaseButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const quantityInput = this.nextElementSibling;
      if (quantityInput) {
        // Check if quantity input exists
        let quantity = parseInt(quantityInput.value);

        if (quantity > 1) {
          quantity--;
          quantityInput.value = quantity;
        }
      }
    });
  });

  increaseButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const quantityInput = this.previousElementSibling;
      if (quantityInput) {
        // Check if quantity input exists
        let quantity = parseInt(quantityInput.value);

        quantity++;
        quantityInput.value = quantity;
      }
    });
  });
}

/*======================================================================================
  Mobile Menu Offcanvas JS 
=======================================================================================*/

var getSiblings = function (elem) {
    const siblings = [];
    let sibling = elem.parentNode.firstChild;
    for (; sibling; )
      1 === sibling.nodeType && sibling !== elem && siblings.push(sibling),
        (sibling = sibling.nextSibling);
    return siblings;
  },
  slideUp = (target, time) => {
    const duration = time || 500;
    (target.style.transitionProperty = "height, margin, padding"),
      (target.style.transitionDuration = duration + "ms"),
      (target.style.boxSizing = "border-box"),
      (target.style.height = target.offsetHeight + "px"),
      target.offsetHeight,
      (target.style.overflow = "hidden"),
      (target.style.height = 0),
      window.setTimeout(() => {
        (target.style.display = "none"),
          target.style.removeProperty("height"),
          target.style.removeProperty("overflow"),
          target.style.removeProperty("transition-duration"),
          target.style.removeProperty("transition-property");
      }, duration);
  },
  slideDown = (target, time) => {
    const duration = time || 500;
    target.style.removeProperty("display");
    let display = window.getComputedStyle(target).display;
    "none" === display && (display = "block"), (target.style.display = display);
    const height = target.offsetHeight;
    (target.style.overflow = "hidden"),
      (target.style.height = 0),
      target.offsetHeight,
      (target.style.boxSizing = "border-box"),
      (target.style.transitionProperty = "height, margin, padding"),
      (target.style.transitionDuration = duration + "ms"),
      (target.style.height = height + "px"),
      window.setTimeout(() => {
        target.style.removeProperty("height"),
          target.style.removeProperty("overflow"),
          target.style.removeProperty("transition-duration"),
          target.style.removeProperty("transition-property");
      }, duration);
  };

const offcanvasHeader = function () {
  (offcanvasMenu = document.querySelector(".offcanvas__menu")),
    offcanvasMenu &&
      offcanvasMenu
        .querySelectorAll(".offcanvas__sub_menu")
        .forEach(function (ul) {
          const subMenuToggle = document.createElement("button");
          subMenuToggle.classList.add("offcanvas__sub_menu_toggle"),
            ul.parentNode.appendChild(subMenuToggle);
        });

  let mobileMenuWrapper = document.querySelector(".offcanvas__menu_ul");
  mobileMenuWrapper &&
    mobileMenuWrapper.addEventListener("click", function (e) {
      let targetElement = e.target;
      if (targetElement.classList.contains("offcanvas__sub_menu_toggle")) {
        const parent = targetElement.parentElement;
        parent.classList.contains("active")
          ? (targetElement.classList.remove("active"),
            parent.classList.remove("active"),
            parent
              .querySelectorAll(".offcanvas__sub_menu")
              .forEach(function (subMenu) {
                subMenu.parentElement.classList.remove("active"),
                  subMenu.nextElementSibling.classList.remove("active"),
                  slideUp(subMenu);
              }))
          : (targetElement.classList.add("active"),
            parent.classList.add("active"),
            slideDown(targetElement.previousElementSibling),
            getSiblings(parent).forEach(function (item) {
              item.classList.remove("active"),
                item
                  .querySelectorAll(".offcanvas__sub_menu")
                  .forEach(function (subMenu) {
                    subMenu.parentElement.classList.remove("active"),
                      subMenu.nextElementSibling.classList.remove("active"),
                      slideUp(subMenu);
                  });
            }));
      }
    });
};
offcanvasHeader();
