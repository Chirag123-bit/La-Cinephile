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

$('.mcard').hover(function(){
  if($(this).hasClass("active")){
      $(this).find('.mbottom').slideUp(function(){
      $('.mcard').removeClass("active");
    })
  }
  else{
    $(this).addClass("active");
    $(this).find('.mbottom').stop().slideDown()
  }
})

function getId(){
	console.log("a")
	var id = $('.slick-current').attr('id');
	console.log(id);
	var anchor = document.getElementById('upcomming-button');
	anchor.href = "/now/"
	anchor.href += id;
}


