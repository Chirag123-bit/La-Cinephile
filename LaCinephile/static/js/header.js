$(function () {
    // Function to attach a scrollbar to top after scrolling down a certain amount
    $(window).on('scroll', function () {
        if ($(window).scrollTop() > 20) {
            $('.navbar').addClass('active'); //Add active class to navbar
        } else {
            $('.navbar').removeClass('active'); // Remove active class from navbar
        }
    });
});