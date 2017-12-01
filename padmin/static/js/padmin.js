$('.convocatoria_desafios_tab item').tab();
$('.ui.checkbox').checkbox();


$('#desafio_guardar').on('click', function() {

      $('#form-desafio-new').submit()

});

function modal_desafio_new() {

$('#modal_desafio_new')
  .modal({
    inverted: true
  }).modal('show');

}


function desafio_view(element) {

    alert(element['id']);

   /* $.ajax({
        type: 'GET',
        url: '/desafio/view/' + element.id,
        data: {
        },

        success: function (data, textStatus) {
          alert(data)

        },
        error: function(xhr, status, e) {
            alert(status, e);
        }

    });*/

}


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
                '<div class="item">'+
                  '<div class="content">'+
                    '<a title="Ver detalles Desafío" href="/desafio/view/' + desafio.id + '" class="header">'+ desafio['titulo'] +'</a>'+
                    '<div class="meta">'+
                      '<span class="cinema">'+
                      '<a href="#" title="Ver participantes">5 participantes</a>'+
                      '</span>'+
                    '</div>'+
                    '<div class="description">'+
                      '<p>'+ desafio['descripcion'] +'</p>'+
                    '</div>'+
                    '<div class="extra">'+
                      '<div class="ui label">Tematica 1</div>'+
                      '<div class="ui label"><i class="globe icon"></i> Tematica 2</div>'+
                      '<div class="ui right floated primary button">'+
                            'Ver D.'+
                            '<i class="right eye icon"></i>'+
                      '</div>'+

                    '</div>'+
                  '</div>'+
                '</div>'
            ).appendTo('#desafios');
           
           }); 

        },
        error: function(xhr, status, e) {
            alert(status, e);
        }
    });


}

function desafio_new(element) {

    var cid =  $(element).attr("convocatoria_id")  //$("#convocatoria_id").val();
    var titulo = $("#titulo").val();
    var descripcion = $("#descripcion").val();

    $.ajax({
        type: 'POST',
        url: $(element).attr("data-url"),
        data: {
          'csrfmiddlewaretoken' : $(element).siblings("input[name='csrfmiddlewaretoken']" ).val(),
          'convocatoria_id': cid, 
          'titulo': titulo,
          'descripcion': descripcion
        },

        success: function (data, textStatus) {

            var desafio_nuevo = data['results'][0];

            $(
                '<div class="item">'+
                  '<div class="content">'+
                    '<a class="header">'+ desafio_nuevo['titulo'] +'</a>'+
                    '<div class="meta">'+
                      '<span class="cinema">'+'5 participantes'+'</span>'+
                    '</div>'+
                    '<div class="description">'+
                      '<p>'+ desafio_nuevo['descripcion'] +'</p>'+
                    '</div>'+
                    '<div class="extra">'+
                      '<div class="ui label">Tematica 1</div>'+
                      '<div class="ui label"><i class="globe icon"></i> Tematica 2</div>'+
                      '<div class="ui right floated primary button">'+
                            'Documentos Asociados'+
                            '<i class="right chevron icon"></i>'+
                      '</div>'+
                    '</div>'+
                  '</div>'+
                '</div>').appendTo('#desafios');
              
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




$(document).ready(function(){
  var cid = $("#convocatoria_id").val();
  get_desafios(cid);
});


