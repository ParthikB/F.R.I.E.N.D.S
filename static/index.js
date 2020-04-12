// To show the image //

function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    
    reader.onload = function(e) {
      $('#img').attr('src', e.target.result);
    }
    
    reader.readAsDataURL(input.files[0]); // convert to base64 string
  }
}

$("#fname").change(function() {
  readURL(this);
});


// To show the name of the image//

$('#fname').bind('change', function () {
  filename = $("#fname").val();
  if (/^\s*$/.test(filename)) {
    $(".file-upload").removeClass('active');
    $("#noFile").text("No file chosen..."); 
  }
  else {
    $(".file-upload").addClass('active');
    $("#noFile").text(filename); 
  }
  console.log(filename);
});


// function for ploting graph

function renderChart(data, labels) {
  var ctx = document.getElementById("myChart").getContext('2d');
  var myChart = new Chart(ctx, {
      type: 'bar',
      data: {
          labels: labels,
          datasets: [{
              label: 'This week',
              data: data,
          }]
      },
  });
  }

  function getChartData() {
  $("#loadingMessage").html('<img src="./giphy.gif" alt="" srcset="">');
  $.ajax({
      url: "https://ghibliapi.herokuapp.com/films",   // <-- graph is reading this json file
      success: function (result) {
          var data = result.map(x=>x.rt_score);
          var labels = result.map(x=>x.title);
          renderChart(data, labels);
          console.log(data);
      },
  });
}
  
// function: when button is clicked, function getCharData() will trigger
  $("#renderBtn").click(  
  function () {
      getChartData();
  });


  
