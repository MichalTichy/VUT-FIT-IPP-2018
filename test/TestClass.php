<?php
require_once("./File.php");

class Test
{

    var $parserResult, $interpretResult, $expectedReturnCode,$outputHtml;

    public function PerformTest($file, $parseScript, $intScript){
        $xml = $this->Parse($file->name, $parseScript);

        if($this->parserResult == 0)
        {
            $this->CreateTempFile($file->name,$xml);
            $diff = $this->Interpret($file->name, $intScript);
            if (strcmp($this->interpretResult, 'OUTDIFF') ==0)
            {
                $IsOk=false;
                $this->outputHtml = HtmlGenerator::BuildOutputDiffBoxHtml($this->testName, $diff);
            }
            else if ($this->interpretResult)
            {
                $IsOk=true;
                $this->outputHtml = HtmlGenerator::BuildOkTestBoxHtml($this->testName);
            }
            else if (!$this->interpretResult)
            {
                $IsOk=false;
                $this->outputHtml = HtmlGenerator::BuildErrTestBoxHtml($this->testName, $this->parserResult , $this->expectedReturnCode);
            }

        }
        else
        {
            $IsOk=false;
            $this->outputHtml = HtmlGenerator::BuildErrTestBoxHtml($this->testName, $this->parserResult , $this->expectedReturnCode);
        }
        return $IsOk;
    }

    private function Parse($path, $parser)
    {
        $out="";
        exec("php5.6 $parser <$path.src 2> /dev/null", $out, $this->parserResult);
        $this->CheckReturnCode($path);
        return $out;
    }

    function CreateTempFile($name,$content)
    {
        file_put_contents("$name.temp", $content);
    }


    private function Interpret($path, $interpreter)
    {
        $code=array();
        exec("python3.6 $interpreter --source=$path.temp < $path.in 2> /dev/null", $code, $this->parserResult);
        $this->CheckReturnCode($path);

        if ($this->parserResult == 0)
        {
            $inputFile = implode("\n",$code);
            $inputFile .= "\n";
            file_put_contents("$path.temp", $inputFile);
            $diff=array();
            exec("diff $path.out $path.temp", $diff, $this->parserResult);
            if ($this->parserResult != 0)
            {
                $this->interpretResult = "OUTDIFF";
            }
        }
        if (file_exists("$path.temp"))
        {
            unlink("$path.temp");
        }

        return $diff;
    }

    private function CheckReturnCode($path)
    {
        $this->expectedReturnCode = file_get_contents("$path.rc");
        $this->interpretResult = $this->expectedReturnCode == $this->parserResult;

        $this->testName = preg_replace('/^.*\//','',$path);
    }
}

?>