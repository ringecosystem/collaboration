# Offchain Subnames on Darwinia Chain

## Project Description

This project aims to implement an offchain subnames solution for the 'darwinia.eth' Ethereum Name Service (ENS) domain but keeps the subname records on Darwinia Chain. 

It leverages the EIP-3668 specification to enable efficient and cost-effective management of subname-address mappings off the Ethereum mainnet. By storing these mappings on Darwinia Chain, the project offers a scalable approach to handle a large number of subdomains without incurring high gas fees.

The solution utilizes a customized OffchainResolver contract on Ethereum, which works with a gateway service connected to the Darwinia Chain. This setup allows for seamless resolution of subnames (e.g., 'foo.darwinia.eth') while maintaining the security and decentralization benefits of the ENS.

<!-- Key features of the project include:
1. Offchain storage of subname-address mappings on Darwinia Chain
2. Integration with ENS on Ethereum using EIP-3668 for secure offchain data retrieval
3. A gateway service to facilitate communication between Ethereum and Darwinia Chain
4. User-friendly UIs for subname registration, update, and resolution.
5. Admin UI for subname management. -->

This project addresses the need for efficient subdomain management within the Darwinia ecosystem, as outlined in the RFP (https://github.com/ringecosystem/collaboration/issues/61), and demonstrates the potential for cross-chain interoperability in domain name services.

### This project will benefit the Darwinia ecosystem in the following ways:

1. It will provide a more efficient and cost-effective way to manage subdomains on the Darwinia Chain, reducing the need for users to pay high gas fees on Ethereum.
2. It will enhance the usability of the 'darwinia.eth' domain by allowing users to register, update, and resolve subnames with reduced costs and improved performance.
3. It will demonstrate the potential for cross-chain interoperability in domain name services, opening up new possibilities for collaboration and innovation within the Darwinia ecosystem.

## Team

- Aki Wu([wuminzhe](https://github.com/wuminzhe))  
  A full stack developer focused on the web3 space. He has been working on darwinia ecosystem for a long time.

## Team Code Repos

- https://github.com/wuminzhe/offchain-resolver  
  This is the mono-repo for this project. All the code related is put here.

## Development Roadmap

### Milestone 1

This milestone is to implement the basic functionality of offchain subnames. 

Estimated Duration: 2 ~ 4 weeks

Cost: 1 ETH

Address: 0x2Da8ccfe0dD2165B8d939eaBf4E3697C4Adb6FDd

#### Tasks:

1. Implement a ERC-3668 compatible OffchainResolver contract on Ethereum.   
2. Implement a DarwiniaSubnameRegistry contract on Darwinia Chain.
3. Implement a gateway to facilitate communication between Ethereum and Darwinia Chain.
4. Contracts audit with devs from Darwinia community.
5. Deploy the contracts to testnets to do testing.
6. Write documentation.

#### Deliverables:

- A ERC-3668 compatible OffchainResolver contract.
- A DarwiniaSubnameRegistry contract.
- A gateway implementation.
- Deployment related
  - Documentation of deployment process. 
  - Deployment scripts.
  - Verified contracts on testnets.
- Contracts audit report.
- Documentation of deployed addresses and how to use it.

### Milestone 2

This milestone is to implement the normal users perspective UI for subname registration, removal, transfer, etc.

Estimated Duration: 2 ~ 4 weeks

Cost: 1 ETH

Address: 0x2Da8ccfe0dD2165B8d939eaBf4E3697C4Adb6FDd

#### Tasks:

1. Implement a sophiscated wallet connect logic.
2. Implement a dashboard for subname management.
3. Implement subname registration, removal, transfer.

#### Deliverables:

- A working deployed instance of the UI.
- Dockerfile and scripts for deployment.
- Documentation of how to deploy and run the UI.

### Milestone 3

This milestone is to implement the admin UI for subname management.

Estimated Duration: 2 ~ 4 weeks

Cost: 1 ETH

Address: 0x2Da8ccfe0dD2165B8d939eaBf4E3697C4Adb6FDd

#### Tasks:

1. Implement a admin dashboard for subname management.
2. Implement subnames list view.
2. Implement subname removal, transfer.

#### Deliverables:

- A working deployed instance of the admin UI.
- Dockerfile and scripts for deployment.
- Documentation of how to deploy and run the admin UI.

### Additional Information

I have two ideas for future work:

* The first is to implement a gas-free subdomain online service. This would allow anyone to use the service to create their own subdomain-based applications, similar to what Uniswap has done with uni.eth.   
  The service is similar to what https://namestone.xyz/ provides.

* The second is to implement a comprehensive subdomain solution. This service is not only needed by Darwinia, but also by other blockchains. Furthermore, even non-EVM chains could benefit from such a solution.