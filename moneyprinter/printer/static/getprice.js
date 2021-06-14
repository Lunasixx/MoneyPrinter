$(document).ready(function(){

    var x = setInterval(function()
    {
        $.ajax({
            type:"GET",
            url: "{% url 'getprice/' %}",
            success: function(response){
                $("#price").empty();
                $("#price").text(response);

            },
            error: function(response){
                alert(response.text);
            }
        })
    },2000);

});