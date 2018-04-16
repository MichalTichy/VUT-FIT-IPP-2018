<?php

require_once("./TestClass.php");
require_once("./SingleDirectoryFileSearch.php");
require_once("./RecursiveFileSearch.php");

$parser = "parse.php";
$interpreter = "interpret.py";

class HtmlGenerator{

    public static function BuildOkTestBoxHtml($name)
    {
        return "<div class=\"box ok\"><h1>$name</h1></div>";
    }

    public static function BuildErrTestBoxHtml($name, $returned, $expected)
    {
        return "<div class=\"box err\"><h1>$name</h1>Expected ERR code:  $expected <br> Returned ERR code: $returned</div>";
    }

    public static function BuildOutputDiffBoxHtml($name, $message)
    {
        $message = implode("|",$message);
        return "<div class=\"box err\"><h1>$name</h1> $message</div>";
    }
    public static function GenerateHead()
    {
        return "<html><head><meta charset=\"UTF-8\"><style>
        .box {border: 3px solid black;margin: 10px;}
        .ok {background-color:green;}
        .err {background-color:red;}
        </style><title>Tests</title></head>";
    }
    public static function BuildResult($countOfOK,$totalCount,$detailsHTML)
    {
        $headHtml=HtmlGenerator::GenerateHead();
        return "<!DOCTYPE html><html>
        $headHtml
        <body><h1> IPP project test results </h1>
        <h2> OK: $countOfOK FAIL: $totalCount</h2>
        $detailsHTML
        </body>
        </html>";
    }
}
function printHelp(){
    printf ("Test suite for IPP interpreter.\n");
    printf ("argumentsL\n");
    printf ("directory <PATH>\n");
    printf ("parse-script <PATH>\n");
    printf ("int-script <PATH>\n");
    printf ("recursive");
}

$options = getopt("", array("directory::","parse-script::","int-script::","recursive","help"));

if (array_key_exists("help", $options))
{
    printHelp();
    exit (0);
}

if (array_key_exists("directory", $options))
    $path = $options["directory"];
else
    $path = getcwd();

if (array_key_exists("parse-script", $options))
    $parser = $options["parse-script"];

if (array_key_exists("int-script", $options))
    $interpreter = $options["int-script"];

if (array_key_exists("recursive", $options) )
    $searcher= new RecursiveFileSearch();
else
    $searcher= new SingleDirectoryFileSearch();

$successHTML;
$failHTML;

$ok=0;
$fail=0;
foreach ($searcher->FindFiles($path) as $file)
{
    $test=new Test();
	$result = $test->PerformTest($file,$parser,$interpreter);
    if ($result)
    {
        $successHTML.=$test->outputHtml;
        $ok++;
    }
    else
    {
        $failHTML.=$test->outputHtml;
        $fail++;
    }


}

fwrite(STDOUT,HtmlGenerator::BuildResult($ok,$fail,$failHTML.$successHTML));

exit(0);
?>