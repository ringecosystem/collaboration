## Creating a Treasury Proposal

Your proposal should address a problem, outline a goal, give a detailed account of how you will
reach that goal, and include any ongoing maintenance needs. As much as possible, you should itemize
the tasks to be completed so fees can be evaluated and milestones can be followed.

### Announcing the Proposal

To minimize storage on-chain, proposals don't contain contextual information. When a user submits a
proposal, they will need to find an off-chain way to explain the proposal:

- Use platforms like [SubSquare](https://darwinia2.subsquare.io/) to initiate discussion with the community. They also offer
  a gauge poll to capture the community sentiment before submitting an on-chain referendum.

Spreading the word about the proposal's explanation to the community is ultimately up to the
proposer. Before submitting the proposal on-chain, it is required to do temperature check on [forum](https://github.com/orgs/darwinia-network/discussions) first.

:::

### Submit Treasury Proposal Preimage

The example below shows how to create a [preimage](../general/glossary#preimage) for a transaction
that requests 100 DOT from Treasury.

- Navigate to [Polkadot-JS UI > Governance > Preimages](https://cloudflare-ipfs.com/ipns/dotapps.io/?rpc=wss%3A%2F%2Frpc.darwinia.network#/preimages)
  and then click on Add Preimage.
- Select the account which will be used to submit the preimage.
- Choose `treasury` pallet in the "propose" dropdown and the `spend(amount, beneficiary)`call
- Enter the DOT amount.
- Enter the AccountID of the beneficiary (which has a verified on-chain identity).
- Submit preimage
- Sign and submit the transaction by paying the specified transaction fees.

:::info Preimage Submission Deposit

A deposit is required for the preimage to be stored on chain. The preimage deposit is proportional
to the amount of information stored within the preimage. Ensure you have enough account
balance to pay for the submission deposit and the transaction fees.

:::

After successful submission of the preimage, it is displayed on Polkadot-JS UI > Governance >
Preimages page. Every preimage is associated with a unique preimage hash. Take a note of this preimage hash, which is required to submit a referendum.

### Submit a Treasury Track Referendum

The example below shows how to submit a Treasury track referendum.

- Navigate to [Polkadot-JS UI > Governance > Referenda](https://cloudflare-ipfs.com/ipns/dotapps.io/?rpc=wss%3A%2F%2Frpc.darwinia.network#/referenda)
  and then click on Submit proposal.
- Select the account which will be used to submit the proposal.
- Choose the appropriate submission track.
- Enter the preimage hash of the treasury spend transaction.(If the preimage exists on-chain, the
  preimage length box is automatically populated)
- Click on Submit proposal.
- Sign and submit the transaction.

Once your submission is executed, your referendum will appear under your chosen track on the
Polkadot-JS UI [referenda page](https://cloudflare-ipfs.com/ipns/dotapps.io/?rpc=wss%3A%2F%2Frpc.darwinia.network#/referenda).

### Reference:
https://wiki.polkadot.network/docs/learn-guides-treasury