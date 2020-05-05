$(function(){
    $('#send_number').click(function(event) {

        event.preventDefault();

        let answer = $("#answer").val();
        $.ajax({
            type: 'POST',
            data: {'answer': answer ,
                    'csrfmiddlewaretoken': getCookie('csrftoken')
                   },

            success: function()
            {
                $( "#answer_state" ).append('<div class="alert alert-success" role="alert">Thanks </div>');
            },
            error: function() {
                $( "#answer_state" )
                .append('<div class="alert alert-danger" role="alert">Error</div>');
            },
            url: './check_answer',
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