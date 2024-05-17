<?php
//check if a file was uploaded first so no warning will appear if "Upload" was pressed without no image selected
if (isset($_FILES['file'])) {
    //check if the upload was successful and the file is not empty
    if ($_FILES['file']['error'] === UPLOAD_ERR_OK && $_FILES['file']['size'] > 0) {
        //specify the directory where the uploaded file will be directed to (if copied, change it to your desired directory)
        $uploadDir = '/upload/';
        //create a unique name with the time in milliseconds and the type of file
        $filename = uniqid('image_') . '.' . pathinfo($_FILES['file']['name'], PATHINFO_EXTENSION);
        //move the uploaded file to the specified directory 
        if (move_uploaded_file($_FILES['file']['tmp_name'], $uploadDir . $filename)) {
            //execute the Python script with the uploaded file as an argument
            $output = shell_exec('python mainprog.py ' . escapeshellarg($uploadDir . $filename));
            //output the result of the Python program
            echo $output;
        } else {
            echo 'Error: Failed to move uploaded file.';
        }
    }
}
?>
