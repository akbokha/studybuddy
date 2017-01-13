$(function() {

    //accordion menu courses
    if ( $(".actableheight").length ) {

        $("h4").click( function() {
            $(this).parent().toggleClass('active');
        });

    }

    //login menu
    $("#loginlink").click( function(e) {
        //disable link click
        e.preventDefault();
        //show menu
        $("#regmenu").removeClass("active");
        $("#loginmenu").toggleClass("active");
    });

    //register menu
    $("#reglink").click( function(e) {
        //disable link click
        e.preventDefault();
        //show menu
        $("#loginmenu").removeClass("active");
        $("#regmenu").toggleClass("active");
    });



      $("#majorjs").change(function(){
        $.getJSON("/items/",{id: $(this).val(), view: 'json'}, function(j) {
          var options = '<option value="">--------&nbsp;</option>';
          for (var i = 0; i < j.length; i++) {
            options += '<option value="' + j[i].optionValue + '">' + j[i].optionDisplay + '</option>';
          }
          $("#coursejs").html(options);
          $("#coursejs option:first").attr('selected', 'selected');
        })
        $("#coursejs").attr('selected', 'selected');
      })

});
