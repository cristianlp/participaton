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


