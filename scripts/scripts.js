function signout() {
    if (window.ethereum) {
      window.ethereum
        .request({
          method: "wallet_requestPermissions",
          params: [
            {
              eth_accounts: {},
            },
          ],
        })
        .then(() => {
            public_key = window.ethereum.selectedAddress;
            var base_url = window.location.origin;
            window.location.replace(base_url + "/?public_key="+public_key);
        });
    }
  }

  async function connectWalletwithMetaMask() {
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' })
    .catch((e) => {
    console.error(e.message)
    return
    })

    if (!accounts) { return }

    public_key = accounts[0]
    
    var base_url = window.location.origin;
    window.location.replace(base_url + "/?public_key="+public_key);
    
    }