


$(document).ready(function () {
    

// To close the message alert
$("#btn-alert-message").on("click", function(){
   $("#div-alert-message").hide()
   });

// default slide on filter option
$("#filter-slide").hide();
  

// Toggle on filter option
$("#filterBtn").click(function(){
   
   $(this).toggleClass('btn-success');

   $("#filter-slide").slideToggle("slow");
   
   });

});


