var homepage = homepage || {};

$(document).ready(function(){
    // get javascript settings which need to be passed from the server
    // for instance urls, users etc
    var settingsUrl = $('html').data('settingsurl');
    $.getJSON(settingsUrl, function(settings){
        // settings are in the settings object
        
    });

    /**
     * Switch to night mode when between 22:00 and 6:00 o clock
     */
    var hours = new Date().getHours();
    if(hours >= 20  || hours <= 7){
        toggle_night();
    }


    // TODO: Delete in production
    $("#day_night_toggle").click(function(){
        toggle_night();
    });


    /**
     * Slide down telephone on input
     */
    $("#contact_form #id_phone").keyup(function(){
        if($(this).val() !== ""){
            $("#id_phonetime").parent().parent().slideDown();
        } else {
            $("#id_phonetime").parent().parent().slideUp();
        }
    });

    $("#contact_form .required :input").keyup(function(){
        if($(this).val() !== ""){
            $(this).parent().removeClass("requiredbg");
        } else {
            $(this).parent().addClass("requiredbg");
        }
    });

    $(".reference").each(function(){
        if($(this).children().length !== 0){
            var self = this;
            $(this).addClass('clickable');
            $(this).click(function(){
                var $link = $(self).find('.reference_description a');
                window.location.href = $link.attr('href');
            });
        }
    });


});

function toggle_night(){
    $('#site').toggleClass('night');
    $('#content p').toggleClass('night');
    $('#content h1').toggleClass('night');
    $('#main').toggleClass('night');
    $('footer').toggleClass('night');
    if($('#site').hasClass('night')){
        $('.foss img').each(function(){
            var src = this.src;
            src = src.replace('day', 'night');
            this.src = src;
        });
    } else {
        $('.foss img').each(function(){
            var src = this.src;
            src = src.replace('night', 'day');
            this.src = src;
        });
    }
}
