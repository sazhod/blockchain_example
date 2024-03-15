// SPDX-License-Identifier: MIT
pragma solidity 0.8.24;

import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "./TokenContract.sol";

contract NftContract is ERC1155 {
    struct Auction {
        address owner;
        address bigAddress;
        uint256 bigValue;
        uint256 startValue;
        uint256 tokenid;
        uint256 timeStampEnd;
        bool isEnded;
    }

    TokenContract tokenContract;
    Auction[] public auctions;

    constructor(address _tokenContract)
        ERC1155("http://localhost:5000/NFT/NFTS/{id}.json")
    {
        tokenContract = TokenContract(_tokenContract);
        _mint(msg.sender, 1, 1, "");
    }
    function startAuction(uint _tokenId, uint _startValue, uint _timeStampEnd) public {
        require(balanceOf(msg.sender, _tokenId) >= 1, "You dont have this nft");

        _burn(msg.sender, _tokenId, 1);
        
        Auction memory newAuction = Auction({
            owner: msg.sender,
            bigAddress: address(0),
            bigValue: 0,
            startValue: _startValue,
            tokenid: _tokenId,
            timeStampEnd: _timeStampEnd,
            isEnded: false
        });
        
        auctions.push(newAuction);
    }
    function bid(uint _auctionId, uint value) public {
        Auction storage auction = auctions[_auctionId];

        require(auction.timeStampEnd > block.timestamp, "Auction has ended");
        require(auction.startValue < value, "Bid must be higher than start value");
        require(auctions[_auctionId].bigValue < value, "Bid must be higher than previous bid");
        require(tokenContract.allowance(msg.sender, address(this)) >= value, "Not enough allowance for ERC20 token");

        if (auction.bigAddress != address(0))
            tokenContract.transferFrom(address(this), auctions[_auctionId].bigAddress, auctions[_auctionId].bigValue);

        tokenContract.transferFrom(msg.sender, address(this), value);

        auctions[_auctionId].bigValue = value;
        auctions[_auctionId].bigAddress = msg.sender;
    }

    function endAuction(uint _auctionId) public {
        Auction storage auction = auctions[_auctionId];
        require(auction.timeStampEnd <= block.timestamp, "Auction has not ended yet");
        require(auction.owner == msg.sender, "Only the owner can end the auction");

        tokenContract.transferFrom(address(this), auctions[_auctionId].owner, auctions[_auctionId].bigValue);
        _mint(auctions[_auctionId].bigAddress, 1, 1, "");
        auctions[_auctionId].isEnded = true;
    }

    function createNft(address to, uint id, uint amount, bytes memory metadata) public {
        _mint(msg.sender, id, amount, "");
    }
}