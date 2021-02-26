
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

//an array of objects containing links to images
const image_urls = [
  {
    name: "Calculator",
    link: "https://images.unsplash.com/photo-1612622826776-cd8b6da23632?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mzh8fGNhbGN1bGF0b3J8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "CurrencyConverter",
    link: "https://images.unsplash.com/photo-1563986768711-b3bde3dc821e?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTV8fGN1cnJlbmN5JTIwZXhjaGFuZ2V8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "DiceRoller",
    link: "https://images.unsplash.com/photo-1605870445919-838d190e8e1b?ixid=MXwxMjA3fDB8MHxzZWFyY2h8M3x8ZGljZXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "DrawingApp",
    link: "https://images.unsplash.com/photo-1524642176501-f3393ec0b116?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mjl8fGRyYXd8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "GuessTheNumberGame",
    link: "https://images.unsplash.com/photo-1502570149819-b2260483d302?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8bnVtYmVyc3xlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Memer",
    link: "https://images.unsplash.com/photo-1607798421660-7d2c0bcff934?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MjF8fG1lbWV8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Random Password Generator",
    link: "https://images.unsplash.com/photo-1504203700686-f21e703e5f1c?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mnx8cGFzc3dvcmR8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "TicTacToe",
    link: "https://images.unsplash.com/photo-1608111282283-df105d21a7ce?ixid=MXwxMjA3fDB8MHxzZWFyY2h8OHx8dGljJTIwdGFjfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Network_Scanner",
    link: "https://images.unsplash.com/photo-1520869562399-e772f042f422?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTB8fG5ldHdvcmt8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "RandomPasswordsGenerator",
    link: "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTB8fHBhc3N3b3JkfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "BitcoinPriceSimulator",
    link: "https://images.unsplash.com/photo-1543699565-003b8adda5fc?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTZ8fGJpdGNvaW58ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Currency-converter",
    link: "https://images.unsplash.com/photo-1563986768711-b3bde3dc821e?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTV8fGN1cnJlbmN5JTIwZXhjaGFuZ2V8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Github-Data-Fetcher",
    link: "https://images.unsplash.com/photo-1556075798-4825dfaaf498?ixid=MXwxMjA3fDB8MHxzZWFyY2h8N3x8Z2l0aHVifGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "markdown-previewer",
    link: "https://images.unsplash.com/photo-1579389083078-4e7018379f7e?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTV8fGVtYWlsfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "qr-code-generator",
    link: "https://images.unsplash.com/photo-1595079676339-1534801ad6cf?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTV8fHFyJTIwY29kZXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "sort-visualizer",
    link: "https://images.unsplash.com/photo-1591696205602-2f950c417cb9?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mnx8Y2hhcnR8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "AutomatingAmazon",
    link: "https://images.unsplash.com/photo-1523474253046-8cd2748b5fd2?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8YW1hem9ufGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "CompleteIPAddressDetailsFinder",
    link: "https://images.unsplash.com/photo-1590233033196-a50b826b059b?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8bWFwfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "DirectoryLister",
    link: "https://images.unsplash.com/photo-1506612966115-4ee2c4c93e2d?ixid=MXwxMjA3fDB8MHxzZWFyY2h8OXx8ZmlsZXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "DuplicateFileRemover",
    link: "https://images.unsplash.com/photo-1464865885825-be7cd16fad8d?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NHx8ZmlsZXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Guessing Game IN JAVA",
    link: "https://images.unsplash.com/photo-1588591795084-1770cb3be374?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MjB8fGdhbWV8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "MorseCode Generator",
    link: "https://images.unsplash.com/photo-1514820402329-de527fdd2e6d?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTN8fG1vcnNlJTIwY29kZXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "NumberGuessingGame",
    link: "https://images.unsplash.com/photo-1502570149819-b2260483d302?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8bnVtYmVyc3xlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "PDF-Encrypter",
    link: "https://images.unsplash.com/photo-1477039181047-efb4357d01bd?ixid=MXwxMjA3fDB8MHxzZWFyY2h8M3x8ZW5jcnlwdHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "RandomPasswordGenerator",
    link: "https://images.unsplash.com/photo-1504203700686-f21e703e5f1c?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mnx8cGFzc3dvcmR8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "RollDice",
    link: "https://images.unsplash.com/photo-1522069213448-443a614da9b6?ixid=MXwxMjA3fDB8MHxzZWFyY2h8OXx8ZGljZXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "ScreenshotTaker",
    link: "https://images.unsplash.com/photo-1566241477600-ac026ad43874?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mnx8c2NyZWVuc2hvdHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "SizeOfDirectory",
    link: "https://images.unsplash.com/photo-1589995186011-a7b485edc4bf?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mnx8aGRkfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "CSV data in websie",
    link: "https://images.unsplash.com/photo-1550645612-83f5d594b671?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NDZ8fGRhdGF8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "CircularImages",
    link: "https://images.unsplash.com/photo-1478754117940-f5bc84311001?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mnx8Y2lyY3VsYXJ8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "CountingDays",
    link: "https://images.unsplash.com/photo-1610888662651-05dbdec7cfae?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MzJ8fGNhbGVuZGFyfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Dice",
    link: "https://images.unsplash.com/photo-1522069213448-443a614da9b6?ixid=MXwxMjA3fDB8MHxzZWFyY2h8OXx8ZGljZXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Drawing App",
    link: "https://images.unsplash.com/photo-1524642176501-f3393ec0b116?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mjl8fGRyYXd8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Geo-location",
    link: "https://images.unsplash.com/photo-1569336415962-a4bd9f69cd83?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTB8fG1hcHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Maze-Game",
    link: "https://images.unsplash.com/photo-1590278458425-6aa3912a48a5?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8bWF6ZXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Notes App",
    link: "https://images.unsplash.com/photo-1517842645767-c639042777db?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8bm90ZXN8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Number Guessing Game",
    link: "https://images.unsplash.com/photo-1502570149819-b2260483d302?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8bnVtYmVyc3xlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Password Generator",
    link: "https://images.unsplash.com/photo-1504203700686-f21e703e5f1c?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mnx8cGFzc3dvcmR8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Pokedex",
    link: "https://images.unsplash.com/photo-1542779283-429940ce8336?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8cG9rZW1vbnxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Qr code generator",
    link: "https://images.unsplash.com/photo-1595079676339-1534801ad6cf?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTV8fHFyJTIwY29kZXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Random Email Generator",
    link: "https://images.unsplash.com/photo-1557200134-90327ee9fafa?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mnx8ZW1haWx8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Rock, Paper, scissors",
    link: "https://images.unsplash.com/photo-1522032662723-6649e699785f?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8cm9jayUyMHBhcGVyJTIwc2Npc3NvcnN8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "SudokuSolver",
    link: "https://images.unsplash.com/photo-1526566661780-1a67ea3c863e?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8cHV6emxlfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "TextEditior",
    link: "https://images.unsplash.com/photo-1542831371-29b0f74f9713?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8Y29kZXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "UrlShortner",
    link: "https://images.unsplash.com/photo-1598662779094-110c2bad80b5?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTJ8fGtleWJvYXJkfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "dynamic display(moment extension)",
    link: "https://images.unsplash.com/photo-1555940280-66bf87aa823d?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MzB8fGRpc3BsYXl8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "light-bulb",
    link: "https://images.unsplash.com/photo-1493402702251-a6e5320337f7?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mnx8bGlnaHQlMjBidWxifGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Tic Tac Toe Game",
    link: "https://images.unsplash.com/photo-1608111282283-df105d21a7ce?ixid=MXwxMjA3fDB8MHxzZWFyY2h8OHx8dGljJTIwdGFjfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Todo-List",
    link: "https://images.unsplash.com/photo-1547480053-7d174f67b557?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8dG8lMjBkbyUyMGxpc3R8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "todoList-react",
    link: "https://images.unsplash.com/photo-1547480053-7d174f67b557?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8dG8lMjBkbyUyMGxpc3R8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "TODO",
    link: "https://images.unsplash.com/photo-1547480053-7d174f67b557?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8dG8lMjBkbyUyMGxpc3R8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Amazon_Price_Tracker",
    link: "https://images.unsplash.com/photo-1523474253046-8cd2748b5fd2?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8YW1hem9ufGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "AnimeTracker",
    link: "https://images.unsplash.com/photo-1581833971358-2c8b550f87b3?ixid=MXwxMjA3fDB8MHxzZWFyY2h8M3x8YW5pbWV8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Automate Login",
    link: "https://images.unsplash.com/photo-1504203700686-f21e703e5f1c?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mnx8cGFzc3dvcmR8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "BMI_GUI",
    link: "https://images.unsplash.com/photo-1523901839036-a3030662f220?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mnx8c2NhbGUlMjB3ZWlnaHR8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Broswer",
    link: "https://images.unsplash.com/photo-1590595906931-81f04f0ccebb?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8YnJvd3NlcnxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Bulk-EmailSender",
    link: "https://images.unsplash.com/photo-1557200134-90327ee9fafa?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mnx8ZW1haWx8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "CPU_Temperature",
    link: "https://images.unsplash.com/photo-1555617981-dac3880eac6e?ixid=MXwxMjA3fDB8MHxzZWFyY2h8M3x8Y3B1fGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Caesar-Cipher",
    link: "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NHx8Y29kZXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Calculate-distance",
    link: "https://images.unsplash.com/photo-1612622826776-cd8b6da23632?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mzh8fGNhbGN1bGF0b3J8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Certificate_Generator",
    link: "https://images.unsplash.com/photo-1589330694653-ded6df03f754?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8Y2VydGlmaWNhdGV8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Chrome Dinosaur Automation",
    link: "https://images.unsplash.com/photo-1584844115436-473887b1e327?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NXx8ZGlub3NhdXJ8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Coffee-Machine",
    link: "https://images.unsplash.com/photo-1469957761306-556935073eba?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NHx8Y29mZmVlJTIwbWFjaGluZXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Colortoblack",
    link: "https://images.unsplash.com/photo-1527843812948-a8c2ddd2fb68?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTJ8fGJsYWNrfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "CovidLiveTracker",
    link: "https://images.unsplash.com/photo-1603448448989-336b90551bf6?ixid=MXwxMjA3fDB8MHxzZWFyY2h8M3x8Y292aWQlMjBhcHB8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "DDoS",
    link: "https://images.unsplash.com/photo-1510511459019-5dda7724fd87?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NXx8bWF0cml4fGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Dice Rolling Simulator using Python",
    link: "https://images.unsplash.com/photo-1522069213448-443a614da9b6?ixid=MXwxMjA3fDB8MHxzZWFyY2h8OXx8ZGljZXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Discovering Subdomains",
    link: "https://images.unsplash.com/photo-1592991538534-00972b6f59ab?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTN8fGtleWJvYXJkfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Disk_Space_Analyser",
    link: "https://images.unsplash.com/photo-1555617981-dac3880eac6e?ixid=MXwxMjA3fDB8MHxzZWFyY2h8M3x8Y3B1fGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Desktop_notifier",
    link: "https://images.unsplash.com/photo-1588200908342-23b585c03e26?ixid=MXwxMjA3fDB8MHxzZWFyY2h8OXx8ZGVza3RvcHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Duplicate Image Remover",
    link: "https://images.unsplash.com/photo-1590421631770-c6fe140592b4?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mzd8fGZpbGV8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "E-Dictionary",
    link: "https://images.unsplash.com/photo-1476357471311-43c0db9fb2b4?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NHx8ZGljdGlvbmFyeXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Extract-Metadata",
    link: "https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8ZGF0YXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Facebook_Auto_Post",
    link: "https://images.unsplash.com/photo-1432888622747-4eb9a8efeb07?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxzZWFyY2h8Nnx8ZmFjZWJvb2t8ZW58MHx8MHw%3D&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Geeks for Geeks Article Downloader",
    link: "https://images.unsplash.com/photo-1587620962725-abab7fe55159?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8cHJvZ3JhbW1pbmd8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "GradientDescent",
    link: "https://images.unsplash.com/photo-1579547945478-a6681fb3c3c9?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxzZWFyY2h8MzN8fGdyYWRpZW50fGVufDB8fDB8&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "ImgFormatConverterFinal",
    link: "https://images.unsplash.com/photo-1505226755626-21044548b8aa?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NXx8aW1hZ2UlMjBmb3JtYXR8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Instagram scraping",
    link: "https://images.unsplash.com/photo-1505322747495-6afdd3b70760?ixid=MXwxMjA3fDB8MHxzZWFyY2h8M3x8aW5zdGFncmFtfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Internshala_Scrapper",
    link: "https://images.unsplash.com/photo-1542903660-eedba2cda473?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Nnx8ZGF0YXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Magic Pen",
    link: "https://images.unsplash.com/photo-1585336261022-680e295ce3fe?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NXx8cGVufGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "MoorseCodeGenerator",
    link: "https://images.unsplash.com/photo-1514820402329-de527fdd2e6d?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTN8fG1vcnNlJTIwY29kZXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "MorseCodeTranslator",
    link: "https://images.unsplash.com/photo-1514820402329-de527fdd2e6d?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTN8fG1vcnNlJTIwY29kZXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Network_scanner",
    link: "https://images.unsplash.com/photo-1520869562399-e772f042f422?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTB8fG5ldHdvcmt8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "PasswordStrenght",
    link: "https://images.unsplash.com/photo-1504203700686-f21e703e5f1c?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mnx8cGFzc3dvcmR8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Pdf_Reader",
    link: "https://images.unsplash.com/photo-1477039181047-efb4357d01bd?ixid=MXwxMjA3fDB8MHxzZWFyY2h8M3x8ZW5jcnlwdHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Random-Email-Generator",
    link: "https://images.unsplash.com/photo-1557200134-90327ee9fafa?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mnx8ZW1haWx8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "RestNotifier",
    link: "https://images.unsplash.com/photo-1554177255-61502b352de3?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Nnx8bm90aWZpY2F0aW9ufGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Screen Recorder",
    link: "https://images.unsplash.com/photo-1593642634315-48f5414c3ad9?ixid=MXwxMjA3fDF8MHxzZWFyY2h8MXx8c2NyZWVufGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "ScreenShot Taker",
    link: "https://images.unsplash.com/photo-1566241477600-ac026ad43874?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mnx8c2NyZWVuc2hvdHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Shutdown-Restart Computer",
    link: "https://images.unsplash.com/photo-1559163454-e7d1e00a4e54?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTR8fHBjfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Snake Game",
    link: "https://images.unsplash.com/photo-1567391454009-0894f63e5550?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTV8fGdhbWV8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Text Translator",
    link: "https://images.unsplash.com/photo-1488590528505-98d2b5aba04b?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxzZWFyY2h8M3x8dnMlMjBjb2RlfGVufDB8fDB8&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "TextToSpeech",
    link: "https://images.unsplash.com/photo-1603336540413-009bd9dc5133?ixid=MXwxMjA3fDB8MHxzZWFyY2h8OHx8ZGVhZnxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Todoapp",
    link: "https://images.unsplash.com/photo-1547480053-7d174f67b557?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8dG8lMjBkbyUyMGxpc3R8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "ToonifyImage",
    link: "https://images.unsplash.com/photo-1581833971358-2c8b550f87b3?ixid=MXwxMjA3fDB8MHxzZWFyY2h8M3x8YW5pbWV8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "URLShortner",
    link: "https://images.unsplash.com/photo-1598662779094-110c2bad80b5?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTJ8fGtleWJvYXJkfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Unzip files",
    link: "https://images.unsplash.com/photo-1464865885825-be7cd16fad8d?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NHx8ZmlsZXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Song-Lyrics-Fetcher",
    link: "https://images.unsplash.com/photo-1520446266423-6daca23fe8c7?ixid=MXwxMjA3fDB8MHxzZWFyY2h8M3x8c29uZ3xlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Video to Gif",
    link: "https://images.unsplash.com/photo-1493804714600-6edb1cd93080?ixid=MXwxMjA3fDB8MHxzZWFyY2h8M3x8dmlkZW98ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "WebCrawler",
    link: "https://images.unsplash.com/photo-1550645612-83f5d594b671?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NDZ8fGRhdGF8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Website Blocker",
    link: "https://images.unsplash.com/photo-1546617885-4822125f891e?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NHx8c3RvcHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "WhatsApp_Message_Automation",
    link: "https://images.unsplash.com/photo-1519069060891-f8c50519bf39?ixid=MXwxMjA3fDB8MHxzZWFyY2h8M3x8d2hhdHNhcHB8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "Wifi Connected Device",
    link: "https://images.unsplash.com/photo-1516044734145-07ca8eef8731?ixid=MXwxMjA3fDB8MHxzZWFyY2h8M3x8d2lmaXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "WifiConnectionFinder",
    link: "https://images.unsplash.com/photo-1583474884909-230dac058b63?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8d2lmaXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "basic GUI calculator",
    link: "https://images.unsplash.com/photo-1612622826776-cd8b6da23632?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mzh8fGNhbGN1bGF0b3J8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "convert_csv_to_markdown_table",
    link: "https://images.unsplash.com/photo-1550645612-83f5d594b671?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NDZ8fGRhdGF8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "geo_location_from_IP_address",
    link: "https://images.unsplash.com/photo-1569336415962-a4bd9f69cd83?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTB8fG1hcHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "keylogger",
    link: "https://images.unsplash.com/photo-1592991538534-00972b6f59ab?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTN8fGtleWJvYXJkfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "mergetwopdf",
    link: "https://images.unsplash.com/photo-1477039181047-efb4357d01bd?ixid=MXwxMjA3fDB8MHxzZWFyY2h8M3x8ZW5jcnlwdHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "passwordGenerator",
    link: "https://images.unsplash.com/photo-1504203700686-f21e703e5f1c?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mnx8cGFzc3dvcmR8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "pdf-encrypt",
    link: "https://images.unsplash.com/photo-1477039181047-efb4357d01bd?ixid=MXwxMjA3fDB8MHxzZWFyY2h8M3x8ZW5jcnlwdHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "randomPasswordGenerator",
    link: "https://images.unsplash.com/photo-1504203700686-f21e703e5f1c?ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mnx8cGFzc3dvcmR8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "tictactoe",
    link: "https://images.unsplash.com/photo-1608111282283-df105d21a7ce?ixid=MXwxMjA3fDB8MHxzZWFyY2h8OHx8dGljJTIwdGFjfGVufDB8fDB8&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "weatherscrapper",
    link: "https://images.unsplash.com/photo-1486016006115-74a41448aea2?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxzZWFyY2h8Mnx8cmFpbnxlbnwwfHwwfA%3D%3D&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "whatsapp_automation",
    link: "https://images.unsplash.com/photo-1519069060891-f8c50519bf39?ixid=MXwxMjA3fDB8MHxzZWFyY2h8M3x8d2hhdHNhcHB8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
  {
    name: "youtube_video_downloader",
    link: "https://images.unsplash.com/photo-1541877944-ac82a091518a?ixid=MXwxMjA3fDB8MHxzZWFyY2h8M3x8eW91dHViZXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"
  },
]

const default_image = {
  name: "default",
  link: "assets/img/services.jpg"
}

// assets/img/services.jpg - default image, dont lose it

function fetchDataAndroid() {
  fetch('https://api.github.com/repos/Tejas1510/Hacking-Scripts/contents/Android Studio Scripts').then(response => {
    return response.json();
  })
    .then(data => {
      const html = data.map(script => {

        //find the image that correspond with the script
        let image_url = image_urls.find(image => image.name === script.name);
        if (!image_url) {
          //if there is no image assigned for the script, set a default image
          image_url = default_image
        }

        return `
        <div class="col-md-6 d-flex align-items-stretch" data-aos="fade-up">
        <div class="card">
          <div class="card-img">
            <img src="${image_url.link}" alt="...">
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
        //find the image that correspond with the script
        let image_url = image_urls.find(image => image.name === script.name);
        if (!image_url) {
          //if there is no image assigned for the script, set a default image
          image_url = default_image
        }


        return `
          <div class="col-md-6 d-flex align-items-stretch" data-aos="fade-up">
          <div class="card">
            <div class="card-img">
              <img src="${image_url.link}" alt="...">
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

        //find the image that correspond with the script
        let image_url = image_urls.find(image => image.name === script.name);
        if (!image_url) {
          //if there is no image assigned for the script, set a default image
          image_url = default_image
        }

        if (script.name != "bin" && script.name != ".classpath" && script.name != ".project") {
          return `
        <div class="col-md-6 d-flex align-items-stretch" data-aos="fade-up">
        <div class="card">
        <div class="card-img">
        <img src="${image_url.link}" alt="...">
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

        //find the image that correspond with the script
        let image_url = image_urls.find(image => image.name === script.name);
        if (!image_url) {
          //if there is no image assigned for the script, set a default image
          image_url = default_image
        }


        // console.log(script);
        return `
        <div class="col-md-6 d-flex align-items-stretch" data-aos="fade-up">
        <div class="card">
          <div class="card-img">
            <img src="${image_url.link}" alt="...">
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

        //find the image that correspond with the script
        let image_url = image_urls.find(image => image.name === script.name);
        if (!image_url) {
          //if there is no image assigned for the script, set a default image
          image_url = default_image
        }

        return `
        <div class="col-md-6 d-flex align-items-stretch" data-aos="fade-up">
        <div class="card">
          <div class="card-img">
            <img src="${image_url.link}" alt="...">
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

        //find the image that correspond with the script
        let image_url = image_urls.find(image => image.name === script.name);
        if (!image_url) {
          //if there is no image assigned for the script, set a default image
          image_url = default_image
        }

        return `
          <div class="col-md-6 d-flex align-items-stretch" data-aos="fade-up">
          <div class="card">
            <div class="card-img">
              <img src="${image_url.link}" alt="...">
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