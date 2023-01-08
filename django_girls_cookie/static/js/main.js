var post_to_btn = ""; //because delete button is replicated and only that has the id.
// so to get every button's id on click, a global variable has to be there.
$("#myBtn").on("click", function (event) {
  post_to_btn = $(this).attr("post_id");
  //console.log(post_to_btn);
  $("#myModal").modal("toggle");
});

$("#yes_delete_button").on("click", function (event) {
  postDelete();
  //$("#myModal").modal("toggle");
});

function postDelete() {
  $.ajax({
    url: "delete/" + post_to_btn + "/",
    type: "POST",
    data: $(".post-form").serialize(),
    success: function (json) {
      //alert('Post Deleted!')
      //post_to_delete = ''
      //console.log(json);
      console.log("success");
      var meriDiv = document.getElementById(post_to_btn);
      //console.log(post_to_delete.type);
      meriDiv.parentNode.removeChild(meriDiv);
    },
    error: function (xhr, errmsg, err) {
      console.log(xhr);
      console.log(errmsg);
      console.log(err);
      // $("#results").html(
      //   "<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " +
      //     errmsg +
      //     " <a href='#' class='close'>&times;</a></div>"
      // ); // add the error to the dom
      // console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    },
  });
}

$("#edit").on("click", function (event) {
  //event.preventDefault();
  //postUpdate();
  $("#myModal").modal("toggle");
});
$("#yes_button").on("click", function (event) {
  //event.preventDefault();
  var text_to_update = $("#id_text");
  //console.log(text_to_update);
  var title_to_update = $("#id_title");
  //console.log(title_to_update);
  // var error_message = $("#error_display").val();

  //Check fields empty or not, if empty, disable the submit button.
  if (text_to_update.val().length > 0 && title_to_update.val().length > 0) {
    console.log('All Ok')
  } else {
    console.log("Empty field");
    // $(".invalid-feedback").html("<strong>Fields cannot be empty.</strong>");
    // $("#error_display").text("Fields cannot be empty");

    $(".title_label").before("<p >Fields cannot be empty</p>");

    $(this).prop("disabled", true);
    //postUpdate();
  }
  //$("#myModal").modal("toggle");
});
function postUpdate() {
  //console.log(post_to_update);
  console.log($("#yes_button").data("idpost"));
  //post_to_update = $(this).attr("post_id");

  var text_to_update = $("#id_text").val();
  console.log(text_to_update);
  var title_to_update = $("#id_title").val();
  console.log(title_to_update);
  var post = $("#yes_button").data("idpost");
  $.ajax({
    headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
    url: "/update/" + post + "/",
    type: "POST",
    data: $(".post-form").serialize(),
    success: function (json) {
      //console.log(json);
      console.log("success");
      $(".title_here").text(title_to_update);
      $(".text_here").text(text_to_update);
    },
    error: function (xhr, errmsg, err) {
      console.log(xhr);
      console.log(errmsg);
      console.log(err);

      // $("#results").html(
      //   "<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " +
      //     errmsg +
      //     " <a href='#' class='close'>&times;</a></div>"
      // );
      //console.log(xhr.status + ": " + xhr.responseText);
    },
  });
}

// function postUpdateCall(){
//     postUpdate()
// }
