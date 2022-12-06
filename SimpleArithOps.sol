//SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Calculator{
    uint ans;

    constructor() {
        ans = 0;
    }

    function getAns() view public returns(uint){
        return ans;
    }

    function add(uint num1, uint num2) public{
        ans = num1 + num2;
    }

    function subtract(uint num1, uint num2) public{
        ans = num1 - num2;
    }

    function multiply(uint num1, uint num2) public{
        ans = num1 * num2;
    }

    function divide(uint num1, uint num2) public{
        ans = num2 / num1;
    }
}
