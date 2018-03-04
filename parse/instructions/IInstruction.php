<?php

foreach (glob("Validators/*.php") as $filename)
{
    require_once($filename);
}
interface IInstruction
{
    public function __construct($instructionTextRepresentation);
    public function ToXmlElement($XmlDocument);
}
