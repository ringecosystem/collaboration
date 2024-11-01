# MsgScan UI

## Description

Msgscan is a browser for msgport messages, designed to provide developers and users with a tool to view message content, as well as the source and destination of the messages. Additionally, as msgscan supports various messaging protocols, it needs to support the display of protocol information for different messaging protocols.

## Team

- Snoopy1412([@snoopy1412](https://github.com/snoopy1412))

## Code Repos

- [https://github.com/snoopy1412/msgscan-ui](https://github.com/snoopy1412/msgscan-ui)

## Development Roadmap

### Phase 1

* Estimated Duration: 1.5 week
* Cost: 600 USD
* Address: 0x3d6d656c1bf92f7028Ce4C352563E1C363C58ED5

### Tasks

1. Message List Interface

   Develop the Message List interface using React, combined with the Shadcn framework and TailwindCSS. This interface will feature a table that displays essential transaction data such as timestamp, transaction type, sender, and recipient addresses.

2. Detailed Message View

   Upon user interaction or a search by transaction hash (tx hash), navigate to a detailed page that provides comprehensive information including the full transaction path, its current status, and relevant metadata.

3. Multidimensional Filtering

   Implement multiple filtering options that allow users to refine transactions based on criteria such as transaction status, time range, source address, and destination address. This functionality will be facilitated through a filtering panel where users can specify their preferences.

4. Sorting Functionality

   Enable users to sort the Message List by attributes such as Age or Time Spent. This will be achieved by adding clickable column headers in the table, allowing users to choose their sorting criteria.

5. Dashboard Statistics

   Display key statistics at the top of the interface, such as the total number of transactions, number of active transactions, and distribution across networks/protocols. This will be handled by a dedicated statistics component that updates dynamically based on the current list state.

6. Testnets and Mainnet Data Switching

   Implement a switching mechanism that allows users to toggle between data from Testnets and the Mainnet. This functionality will typically be provided through a toggle button or dropdown menu, enabling the user to select and retrieve data from the appropriate backend service.

7. Search Functionality for Source tx or msgid

   Incorporate a search box that enables users to find specific transactions by source transaction or message identifier (msgid). The search box will support full-text search, optimizing both response time and accuracy.

8. List Pagination

   Implement pagination for the Message List using the `useQuery` hook from React Query. This feature will include frontend pagination controls, allowing users to navigate through different pages of transactions.

9. Data Refresh Interface

   Utilize React's state management and the Fetch API to periodically retrieve the latest data from the backend, ensuring that users consistently have access to the most current transaction information. This will be accomplished by establishing a timed refresh mechanism to maintain data freshness.

### Phase 2

* Estimated Duration: 1.5 week
* Cost: 600 USD
* Address: 0x3d6d656c1bf92f7028Ce4C352563E1C363C58ED5

### Objective

Enhance the aesthetics and user experience of MsgScan, including responsive design for mobile device support, implementing PWA features, improving page animations, detail optimizations, and enhancing SEO.

### Tasks

1. UI Design Optimization

   - Redesign and optimize interface elements and color themes based on UI/UX designer's blueprints to enhance visual appeal and consistency of the user interface.
   - Optimize user interaction design to ensure intuitive and easy-to-understand user operations.

2. Mobile Support

   - Implement responsive design to ensure MsgScan provides a good browsing experience across various screen sizes and devices, especially on mobile devices.
   - Test and adjust the responsiveness and accuracy of touch interactions.

3. PWA Support

   - Develop a Progressive Web Application (PWA) that allows users to add the website to their home screen and access it as a regular app.
   - Implement offline capabilities, enabling the app to operate without an internet connection and ensuring fast loading times.

4. Enhanced Animations

   - Use the Framer Motion library to add interactive animation effects to page elements, such as transitions, response feedback, and dynamic loading effects, to enhance user experience.
   - Ensure animations are smooth and do not affect website performance.

5. Detail Optimization

   - Make detailed adjustments and optimizations to existing features, including tweaks to buttons, icons, fonts, and layouts.

6. SEO Enhancement

   - Optimize website content and structure for search engines to improve visibility and increase organic traffic.
   - Implement best SEO practices such as optimizing meta tags, improving site speed, and ensuring mobile-friendliness.
