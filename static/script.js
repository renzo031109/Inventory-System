
$(document).ready(function () {
    

   // To close the message alert
   $("#btn-alert-message").on("click", function(){
      $("#div-alert-message").hide()
    })


    const dat = document.getElementById('#select-item')

    $('#select-item').change(function() {

      $(this).css('cursor','pointer').attr('title', 'This is a hover text.');

      // $.ajax({
      //    url: '{% url 'add_item' %}',
      //    type: 'GET',
      //    data: {}
      // })
   });



//     $.ajax({
//     url: '/ajax/add_recipe_to_stash/',
//     type: 'GET',
//     data: {
//        # this goes to a django view that, in essence, returns a new 'stash_tooltip' var and 'stash_plus_or_minus' var
//       'stash_plus_or_minus': stash_plus_or_minus,
//     },
//     dataType: 'json',
//     success: function (data) {
//         document.getElementById("stash_recipe_btn").innerHTML = data.stash_plus_or_minus;
//         $("#stash_recipe_tooltip").attr('data-tooltip', data.stash_tooltip);  
//     }
//   });
});
