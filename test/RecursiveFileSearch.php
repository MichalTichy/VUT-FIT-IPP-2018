<?php
require_once("./FileSearchBase.php");

class RecursiveFileSearch extends FileSearchBase{
    public function FindFiles($dir){
        
        $iterator = new RecursiveDirectoryIterator("$dir");
        foreach(new RecursiveIteratorIterator($iterator) as $filename)
        {
            if (strcmp(".src", strstr($filename, '.', false)) != 0)
                continue;


            yield new File($filename);
        }
    }
}

?>