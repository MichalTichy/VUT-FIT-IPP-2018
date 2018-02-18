<?php

function LoadInput(){
    $stdin = fopen('php://stdin', 'r');

    while ($line = fgets($stdin)) {
        yield trim($line);
    }
}

function SaveXml($xml){
    
}

$parser=new CodeParser();
$program=$parser->Parse(LoadInput());
$xml = $program->ConvertToXml();
SaveXml($xml);

?>