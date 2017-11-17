$('.desafios_tab desafios').tab();
$('.ui.checkbox').checkbox();

function get_desafios(cid) {

    $.ajax({
        type: 'GET',
        url: '/desafio/all/' + cid,
        data: {
        },

        success: function (data, textStatus) {
            $('#desafios').empty();
            var desafios = data['results'];

            $.each(desafios, function (indice,desafio) {
            // template
            $(
                '<div class="item">' +
                  '<i class="large github middle aligned icon"></i>' +
                  '<div class="content">' +
                      '<a class="header">'+ desafio['titulo'] +'</a>' +
                      '<div class="description">'+desafio['descripcion']+'</div>' +

/*                      '<div class="extra">' +
                        '<div class="ui right floated button">'+
                          'Ver'+
                        '</div>'+
                      '</div>' + 
*/
                  '</div>' +
                '</div>'
            ).appendTo('#desafios');
           
           }); 

        },
        error: function(xhr, status, e) {
            alert(status, e);
        }
    });


}

function desafio_new() {

    var cid = $("#convocatoria_id").val();
    var titulo = $("#titulo").val();
    var descripcion = $("#descripcion").val();

    $.ajax({
        type: 'POST',
        url: '/desafio/new',
        data: {
          'convocatoria_id': cid, 
          'titulo': titulo,
          'descripcion': descripcion
        },

        success: function (data, textStatus) {
            var desafio_nuevo = data['results'][0];
            $(
                '<div class="item">' +
                  '<i class="large github middle aligned icon"></i>' +
                  '<div class="content">' +
                      '<a class="header">'+ desafio_nuevo['titulo'] +'</a>' +
                      '<div class="description">'+desafio_nuevo['descripcion']+'</div>' +

/*                      '<div class="extra">' +
                        '<div class="ui right floated button">'+
                          'Ver'+
                        '</div>'+
                      '</div>' + 
*/
                  '</div>' +
                '</div>'
            ).appendTo('#desafios');

       },
        error: function(xhr, status, e) {
            alert(status, e);
        }
    });

}


function convocatoria_desafios(id) {

   $.ajax({
        url: '/padmin/convocatoria/desafios/' + id,
        method: 'POST',
        data: {
              },
        dataType: 'json',
        success: function (data) {
            alert(data);
        }
     });


}



function modal_desafio_new() {

$('.ui.modal')
  .modal({
    inverted: true
  }).modal('show');

}

/*$(function(){
	
	// tabbed menus
	
	$('.menu .item').tab();
	
  $.getJSON('getDesafios',function (desafios) {
    $.each(desafios.data,function (desafio,src) {
		 // template
      $(
      '<div class="column">' +
        '<div class="ui centered fluid card">' +
          '<div class="image">' +
            '<img src="' + this.images.standard_resolution.url + '" />' +
              '</div>' +
                '<div class="content">' +
                  '<a class="header">' + this.user.full_name + '</a>' +
                    '<div class="meta">' +
                      '<span class="date">' + this.filter + ' Filter' +'</span>' +
                      '</div>' +
                      '<div class="description">' + this.user.username +
                      '</div>' +
                  '</div>'+
                    '<div class="extra content">' +
                    '<span class="right floated">' + '<i class="heart outline icon">'+ '</i>' + this.likes.count +' likes'+'</span>' +
							'<span class="left floated">' + '<i class="comments outline icon">'+ '</i>' + this.comments.count +' comments'+'</span>' +
                    '</div>' +
                  '</div>'+
                '</div>'
      ).appendTo('#desafios');
    }); 
  });
	
// script to for search
var accessToken = ''; // use your own token	
	
$('.ui.search')
  .search({
    type          : 'category',
    minCharacters : 3,
    apiSettings   : {
      onResponse: function(githubResponse) {
        var
          response = {
            results : {}
          }
        ;
        // translate GitHub API response to work with search
        $.each(githubResponse.items, function(index, item) {
          var
            language   = item.language || 'Unknown',
            maxResults = 8
          ;
          if(index >= maxResults) {
            return false;
          }
          // create new language category
          if(response.results[language] === undefined) {
            response.results[language] = {
              name    : language,
              results : []
            };
          }
          // add result to category
          response.results[language].results.push({
            title       : item.name,
            description : item.description,
            url         : item.html_url
          });
        });
        return response;
      },
      url: '//api.github.com/search/repositories?q={query}'
    }
  })
;

});
*/



$(document).ready(function(){
  var cid = $("#convocatoria_id").val();
  get_desafios(cid);
});

//csrf token para pedidos ajax ***********************************************************************
$(function() {


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});