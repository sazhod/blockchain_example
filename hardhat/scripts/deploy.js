// We require the Hardhat Runtime Environment explicitly here. This is optional
// but useful for running the script in a standalone fashion through `node <script>`.
//
// You can also run a script with `npx hardhat run <script>`. If you do that, Hardhat
// will compile your contracts, add the Hardhat Runtime Environment's members to the
// global scope, and execute the script.
const hre = require("hardhat");

async function main() {
  const currentTimestampInSeconds = Math.round(Date.now() / 1000);
  const unlockTime = currentTimestampInSeconds + 60;

  const lockedAmount = hre.ethers.parseEther("0.001");

  const lock = await hre.ethers.deployContract("Lock", [unlockTime], {
    value: lockedAmount,
  });

  await lock.waitForDeployment();

  console.log(
    `Lock with ${ethers.formatEther(
      lockedAmount
    )}ETH and unlock timestamp ${unlockTime} deployed to ${lock.target}`
  );
}

// We recommend this pattern to be able to use async/await everywhere
// // and properly handle errors.
// main().catch((error) => {
//   console.error(error);
//   process.exitCode = 1;
// });

async function main1() {
  // const token_contract = await hre.ethers.deployContract("Lock", [unlockTime], {
  //   value: lockedAmount,
  // });
  // console.log(her.ethers.)
  const token_contract = await hre.ethers.deployContract("TokenContract");
  console.log(token_contract)
  console.log("Contract address");

  const token_contract2 = await hre.ethers.deployContract("TokenContract2");
  console.log(token_contract2);
  console.log("Contract address");
}


// main1().catch((error) => {
//   console.error(error);
//   process.exitCode = 1;
// });

async function main2() {
  const [deployer] = await hre.ethers.getSigners();
  console.log('Deploying contracts with the account: ' + deployer.address);
  console.log(hre.ethers.version);
  // // Deploy First
  // const First = await ethers.getContractFactory('Lock');
  // const first = await First.deploy();

  // Deploy Second
  const First = await hre.ethers.getContractFactory('TokenContract');
  const first = await First.deploy();
  await first.waitForDeployment();
  
  console.log( "Second: " + first.address );
  console.log( "Second: " + first); 

  const Second = await hre.ethers.getContractFactory('TokenContract2');
  const second = await Second.deploy();
  second.waitForDeployment();
  
  console.log( "Second: " + second.address );
  console.log( "Second: " + second); 
}

main2()
  .then(() => process.exit())
  .catch(error => {
      console.error(error);
      process.exit(1);
})
