<?php
require_once("./File.php");


abstract class FileSearchBase{
    abstract function FindFiles($path);
}

?>