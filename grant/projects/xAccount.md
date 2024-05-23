## Darwinia xAccount UI

### Project Description

Darwinia xAccount is a component within Darwinia Msgport, acting as the cross-chain account abstraction. Your xAccount is uniquely controlled by your local address on the source chain. As an encapsulation of Darwinia Msgport's cross-chain capabilities, xAccount simplifies the user experience in executing cross-chain operations.

This project is to implement the UI part of Darwinia xAccount.

The ui prototype:

<img src="https://github.com/darwinia-network/collaboration/assets/1608576/fb307cf2-5de1-45f0-9cec-68447343a54a" style="width: 50%" alt="xAccount-UI"/>

### **Why is this project good for the Darwinia ecosystem**

Darwinia xAccount is built upon the Darwinia Msgport, which serves as Darwinia's flagship product. However, for individuals who aren't developers, having a suite of smart contracts without a user interface (UI) can be daunting. Therefore, this project aims to provide users, especially non-developers, with a more user-friendly experience.

Drawing inspiration from Gnosis Safe, which offers users an intuitive UI for utilizing a multi-sig account to interact with decentralized applications (dApps), xAccount UI seeks to provide a similar experience. With xAccount UI, users can seamlessly access any dApp on the remote chain using their xAccount, just like they would with a regular account.

### Team

- Snoopy1412([@snoopy1412](https://github.com/snoopy1412))

### Team Code Repos

- [https://github.com/snoopy1412/xAccount-ui](https://github.com/snoopy1412/xAccount-ui)

### Development Roadmap

### **Phase 1**

Estimated Duration: 8 weeks

Cost: 3500 USD

Address: 0x3d6d656c1bf92f7028Ce4C352563E1C363C58ED5

#### Tasks:

1. **User Interface Design and Responsive Implementation**

   - **Objective**: Create an intuitive, modern user interface, optimizing the user experience across different devices and screen sizes.
   - **Tech Stack**: Utilize the React framework combined with TailwindCSS and Shadcn UI to support responsive design and high customizability.

2. **Blockchain Interaction and Web3 Integrationn**

   - **Web3 Tech Stack Integration**: Use the Wagmi library to simplify interactions with EVM-compatible blockchains, given its concise API and good compatibility with React.
   - **Wallet Connection and Blockchain Interaction Optimization**: Use @rainbow-me/rainbowkit to further simplify the wallet connection process and enhance the blockchain interaction experience.

3. **dApp URL Management and Remote Account Functionality**

   - **dApp URL Management Interface**: Implement a user-friendly interface allowing users to add and manage dApp URLs, automatically fetching and storing dApp metadata (title, description, icon) to enhance user recognition and management capabilities.
   - **Remote Account Creation and Management**: Develop functionality allowing users to create remote accounts based on their local wallet addresses, supporting cross-chain operations and dApp interactions. Design clear user interfaces and processes to guide users in managing and using their remote accounts.

4. **iframe Within dApp Access, Interaction, and Cross-chain Operations**

   - **Accessing dApps via iframe**: Access target dApps through iframe technology, injecting the remote account address to enable user interaction using their remote account.
   - **Using xCreate for Cross-chain Account Creation**: Implement the xCreate function to facilitate the creation of cross-chain accounts. This function allows users to establish a remote account on a target chain from their local chain. The process involves specifying the target chain, the necessary parameters for account creation, and optionally, a recovery account for additional security. This functionality enhances the flexibility and reach of xAccount, enabling users to interact seamlessly across multiple blockchains.
   - **Contract Operation Mechanism and Cross-chain Operations**: Design mechanisms to ensure that contract operations within the iframe are smoothly taken over and executed by the remote account. Utilize Darwinia Msgport to monitor contract operations within the iframe, processing these operations through LCMP or ORMP protocols to enable cross-chain communication and contract calls. Ensure smooth operation execution and provide clear feedback to users.

5. **Historical Transaction Records and User Experience Optimization**

   - **Viewing Historical Transaction Records**: Develop a feature allowing users to view historical transaction records executed through xAccount, including cross-chain operations and transactions across different dApps. Design an intuitive interface to enhance the efficiency of record queries and user experience.
   - **Optimizing Contract Operation User Experience**: Design and implement superior UX/UI to guide users in conducting contract operations within the iframe using their remote account, including loading pages and feedback on operation status. Implement a transparent operation process, clearly informing users that contract operations are executed on Darwinia Msgport, thus enhancing user trust.
