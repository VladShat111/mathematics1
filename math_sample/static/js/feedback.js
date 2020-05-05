$(function(){
    $('#submit_feedback').click(function(event) {

        event.preventDefault();

        let feedbackUsername = $("#feed_username").val();
        let feedbackEmail = $("#feed_email").val();
        let feedbackText = $("#feed_text").val();

        $.ajax({
            type: 'POST',
            data: {'feedbackUsername': feedbackUsername,
                    'feedbackEmail': feedbackEmail,
                    'feedbackText': feedbackText,
                    'csrfmiddlewaretoken': getCookie('csrftoken')
                   },

            success: function()
            {

                $( "#FeedbackState" ).append('<div class="alert alert-success" style="background-color:#c6ffb3; color: black; " role="alert">Thanks for your feedback!</div>');
                $("#feed_username").val("");
            },
            error: function() {
                $( "#FeedbackState" )
                .append('<div class="alert alert-danger" style="background-color:#ff9999; color: black; " role="alert">For some reason we can not save your feedback!</div>');
            },
            url: './feedback/',
            cache: false
        });
        return false;
    });
}

);

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');