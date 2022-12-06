//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract requireExample{
    uint256 input;
    address sender;

    function some_state_changing_fn (uint256 _input) public returns (bool success)
    {
    sender = msg.sender;
    require(_input >= 100, "input should be greater or equals to 100");
    input = _input;
    success = true;
    }
}