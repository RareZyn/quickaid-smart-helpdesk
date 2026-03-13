<div align="center">

# QuickAid

![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Azure Functions](https://img.shields.io/badge/Azure_Functions-0062AD?style=for-the-badge&logo=azure-functions&logoColor=white)
![Azure Cosmos DB](https://img.shields.io/badge/Azure_Cosmos_DB-51A6ED?style=for-the-badge&logo=azure-cosmos-db&logoColor=white)

</div>

## Overview

QuickAid is a smart campus helpdesk application designed for university students and staff to submit issues, track requests, and receive timely support. A cloud-native application built on Microsoft Azure, QuickAid enables ticket submission, status tracking, automated notifications, and secure data management, while remaining scalable, cost-efficient, and deployment-ready under Azure Free Tier constraints.

This application was developed as a Capstone Project for the MyMahir Microsoft Developer programme.

## Features

- **Issue Submission**: A modern web form interface allowing users to quickly submit helpdesk tickets.
- **Ticket Tracking**: A secure endpoint enabling users to retrieve and check the status of their submitted tickets via their email addresses.
- **Automated Notifications**: Immediate email confirmations sent upon ticket submission, ensuring users are kept in the loop.
- **Persistent Data**: Secure and scalable ticket storage utilizing unique identifiers and accurate status tracking mechanisms.

## Architecture and Technology Stack

The project utilizes a decoupled client-server model, capitalizing on the scalability of serverless computing and managed cloud services.

### Frontend

- **Framework**: Next.js and React
- **Styling**: Tailwind CSS and custom UI components
- **Hosting**: Azure App Service

### Backend

- **Compute**: Azure Functions (Serverless architecture using Python)
- **Database**: Azure Cosmos DB (NoSQL)
- **Secrets Management**: Azure Key Vault
- **Communication**: SendGrid API for transactional emails
- **Telemetry & Monitoring**: Azure Application Insights (Optional diagnostic integration)

## Project Structure

```text
quickaid-smart-helpdesk/
├── docs/                 # Project documentation and specifications
├── frontend/             # Next.js web application
│   ├── app/              # Next.js App Router pages and layouts
│   ├── components/       # Reusable UI components
│   ├── lib/              # Utility functions
│   └── public/           # Static assets
└── README.md             # Project overview
```

## System Requirements

To run this project locally or deploy it to your own environment, you will need:

- An active **Microsoft Azure** subscription (Free Tier is sufficient)
- A **SendGrid** account for email integration API keys
- **Node.js** (v18 or higher) for frontend development
- **Python** (v3.9 or higher) and Azure Functions Core Tools for backend development

## Getting Started

### Local Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install the necessary dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```
4. Access the web interface at `http://localhost:3000`.

### Backend Configuration (Azure Functions)

_Note: The backend implementation relies on an Azure Functions Python worker. Full configuration steps will be added once the backend directory is initialized._

### Azure Deployment

1. **Database**: Provision an Azure Cosmos DB (Core NoSQL) account.
2. **Secrets**: Create an Azure Key Vault and store infrastructure connection strings and SendGrid API keys.
3. **Backend**: Publish the Python functions to an Azure Function App. Ensure it has access policies granting read permissions to Key Vault.
4. **Frontend**: Deploy the Next.js application to Azure App Service, specifying environment variables pointing to your Azure Functions endpoint.

## Evaluation and Assessment

This project was built to meet the evaluation criteria of the MyMahir programme:

- Successful deployment of both Frontend and Backend components.
- Demonstrated working features (Submit and Retrieve Tickets).
- Proper integration of SendGrid for email notifications.
- Rigorous adherence to security principles using Azure Key Vault.

## License

This project was created for educational purposes as part of the MyMahir Microsoft Developer programme Capstone.
