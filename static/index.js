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


/// function for ploting graph
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
      url: "https://ghibliapi.herokuapp.com/films",
      success: function (result) {
          var data = result.map(x=>x.rt_score);
          var labels = result.map(x=>x.title);
          renderChart(data, labels);
          console.log(data);
      },
  });
}
  
  $("#renderBtn").click(
  function () {
      getChartData();
  });

// Code for reading the data and show it in console  

var mydata = JSON.parse(data);
console.log(mydata[0].class);
console.log(mydata[0].prob_distribution);

//  i want you to make this syntax of info.json
// data = '[{"class" : "Joey", "prob_distribution" : [17.19, 60.88, 11.06, 0.0, 0.79,10.08]}]';