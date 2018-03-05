<?php
require_once("CodeParser.php");

function LoadInput(){
    $stdin = fopen('php://stdin', 'r');
    $firstLine=strtolower(fgets($stdin));
    if(trim($firstLine)!=".ippcode18")
        throw new SyntaxException("Missing language definition (.IPPcode18).");

    $end=false;
    while (($line = fgets($stdin)) && !$end) {

        $line=trim(RemoveComment($line));
        $line=preg_replace('!\s+!', ' ', $line);
        if (strlen($line)==0)
            continue;

        yield $line;
    }
}

function RemoveComment($input){
    return strpos($input, "#")!==false ? substr($input, 0, strpos($input, "#")) : $input;
}

$parser=new CodeParser();
$program=$parser->Parse(LoadInput());
$xml = $program->ConvertToXml();
$s= $xml->saveXML();
fwrite(STDOUT, $xml->saveXML());
?>