(function ($) {
    $(function () {

        $('.button-collapse').sideNav();
        $('.parallax').parallax();

        $('.scrollTo').each(function (i, e) {
            $(e).find('a').click(function (event) { // Au clic sur un élément
                event.preventDefault();
                var page = $("." + $(this).attr('href')); // Page cible
                var speed = 750; // Durée de l'animation (en ms)
                $('html, body').animate({scrollTop: $(page).offset().top}, speed); // Go
                ;
            });
        });

    }); // end of document ready
})(jQuery) // end of jQuery name space