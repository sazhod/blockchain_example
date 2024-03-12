// https://eips.ethereum.org/EIPS/eip-20
// SPDX-License-Identifier: MIT
pragma solidity 0.8.24;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract TokenContract is ERC20 {
    address Owner = 0x0C8EfAe6C1BfB983DA37F1d41904234f3C4c2488;
    address Tom = 0x6D0102592b1bB09D88f7eB910Ae5234Ba3861985;
    address Max = 0x49DcB0339C7D3ECFa3cCFC217a064E954AFE8A0d;
    address Jack = 0xE91F2Da19168a83CFa14c7d4422ff8f60fe330Cf;

    constructor() ERC20("Professional", "PROFI"){
        decimals();
        _mint(msg.sender, 1000000 * 10 ** decimals());

        transfer(Owner, 100000*10**decimals());
        transfer(Tom, 200000*10**decimals());
        transfer(Max, 300000*10**decimals());
        transfer(Jack, 400000*10**decimals());
    }

    function decimals() public pure override returns (uint8) {
        return 6;
    }
}