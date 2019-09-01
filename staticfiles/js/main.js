$(document).ready(function () {

    var menuClicked = false;

    $(".menu").click(function () {
        $(".nav-links").css({
            'width': '100%',
            'padding': '0px 20px',
            'position': 'absolute',
            'top': '60px',
            'left': '0px',
            'background-color': 'white',
            'height': '130px'
        });

        if (menuClicked) {
            $(".nav-links").slideUp('slow');
            menuClicked = false;
        } else {
            $(".nav-links").slideDown('slow');
            menuClicked = true;
        }

    });

    var activeGLink = $(".link").first();

    $.each($(".link"), function (index, element) {
        $(element).click(function () {
            activeGLink.removeClass('active-link');
            activeGLink = $(this);
            activeGLink.addClass('active-link');
        });
    });

    var activeSLink = $(".link").first();

    if ($(window).width() <= 576) {
        activeSLink.addClass('slink-active');
        $.each($(".link"), function (index, element) {
            $(element).click(function () {
                activeSLink.removeClass('slink-active');
                activeSLink = $(this);
                activeSLink.addClass('slink-active');
                $(".nav-links").slideUp('slow');
                menuClicked = false;
            });
        });
    };

    var activeMealLink = $(".meal-links a").first();

    $.each($(".meal-links a"), function (index, element) {
        $(element).click(function (e) {
            e.preventDefault();
            activeMealLink.removeClass('active-meal');
            activeMealLink = $(this);
            activeMealLink.addClass("active-meal");

            $.ajax({
                url: '/get-meals/',
                data: {
                    type: $(element).data('type')
                },
                dataType: 'json',
                success: function (data) {
                    $(".s_meals").html(data.meal_html);
                }
            });
        });
    });

    $.each($(".r_field"), function (index, element) {
        $(element).focus(function () {
            $(this).css({
                'background-color': 'transparent',
                'color': 'white',
                'box-shadow': 'none',
                'border-bottom': '1px solid orange',
            });
        });

        $(element).blur(function () {
            $(this).css({
                'background-color': 'transparent',
                'border': 'none',
                'border-bottom': '1px solid #fff',
            });
        });
    });
});