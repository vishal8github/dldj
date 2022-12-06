//SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract Counter{
    string private name;
    uint private count;     //this is state variable...means this variable value will store at blockchain directly

    constructor(string memory _name, uint _initialCount){
        name = _name;
        count = _initialCount;
    }

    function increament() public returns (uint newCount){
        count += 1;       //count = count + 2;
        return count;
    }

    function decreament() public returns (uint newCount){
        count -= 1;       //count = count + 2;
        return count;
    }

    function getCount() public view returns (uint){
        return count;
    }

    function getName() public view returns (string memory currentName){
        return name;
    }

    function setName(string memory _newName) public returns (string memory newName){
        name = _newName;
        return name;
    }
}