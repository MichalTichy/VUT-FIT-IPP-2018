<?php
require_once("CodeParser.php");

function LoadInput(){
    $stdin = fopen('php://stdin', 'r');

    while ($line = fgets($stdin)) {
        yield trim(RemoveComment($line));
    }
}

function RemoveComment($input){
    return strpos($input, "#")!==false ? substr($input, 0, strpos($input, "#")) : $input;
}

function SaveXml($xml){

}

$parser=new CodeParser();
$program=$parser->Parse(LoadInput());
$xml = $program->ConvertToXml();
SaveXml($xml);

?>