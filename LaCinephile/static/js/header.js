$(function () {
  $(window).on('scroll', function () {
      if ( $(window).scrollTop() > 20 ) {
          $('.navbar').addClass('active');
      } else {
          $('.navbar').removeClass('active');
      }
  });
});