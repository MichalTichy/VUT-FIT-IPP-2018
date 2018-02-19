<?php

interface IValidator
{
    public function Validate($input);

    protected function Is($input);
}
