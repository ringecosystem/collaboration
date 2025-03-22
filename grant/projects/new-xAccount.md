## New Darwinia XAccount UI

### Project Description

XAccount is an assisted action generation tool for cross-chain governance, which can be used with governance tools like [Tally](https://www.tally.xyz/gov/ringdao/proposals). You can specify the action you wish to execute in your governance proposal, and once it is passed, the action will be executed. However, actions can sometimes be complex, especially when involving cross-chain operations, creating a barrier for participants to join the governance. This tool aims to solve this problem by providing a UI inspired by [Impersonator](https://impersonator.xyz/). It allows users to simulate Dapp interactions and capture user operation calls, which can then be wrapped with cross-chain capabilities and copied to external governance platforms. This tool has two parts: Create XAccount and Generate Action.

This project is to implement the UI part of Darwinia XAccount.

### Team

- Snoopy1412([@snoopy1412](https://github.com/snoopy1412))

### Team Code Repos

- [https://github.com/ringecosystem/xaccount-ui](https://github.com/ringecosystem/xaccount-ui)

### Development Roadmap

### **Phase 1**

Estimated Duration: 6 weeks

Cost: 2500 USD

Address: 0x3d6d656c1bf92f7028Ce4C352563E1C363C58ED5

#### Tasks:

1. **User Interface Design and Responsive Implementation**

   - **Objective**: Create an intuitive, modern user interface, optimizing the user experience across different devices and screen sizes.
   - **Tech Stack**: Utilize Next.js and React framework combined with TailwindCSS and shadcn/ui to support responsive design and high customizability.

2. **Blockchain Interaction and Web3 Integrationn**

   - **Web3 Tech Stack Integration**: Use the Wagmi and viem library to simplify interactions with EVM-compatible blockchains, given its concise API and good compatibility with React.
   - **Wallet Connection and Blockchain Interaction Optimization**: Use @rainbow-me/rainbowkit to further simplify the wallet connection process and enhance the blockchain interaction experience.

3. **DApp Access and Transaction Capture Mechanisms**

   XAccount adopts the design philosophy of Impersonator.xyz, offering two transaction capture methods to accommodate different DApp interaction scenarios:

   - **WalletConnect Mode**

     - Direct DApp connection through WalletConnect protocol
     - Support for QR code scanning and deep linking connection
     - Real-time transaction request capture within WalletConnect sessions

   - **iframe Embedding Mode**
     - Load target DApps within a secure iframe environment
     - Rely on Gnosis Safe SDK for transaction capture and processing
     - Maintain original DApp interface while monitoring transactions

4. **Cross-chain Account Creation and Remote Operation**

   - **Cross-chain Account Creation**

     - Support creating remotely controlled accounts on target chains
     - Ensure secure cross-chain account control

   - **Remote Operation Execution**
     - Support selection of deployed XAccounts for operation execution
     - Support cross-chain transaction simulation and execution
     - Generate governance-compatible operation actions in JSON format
