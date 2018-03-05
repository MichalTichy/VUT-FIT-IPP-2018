<?php
interface IProgram
{
    public function __construct(array $instructions);
    public function ConvertToXml();
    public function GetCountOfInstructions();
}
