// SPDX-License-Identifier: MIT
pragma solidity >=0.5.0 <0.9.0;

import {ERC1155} from "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";


contract NftContract is ERC1155 {
    address public owner;
    constructor() ERC1155("http://localhost:5000/NFT/NFTS/{id}.json"){
        owner = msg.sender;
    }
    function mint(address to, uint id, uint amount) public {
        _mint(to, id, amount, "");
    }
}