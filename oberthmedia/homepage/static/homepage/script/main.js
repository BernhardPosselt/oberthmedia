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

    /**
     * Twitter
     */
    var user = 'OberthMedia';
      
    // using jquery built in get json method with twitter api, return only one result
    $.getJSON('http://twitter.com/statuses/user_timeline.json?screen_name=' + user + '&count=1&callback=?', function(data)      {
          
        // result returned
        var tweet = data[0].text;
      
        // process links and reply
        tweet = tweet.replace(/(\b(https?|ftp|file):\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|])/ig, function(url) {
            return '<a href="'+url+'">'+url+'</a>';
        }).replace(/B@([_a-z0-9]+)/ig, function(reply) {
            return  reply.charAt(0)+'<a href="http://twitter.com/'+reply.substring(1)+'">'+reply.substring(1)+'</a>';
        });
      
        // output the result
        $("#twitter .descr").html(tweet);
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