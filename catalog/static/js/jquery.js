$(document).ready(function() {

  $("label").click(function() {
    $(this).css({
      "background-color": "#1e8eff",
      "color": "white"
    });
  });

  $("#hitlistButton").click(function() {
    $(this).css({
      "background-color": "#f2f2f2",
      "color": "#1e8eff"
    });
    $("#wishlistButton").css({
      "background-color": "#b7b5b5",
      "color": "#f2f2f2"
    });
    $("#hitlistResults").css("z-index", "100");
    $("#wishlistResults").css("z-index", "1");
  });

  $("#wishlistButton").click(function() {
    $(this).css({
      "background-color": "#f2f2f2",
      "color": "#1e8eff"
    });
    $("#hitlistButton").css({
      "background-color": "#b7b5b5",
      "color": "#f2f2f2"
    });
    $("#wishlistResults").css("z-index", "100");
    $("#hitlistResults").css("z-index", "1");
  });

  $("#hitlistButtonUser").click(function() {
    $(this).css({
      "background-color": "#f2f2f2",
      "color": "#1e8eff"
    });
    $("#wishlistButtonUser").css({
      "background-color": "#b7b5b5",
      "color": "#f2f2f2"
    });
    $("#hitlistResultsUser").css("z-index", "100");
    $("#wishlistResultsUser").css("z-index", "1");
  });

  $("#wishlistButtonUser").click(function() {
    $(this).css({
      "background-color": "#f2f2f2",
      "color": "#1e8eff"
    });
    $("#hitlistButtonUser").css({
      "background-color": "#b7b5b5",
      "color": "#f2f2f2"
    });
    $("#wishlistResultsUser").css("z-index", "100");
    $("#hitlistResultsUser").css("z-index", "1");
  });




});
