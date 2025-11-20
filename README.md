
# Multi-Tool Agent Test: Currency Conversion Assistant

A demonstration project showcasing Google's Agent Development Kit (ADK) with multi-tool agent capabilities for currency conversion with transaction fee calculations.

## Overview

This project implements a smart currency conversion assistant that combines multiple specialized tools:
- **Payment Method Fee Lookup** - Retrieves transaction fees for different payment methods
- **Exchange Rate API** - Gets real-time currency exchange rates
- **Calculation Agent** - A specialized Python code generator for mathematical computations
- **Root Agent** - Orchestrates the workflow between all tools

## Features

- 🔄 Currency conversion from EUR to other currencies
- 💳 Transaction fee calculation based on payment method
- 🧮 Automated Python code generation for complex calculations
- 🔧 Multi-tool agent architecture using Google's ADK
- 💬 Conversational AI interface using Gemini 2.5 Flash Lite

## Prerequisites

- Python 3.8+
- Google ADK access
- ExchangeRatesAPI.io account (free tier)
- Gemini API access

## Installation

1. Clone the repository:
```bash
git clone https://github.com/TeddyM1975/multi_tool_agent_test.git
cd multi_tool_agent_test
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the project root with:
```
EXCHANGE_API_KEY=your_exchangeratesapi_key
GOOGLE_API_KEY=your_gemini_api_key
```

## API Limitations

**Important Note**: Due to using the free tier of ExchangeRatesAPI.io, this implementation currently only supports converting **from EUR** to other currencies. The base currency is hardcoded to EUR in the `get_exchange_rate` function.

Future plans include migrating to a different API provider with more flexible free tier options.

## Project Structure

```
multi_tool_agent_test/
├── agent.py              # Main agent implementation
├── requirements.txt      # Python dependencies
├── .env                 # Environment variables (create this)
└── README.md           # This file
```

## Available Tools

### 1. Payment Method Fee Lookup
Returns transaction fees for supported payment methods:
- Platinum Credit Card: 2%
- Gold Debit Card: 3.5%
- Bank Transfer: 1%

### 2. Exchange Rate API
Fetches real-time exchange rates from EUR to target currencies using ExchangeRatesAPI.io

### 3. Calculation Agent
A specialized agent that generates Python code for mathematical computations, ensuring accurate calculations without manual arithmetic.

## Usage Example

The agent can handle queries like:
- "Convert 100 EUR to USD using platinum credit card"
- "How much is 500 EUR in GBP with bank transfer fees?"
- "Convert 250 EUR to JPY using gold debit card"

## Technical Details

- **Framework**: Google Agent Development Kit (ADK)
- **LLM Model**: Gemini 2.5 Flash Lite
- **Session Management**: In-memory session service
- **Code Execution**: Built-in code executor
- **API Integration**: ExchangeRatesAPI.io for currency data

## Development Notes

This project serves as a test bed for:
- Multi-tool agent orchestration
- Tool context management
- Agent-to-agent communication
- Error handling in tool chains
- Session persistence strategies

## Future Enhancements

- [ ] Migrate to more flexible currency API
- [ ] Add support for multiple base currencies
- [ ] Implement database persistence for sessions
- [ ] Add more payment methods and fee structures
- [ ] Create web interface for the agent
- [ ] Add historical exchange rate tracking

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for suggestions and bug reports.

## License

This project is open source. Please check the repository for specific licensing information.

## Disclaimer

This is a demonstration project for testing Google's ADK capabilities. The exchange rates and fee structures are for illustrative purposes and may not reflect real-world values.
```
