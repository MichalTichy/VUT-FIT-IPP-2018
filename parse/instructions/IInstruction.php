<?php
interface IInstruction
{
    public function __construct(array $instructionTextRepresentation);
    public function ToXmlElement();
}
