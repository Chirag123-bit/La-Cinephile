$(".slider").slick({
  slidesToShow: 3,
  slidesToScroll: 1,
  arrows: true,
  dots: false,
  centerMode: true,
  variableWidth: true,
  infinite: true,
  focusOnSelect: true,
  cssEase: "linear",
  touchMove: true,
  prevArrow: '<button class="slick-prev"> < </button>',
  nextArrow: '<button class="slick-next"> > </button>',
});

var imgs = $(".slider img");
imgs.each(function () {
  var item = $(this).closest(".item");
  item.css({
    "background-image": "url(" + $(this).attr("src") + ")",
    "background-position": "center",
    "-webkit-background-size": "cover",
    "background-size": "cover",
  });
  $(this).hide();
});

$(".slider").on('afterChange', function (event, slick, currentSlide, nextSlide) {
      $(".slick-slide").removeClass('act'); // Removes class "act" from overall slider
      $('.slick-current').addClass('act'); // Add class "act" to current slide
   });

$('.mcard').hover(function(){ // Toggle active class to active slider
  if($(this).hasClass("active")){ // Check wheter current element has active class
      $(this).find('.mbottom').slideUp(function(){ //If it does remove it as we are moving out of that element
      $('.mcard').removeClass("active");
    })
  }
  else{ //If it does not it add it as we are hovering on that element
    $(this).addClass("active");
    $(this).find('.mbottom').stop().slideDown()
  }
})

function getId(){ // change href attrinute of anchor tag to slider movie's url
	var id = $('.slick-current').attr('id'); // get current slide from slider
	var anchor = document.getElementById('upcomming-button'); // get element button from document
	anchor.href = "/now/" // Overwrite current href value
	anchor.href += id; // append id of movie to the overwritten href
}

function getId2(){ // change href attrinute of anchor tag to slider movie's url
	var id = $('.slick-current').attr('id');  // get current slide from slider
	var anchor = document.getElementById('upcomming-button'); // get element button from document
	anchor.href = "/up/" // Overwrite current href value
	anchor.href += id; // append id of movie to the overwritten href
}

