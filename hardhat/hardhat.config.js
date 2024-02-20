require("@nomicfoundation/hardhat-toolbox");

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.8.24",
  networks: {
    hardhat: {
      accounts: [
        {
          // Аккаунт Owner. Первый аккаунт берется по умолчанию как signer
          privateKey: '9494a16261b41ba75d897cbbd246c836b091faacceeb2b149a4946eb3cfa428b',
          balance: '10000000000000000000000',
        },
        {
          // Tom
          privateKey: 'd2dd35918b87728877fa31b6ba8f907f0d609c9c6a63722928cdd22c9205735f',
          balance: '10000000000000000000000',
        },
        {
          // Max
          privateKey: 'd814f891b8dc18f9e6e7e3326230bc7edc3cee66957c215a2d15c7646996e5e1',
          balance: '10000000000000000000000',
        },
        {
          // Jack
          privateKey: '4dcda45c42bda724b55e7d1281f4c9d3978314bb2f6b2ac540ebc0398148df89',
          balance: '10000000000000000000000',
        },
        {
          // Account 2
          privateKey: 'ac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80',
          balance: '10000000000000000000000',
        },
      ]
    },
  }
};
