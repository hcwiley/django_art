function bindEnlarge(){
  $(".enlarge").on('click tap', function(){
    var modal = $("#enlarged");
    modal.find(".name").text($(this).data("name"));
    modal.find(".img").css("background-image","url('"+$(this).data("full")+"')");
    //var info = $(this).parents('.row').find('.info').html();
    //modal.find('.info').html(info);
    modal.modal("toggle", {keyboard: true});
  });
}

$(window).ready(function(){
  bindEnlarge();
});
