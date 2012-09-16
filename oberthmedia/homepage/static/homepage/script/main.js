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
            $(this).addClass('clickable');
            $(this).click(function(){
                var $link = $(this).find('.reference_description a');
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
}
