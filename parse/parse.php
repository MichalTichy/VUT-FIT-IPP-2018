<?php
require_once("./CodeParser.php");

function LoadInput(){
    $stdin = fopen('php://stdin', 'r');
    $firstLine=strtolower(fgets($stdin));
    if(trim($firstLine)!=".ippcode18")
        throw new SyntaxException("Missing language definition (.IPPcode18).");

    while ($line = fgets($stdin)) {

        $line=trim(RemoveComment($line));
        $line=preg_replace('![\s\t]+!', ' ', $line);
        if (strlen($line)==0)
            continue;

        yield $line;
    }
}

$CountOfComments=0;
function RemoveComment($input){
    if (strpos($input, "#")!==false)
    {
        return substr($input, 0, strpos($input, "#"));
    }
    else
    {
        $GLOBALS['CountOfComments']++;
        return $input;
    }
}

function PrintHelpIfRequested($argc,array $argv){
    if (in_array("--help",$argv))
    {
        if ($argc!=2)
        	throw new InvalidArgumentException();

        fwrite(STDOUT, "Loads IPPcode18 from STDIN, performs lexical and syntatical checks and if valid than outputs XML representation of given input.");
    	exit();
    }
}

function PrintStatsIfRequested($argc,array $argv,$countOfComments,$countOfInstructions){
    if (count(preg_grep("/^--stats=.*$/",$argv)) !== 0 && (in_array("--loc",$argv) || in_array("--comments",$argv)))
        throw new InvalidArgumentException();

    if (count(preg_grep("/^--stats=.*$/",$argv))===0)
        return;

    $statsArg=array_pop(preg_grep("/^--stats=.*$/",$argv));
    $file = fopen(substr($statsArg, strpos($statsArg, "=")+1), "w") or die(12);
    $newLineNeeded=false;
    for ($i = 0; $i < $argc; $i++)
    {
        if ($argv[$i]=="--loc")
        {
            if ($newLineNeeded)
            {
                fwrite($file, PHP_EOL);
                $newLineNeeded=false;
            }

            $newLineNeeded=true;
            fwrite($file, $countOfInstructions);
        }
        if ($argv[$i]=="--comments")
        {
            if ($newLineNeeded)
            {
                fwrite($file, PHP_EOL);
                $newLineNeeded=false;
            }

            $newLineNeeded=true;
            fwrite($file, $countOfComments);
        }

    }
    fclose($file);
}

try
{
    PrintHelpIfRequested($argc,$argv);
    $parser=new CodeParser();

    $program=$parser->Parse(LoadInput());

    PrintStatsIfRequested($argc,$argv,$GLOBALS['CountOfComments'],0);

    $xml = $program->ConvertToXml();
    fwrite(STDOUT, $xml->saveXML());
}
catch (InvalidArgumentException $exception)
{
    exit(10);
}
catch (InvalidArgumentException $exception)
{
    exit(10);
}
catch (SyntaxException $exception)
{
    exit(1);
}
catch (LexicalException $exception)
{
    exit(1);
}
catch (Exception $exception)
{
	exit(99);
}

?>