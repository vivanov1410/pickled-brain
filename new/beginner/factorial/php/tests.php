<?php

require_once('library.php');

class TestFactorial extends PHPUnit_Framework_TestCase {

  public function test_factorial() {
    $this->assertEquals(1, factorial(1));
    $this->assertEquals(2, factorial(2));
    $this->assertEquals(6, factorial(3));
    $this->assertEquals(120, factorial(5));
  }

}