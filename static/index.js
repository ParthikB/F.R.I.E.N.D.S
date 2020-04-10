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
  console.log(filename)
});




//// A function that would return the contents of the JSON file located
//// in the same dir as this script

// function find_file(){
//   const { readdirSync } = require('fs');
//   const PATH_TO_YOUR_FOLDER = '.';
  
//   var file_found = false
//   while (file_found==false) {  

//     dir_files = readdirSync(PATH_TO_YOUR_FOLDER)

//     for (var i=0; i<dir_files.length; i++) {
//       fname = dir_files[i]
//       if (fname=='info.json') {
//         var file_found = true
//         console.log('File Found')
//         return require('./info');
//       }
//     console.log('File not found. Recursing...')
//       }
//   }
// }


////// data is the contents of the JSON file, which can be splitted as follows
//// var data = find_file()

//// var class_name = data['class'] 
//// var prob_dist  = data['prob']

//// console.log(class_name)
//// console.log(prob_dist)
