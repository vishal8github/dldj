// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;


contract Operations{
    uint num1;
    uint num2;

    function firstNumber(uint a) public{
        num1 = a;
    }

    function secondNumber(uint b) public{
        num2 = b;
    }

    function add() view public returns(uint){
        return num1 + num2;
    }

    function subtract() view public returns(uint){
        return num1 - num2;
    }

    function multiply() view public returns(uint){
        return num1 * num2;
    }

    function divide() view public returns(uint){
        return num1 / num2;
    }
}