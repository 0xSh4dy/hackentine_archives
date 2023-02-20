<form action="/" method="post">
    <input type="text" name="something" placeholder="Enter something">
    <input type="submit" value="Submit">
</form>

<?php
    $flag = fopen("flag.txt", "r");
    if($_POST["something"]){
        $something = $_POST["something"];
        if(md5($something)==0){
            echo fread($flag,filesize("flag.txt"));
        }
        else{
            echo "Try harder";
        }
    }
?>