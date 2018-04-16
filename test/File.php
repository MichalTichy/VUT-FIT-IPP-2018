<?php

class File
{
    var $name;
    function __construct($filename)
    {
        $this->name = strstr($filename, ".src", true);


        if (!file_exists("$this->name.in"))
        {
            $file = fopen("$this->name.in", 'w+');
            fclose($file);
        }

        if (!file_exists("$this->name.out"))
        {
            $file = fopen("$this->name.out", 'w+');
            fclose($file);
        }

        if (!file_exists("$this->name.rc"))
        {
            $file = fopen("$this->name.rc", 'w+');
            fwrite($file, "0");
            fclose($file);
        }
    }
}

?>