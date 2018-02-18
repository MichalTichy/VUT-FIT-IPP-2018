<?php
interface IInstruction
{
    public function __construct($instructionTextRepresentation);
    public function ToXmlElement();
}
