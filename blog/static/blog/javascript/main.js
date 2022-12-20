var post_to_delete = ''
$(document).on("click", "#myBtn", function (event) {
    post_to_delete = $(this).attr("post_id");

  $("#myModal").modal('toggle');

});


function postDelete(){
    
    //var post_to_delete = $(this).attr("item_id");
    console.log(post_to_delete)
    $.ajax({
      url: "delete",
      type: "GET",
      data: {
        post_to_delete: post_to_delete,
      },
      success: function (json) {
        //post_to_delete = ''
        console.log(json);
        console.log("success");
        var meriDiv = document.getElementById(post_to_delete);
        console.log(post_to_delete.type)
        meriDiv.parentNode.removeChild(meriDiv);
        
      },
      error: function (xhr, errmsg, err) {
        $("#results").html(
          "<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " +
            errmsg +
            " <a href='#' class='close'>&times;</a></div>"
        ); // add the error to the dom
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      },
    });
}

function postDeleteCall(){
    postDelete();

}

$(document).on("click",'#edit', function(event){
    event.preventDefault();
    post_to_update = $(this).attr("post_id");
    $("#myModal").modal("toggle");
    
    
})

function postUpdate(){
    console.log(post_to_update);
    var text_to_update = $('#id_text').val()
    console.log(text_to_update)
    var title_to_update = $("#id_title").val();
    console.log(title_to_update);

    $.ajax({
      headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
      url: "../../update",
      type: "POST",
      data: {
        post_to_update: post_to_update,
        title:title_to_update,
        text:text_to_update,
      },
      success: function (json) {
        console.log(json);
        console.log("success");
        $('.title_here').text(title_to_update)
        $('.text_here').text(text_to_update)
        
      },
      error: function (xhr, errmsg, err) {
        $("#results").html(
          "<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " +
            errmsg +
            " <a href='#' class='close'>&times;</a></div>"
        );
        console.log(xhr.status + ": " + xhr.responseText);
      },
    });
}
function postUpdateCall(){
    postUpdate()
}
