# Darwinia Grant Template

## Project name

Darwinia Crab Faucet

### Project Description

Please provide the following:

- To create a faucet for Crab Network.
- An indication of why this project is good for the Darwinia ecosystem. It will help any developers working on Darwinia's testnet Crab to get CRINGs for testing purposes.
- I'll deploy the frontend and backend spearatley and a subdomain of Darwinia could be dedicated for the integration

### Team

I have been working in the Polkadot's ecosystem for over a year now and have several projects in different capacities under my belt

- [Furqan Ahmed](https://furqan.me)

### Legal Structure

Name of Legal Entity executing the project: Furqan Ahmed

### Team Code Repos

- <https://github.com/nblogist>

### Development Roadmap

The project will have 3 Milestones:

1. Frontend Development

2. Backend Development

3. Integration, Deployment & testing

### Frontend Development - Time: 0.5 week (400 USDT)

At the end of this milestone a simple frontend will be created on ReactJs using TypeScript with a simple request button and an address input control

### Backend Development - Time: 2.5 weeks (1500 USDT)

Backend will be created by following steps:

- []  Setup express server
- []  DDOS protected on express side
- []  Setup environment variables to be stored in `.env` that configure
  - []  The amount of token to be paid on each request
    - []  The rate-limit parameters for accounts testing
    -[]  The mnemonic/private key of account paying the token on new requests.
- []  Create a route that pays token to an address
  - []  Receives the address and chain identifier as input
    - []  Checks the address is valid against that chain
    - []  Make use of chain as a string to verify account validity
    - []  Integrate FingerPrinting of Express
    - []  Checks that this address hasn't requested tokens on this chain in the last ***X*** minutes defined by the rate-limit parameters in `.env`
    - []  Checks that this IP hasn't request tokens on this chain in the last ***X*** minutes defined by the rate-limit parameters in `.env`
    - []  If checks fail, return an error response to the client.
    - []  Sets up keyring with mnemonic/private key from `.env`
    - []  Pays token to the address passed into the route
    - []  Records the (address, chain) in local DB
    - []  Records the (IP address, chain) in a local DB
    - []  Sends back a successful response

### Integration, Deployment & testing - Time: 1 week (600 USDT)

In the Final Milestones the product from above 2 milestones would be integrated to work to gather in a fully functional faucet for crab network and tested for expected behavior.

### Additional Information

-
