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
    if(hours >= 22  || hours <= 6){
        toggle_night();
    }

    /**
     * Twitter
     */
    var twitterUser = "OberthMedia";
    var twitterUrl = "http://search.twitter.com/" + twitterUser + ".json&callback=?&count=1" ;
    
    $.getJSON(twitterUrl, function(json){
        $("#twitter").html(json.followers_count);
    });
    $("#twitter").click(function(){
        toggle_night();
    });
    $("#twitter").hover(
        function(){
            if(!$('#twitter .social').is(':animated') && !$('#twitter .descr').is(':animated')){
                $('#twitter .descr').fadeOut(function(){
                    $('#twitter .social').fadeIn();
                });
            }
        }, 
        function(){
            if(!$('#twitter .social').is(':animated') && !$('#twitter .descr').is(':animated')){
                $('#twitter .social').fadeOut(function(){
                    $('#twitter .descr').fadeIn();
                });
            }
        }
    );

    /**
     * References effects
     */
    $(".reference").hover(
        function(){
            var self = this;
            if(!$(this).children('.reference_image').is(':animated') && 
               !$(this).children('.reference_details').is(':animated')){
                $(this).children('.reference_image').slideUp();
                $(self).children('.reference_details').slideDown();
            }
        }, 
        function(){
            var self = this;
            if(!$(this).children('.reference_image').is(':animated') && 
               !$(this).children('.reference_details').is(':animated')){
                $(this).children('.reference_image').slideDown();
                $(self).children('.reference_details').slideUp();
            }
        }
    );

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
    })

});

function toggle_night(){
    $('#site').toggleClass('night');
    $('#content p').toggleClass('night');
    $('#content h1').toggleClass('night');
    $('#main').toggleClass('night');
    $('footer').toggleClass('night');
}