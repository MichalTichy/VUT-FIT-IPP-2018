<?php
require_once("CodeParser.php");

function LoadInput(){
    $stdin = fopen('php://stdin', 'r');
    $firstLine=strtolower(fgets($stdin));
    if($firstLine!=".ippcode18")
        throw new SyntaxException("Missing language definition (.IPPcode18).");

    while ($line = fgets($stdin)) {

        $line=trim(RemoveComment($line));
        if (strlen($line)==0)
            continue;

        yield $line;
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