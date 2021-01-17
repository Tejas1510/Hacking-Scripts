
!(function ($) {
  "use strict";

  // Smooth scroll for the navigation menu and links with .scrollto classes
  var scrolltoOffset = $('#header').outerHeight() - 1;
  $(document).on('click', '.nav-menu a, .mobile-nav a, .scrollto', function (e) {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      if (target.length) {
        e.preventDefault();

        var scrollto = target.offset().top - scrolltoOffset;

        if ($(this).attr("href") == '#header') {
          scrollto = 0;
        }

        $('html, body').animate({
          scrollTop: scrollto
        }, 1500, 'easeInOutExpo');

        if ($(this).parents('.nav-menu, .mobile-nav').length) {
          $('.nav-menu .active, .mobile-nav .active').removeClass('active');
          $(this).closest('li').addClass('active');
        }

        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active');
          $('.mobile-nav-toggle i').toggleClass('icofont-navigation-menu icofont-close');
          $('.mobile-nav-overly').fadeOut();
        }
        return false;
      }
    }
  });

  // Activate smooth scroll on page load with hash links in the url
  $(document).ready(function () {
    if (window.location.hash) {
      var initial_nav = window.location.hash;
      if ($(initial_nav).length) {
        var scrollto = $(initial_nav).offset().top - scrolltoOffset;
        $('html, body').animate({
          scrollTop: scrollto
        }, 1500, 'easeInOutExpo');
      }
    }
  });

  // Mobile Navigation
  if ($('.nav-menu').length) {
    var $mobile_nav = $('.nav-menu').clone().prop({
      class: 'mobile-nav d-lg-none'
    });
    $('body').append($mobile_nav);
    $('.mobile-nav .nav-logo').remove();
    $('body').prepend('<button type="button" class="mobile-nav-toggle d-lg-none"><i class="icofont-navigation-menu"></i></button>');
    $('body').append('<div class="mobile-nav-overly"></div>');

    $(document).on('click', '.mobile-nav-toggle', function (e) {
      $('body').toggleClass('mobile-nav-active');
      $('.mobile-nav-toggle i').toggleClass('icofont-navigation-menu icofont-close');
      $('.mobile-nav-overly').toggle();
    });

    $(document).on('click', '.mobile-nav .drop-down > a', function (e) {
      e.preventDefault();
      $(this).next().slideToggle(300);
      $(this).parent().toggleClass('active');
    });

    $(document).click(function (e) {
      var container = $(".mobile-nav, .mobile-nav-toggle");
      if (!container.is(e.target) && container.has(e.target).length === 0) {
        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active');
          $('.mobile-nav-toggle i').toggleClass('icofont-navigation-menu icofont-close');
          $('.mobile-nav-overly').fadeOut();
        }
      }
    });
  } else if ($(".mobile-nav, .mobile-nav-toggle").length) {
    $(".mobile-nav, .mobile-nav-toggle").hide();
  }

  // Navigation active state on scroll
  var nav_sections = $('section');
  var main_nav = $('.nav-menu, .mobile-nav');

  $(window).on('scroll', function () {
    var cur_pos = $(this).scrollTop() + 200;

    nav_sections.each(function () {
      var top = $(this).offset().top,
        bottom = top + $(this).outerHeight();

      if (cur_pos >= top && cur_pos <= bottom) {
        if (cur_pos <= bottom) {
          main_nav.find('li').removeClass('active');
        }
        main_nav.find('a[href="#' + $(this).attr('id') + '"]').parent('li').addClass('active');
      }
      if (cur_pos < 300) {
        $(".nav-menu ul:first li:first").addClass('active');
      }
    });
  });

  // Stick the header at top on scroll
  $("#header").sticky({
    topSpacing: 0,
    zIndex: '50'
  });

  // Back to top button
  $(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
      $('.back-to-top').fadeIn('slow');
    } else {
      $('.back-to-top').fadeOut('slow');
    }
  });

  $('.back-to-top').click(function () {
    $('html, body').animate({
      scrollTop: 0
    }, 1500, 'easeInOutExpo');
    return false;
  });

  // Porfolio isotope and filter
  $(window).on('load', function () {
    var portfolioIsotope = $('.portfolio-container').isotope({
      itemSelector: '.portfolio-item',
      layoutMode: 'fitRows'
    });

    $('#portfolio-flters li').on('click', function () {
      $("#portfolio-flters li").removeClass('filter-active');
      $(this).addClass('filter-active');

      portfolioIsotope.isotope({
        filter: $(this).data('filter')
      });
      aos_init();
    });

    // Initiate venobox (lightbox feature used in portofilo)
    $(document).ready(function () {
      $('.venobox').venobox();
    });
  });

  // Testimonials carousel (uses the Owl Carousel library)
  $(".testimonials-carousel").owlCarousel({
    autoplay: true,
    dots: true,
    loop: true,
    items: 1
  });

  // Portfolio details carousel
  $(".portfolio-details-carousel").owlCarousel({
    autoplay: true,
    dots: true,
    loop: true,
    items: 1
  });

  // Init AOS
  function aos_init() {
    AOS.init({
      duration: 600,
      once: true
    });
  }
  $(window).on('load', function () {
    aos_init();
  });

})(jQuery);

/*
var request = new XMLHttpRequest();
request.open('GET', 'https://api.github.com/repos/Tejas1510/Hacking-Scripts/contents/Python', true)

request.onload = function(){
  var data = JSON.parse(this.response);
  console.log(data);
}

request.send();
*/

function fetchDataAndroid() {
  fetch('https://api.github.com/repos/Tejas1510/Hacking-Scripts/contents/Android Studio Scripts').then(response => {
    return response.json();
  })
    .then(data => {
      const html = data.map(script => {
        return `
        <div class="col-md-6 d-flex align-items-stretch" data-aos="fade-up">
        <div class="card">
          <div class="card-img">
            <img src="assets/img/services.jpg" alt="...">
          </div>
          <div class="card-body">
            <h4 class="card-title"><a href="#">${script.name}</a></h4>
            <h6 class="card-title">Created by - Hacking Script</h6>
            <h2 class="card-title"><a class="github-formatter" href="${script._links.html}"><i class="fa fa-github" style="font-size:36px"></i></a></h2>
          </div>
        </div>
      </div>        
        `;
      }).join("");

      // document.querySelector('.card-title').innerHTML = '<h4>'+data[0].name+'</h4>'
      document.querySelector('.row-android').insertAdjacentHTML("afterbegin", html);

    })
    .catch(error1 => {
      console.log(error1);
    })
}

fetchDataAndroid();

function fetchDataC() {
  fetch('https://api.github.com/repos/Tejas1510/Hacking-Scripts/contents/C').then(response => {
    return response.json();
  })
    .then(data => {
      const html = data.map(script => {
        return `
          <div class="col-md-6 d-flex align-items-stretch" data-aos="fade-up">
          <div class="card">
            <div class="card-img">
              <img src="assets/img/aboutus.jpg" alt="...">
            </div>
            <div class="card-body">
              <h4 class="card-title"><a href="#">${script.name}</a></h4>
              <h6 class="card-title">Created by - Hacking Script</h6>
              <h2 class="card-title"><a class="github-formatter" href="${script._links.html}"><i class="fa fa-github" style="font-size:36px"></i></a></h2>
            </div>
          </div>
        </div>        
          `;
      }).join("");

      // document.querySelector('.card-title').innerHTML = '<h4>'+data[0].name+'</h4>'
      document.querySelector('.row-c').insertAdjacentHTML("afterbegin", html);

    })
    .catch(error1 => {
      console.log(error1);
    })
}

fetchDataC();


function fetchDataJava() {
  fetch('https://api.github.com/repos/Tejas1510/Hacking-Scripts/contents/Java').then(response => {
    return response.json();
  })
    .then(data => {
      const html = data.map(script => {
        if (script.name != "bin" && script.name != ".classpath" && script.name != ".project") {
          return `
        <div class="col-md-6 d-flex align-items-stretch" data-aos="fade-up">
        <div class="card">
        <div class="card-img">
        <img src="assets/img/services.jpg" alt="...">
      </div>
          <div class="card-body">
            <h4 class="card-title"><a href="#">${script.name}</a></h4>
            <h6 class="card-title">Created by - Hacking Script</h6>
            <h2 class="card-title"><a class="github-formatter" href="${script._links.html}"><i class="fa fa-github" style="font-size:36px"></i></a></h2>
          </div>
        </div>
      </div>        
        `;
        }

      }).join("");

      // document.querySelector('.card-title').innerHTML = '<h4>'+data[0].name+'</h4>'
      document.querySelector('.row-java').insertAdjacentHTML("afterbegin", html);

    })
    .catch(error1 => {
      console.log(error1);
    })
}

fetchDataJava();


function fetchDataJavaScript() {
  fetch('https://api.github.com/repos/Tejas1510/Hacking-Scripts/contents/Javascript').then(response => {
    return response.json();
  })
    .then(data => {

      const html = data.map(script => {
        // console.log(script);
        return `
        <div class="col-md-6 d-flex align-items-stretch" data-aos="fade-up">
        <div class="card">
          <div class="card-img">
            <img src="assets/img/aboutus.jpg" alt="...">
          </div>
          <div class="card-body">
            <h4 class="card-title"><a href="#">${script.name}</a></h4>
            <h6 class="card-title">Created by - Hacking Script</h6>
            <h2 class="card-title"><a class="github-formatter" href="${script._links.html}"><i class="fa fa-github" style="font-size:36px"></i></a></h2>
          </div>
        </div>
      </div>        
        `;


      }).join("");

      // document.querySelector('.card-title').innerHTML = '<h4>'+data[0].name+'</h4>'
      document.querySelector('.row-javascript').insertAdjacentHTML("afterbegin", html);

    })
    .catch(error1 => {
      console.log(error1);
    })
}

fetchDataJavaScript();

function fetchDataPython() {

  fetch('https://api.github.com/repos/Tejas1510/Hacking-Scripts/contents/Python').then(response => {
    return response.json();
  })
    .then(data => {
      const html = data.map(script => {
        return `
        <div class="col-md-6 d-flex align-items-stretch" data-aos="fade-up">
        <div class="card">
          <div class="card-img">
            <img src="assets/img/services.jpg" alt="...">
          </div>
          <div class="card-body">
            <h4 class="card-title"><a href="#">${script.name}</a></h4>
            <h6 class="card-title">Created by - Hacking Script</h6>
            <h2 class="card-title"><a class="github-formatter" href="${script._links.html}"><i class="fa fa-github" style="font-size:36px"></i></a></h2>
          </div>
        </div>
      </div>        
        `;
      }).join("");

      // document.querySelector('.card-title').innerHTML = '<h4>'+data[0].name+'</h4>'
      document.querySelector('.row-python').insertAdjacentHTML("afterbegin", html);

    })
    .catch(error1 => {
      console.log(error1);
    })
}

fetchDataPython();


function fetchDataReactJs() {
  fetch('https://api.github.com/repos/Tejas1510/Hacking-Scripts/contents/Reactjs').then(response => {
    return response.json();
  })
    .then(data => {
      const html = data.map(script => {
        return `
          <div class="col-md-6 d-flex align-items-stretch" data-aos="fade-up">
          <div class="card">
            <div class="card-img">
              <img src="assets/img/aboutus.jpg" alt="...">
            </div>
            <div class="card-body">
              <h4 class="card-title"><a href="#">${script.name}</a></h4>
              <h6 class="card-title">Created by - Hacking Script</h6>
              <h2 class="card-title"><a class="github-formatter" href="${script._links.html}"><i class="fa fa-github" style="font-size:36px"></i></a></h2>
            </div>
          </div>
        </div>        
          `;
      }).join("");

      // document.querySelector('.card-title').innerHTML = '<h4>'+data[0].name+'</h4>'
      document.querySelector('.row-reactjs').insertAdjacentHTML("afterbegin", html);

    })
    .catch(error1 => {
      console.log(error1);
    })
}

fetchDataReactJs();

/*
<p class="card-text">This is python script which notifies you when price of your product falls below your expected price.
          Bs4 library is used for web scrapping and SMTP library is used for sending emails.</p>
      <!--  <div class="read-more"><a href="#"><i class="icofont-arrow-right"></i> Read More</a></div>  -->
*/


function randomImage() {
  var path = 'assets/img/',
    imgs = ['service-details-1.jpg', 'service-details-2.jpg', 'service-details-3.jpg', 'service-details-4.jpg', 'services.jpg'],
    i = Math.floor(Math.random() * imgs.length);
  $('.myimage').append("<img src='" + path + imgs[i] + "'>").hide().fadeIn(2000);
}

randomImage();