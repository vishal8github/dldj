// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract  fac {

    function factorial(uint num) pure public returns(uint){
        uint fact = 1;
        uint i =1;
        while(i <= num){
            fact = fact * i;   
            i++;
        }
        return fact;
    }
}