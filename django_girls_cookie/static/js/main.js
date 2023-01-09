var post_to_btn = ""; /*because delete button is replicated and only that has the id. 
So to get every button's id on click, a global variable has to be there.*/

$("#myBtn").on("click", function (event) {
  post_to_btn = $(this).attr("post_id");
  $("#myModal").modal("toggle");
});

$("#yes_delete_button").on("click", function (event) {
  postDelete();
});

function postDelete() {
  $.ajax({
    url: "delete/" + post_to_btn + "/",
    type: "POST",
    data: $(".post-form").serialize(),
    success: function (json) {
      console.log("success");
      var meriDiv = document.getElementById(post_to_btn);
      meriDiv.parentNode.removeChild(meriDiv);
    },
    error: function (xhr, errmsg, err) {
      console.log(xhr);
      console.log(errmsg);
      console.log(err);
    
    },
  });
}
function open_modal(){
  $("#myModal").modal("show");

}
function hide_modal(){
  $("#myModal").modal("hide");

}
$("#edit").on("click", function (event) {
  open_modal();
});
$("#yes_button").on("click", function (event) {
  var text_to_update = $("#id_text");
  var title_to_update = $("#id_title");
  //Check fields empty or not, if empty, disable the submit button.
 
  if (text_to_update.val().length > 0 && title_to_update.val().length > 0) {
    console.log('All Ok')
    postUpdate(text_to_update.val(), title_to_update.val());
    $(".error-msg").text("");

    hide_modal();    
  } else {
    //Prevent the modal from closing
      console.log("Empty field");
    
      // $("#myModal").on("hide.bs.modal", function (e) {
      //   e.preventDefault();
      // });
      $(".error-msg").text("Fields cannot be empty");

    
  }
});
function postUpdate(text_to_update, title_to_update) {
  console.log($("#yes_button").data("idpost"));
  var post = $("#yes_button").data("idpost");
  $.ajax({
    headers: { "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val() },
    url: "/update/" + post + "/",
    type: "POST",
    data: $(".post-form").serialize(),
    success: function (json) {
      console.log("success");
      $(".title_here").text(title_to_update);
      $(".text_here").text(text_to_update);

    },
    error: function (xhr, errmsg, err) {

      //Display the error, critical ones, in console
      console.log(xhr);
      console.log(errmsg);
      console.log(err);

    },
  });
}
