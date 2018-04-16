<?php
require_once("./FileSearchBase.php");

class SingleDirectoryFileSearch extends FileSearchBase{
    function FindFiles($dir){
        foreach (glob("$dir/*.src") as $filename)
        {
            yield new File($filename);
        }
    }
}

?>