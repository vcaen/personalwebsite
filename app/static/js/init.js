(function ($) {
    $(function () {

        $('.button-collapse').sideNav();
        $('.parallax').parallax();

        $('.scrollTo').click(function () { // Au clic sur un élément
            console.log('click')
            var page = $('.education').first() // Page cible
            var speed = 750; // Durée de l'animation (en ms)
            $('html, body').animate({scrollTop: $(page).offset().top}, speed); // Go
            return false;
        });

    }); // end of document ready
})(jQuery) // end of jQuery name space