# Selenium Login Test Automation

## About This Project

This automated testing framework was developed as a learning project to explore Selenium WebDriver with Python and Firefox, focusing on creating robust, maintainable test automation code. The project showcases industry-standard practices for test automation, including proper error handling, logging, screenshot capture, and structured test organization. While fully functional for testing login scenarios, this project represents a journey in mastering test automation principles and Python development.

## Features

- **Comprehensive Test Coverage**: Tests valid login, invalid username, invalid password, and empty field scenarios
- **Detailed Logging**: Complete action logging with timestamps and structured output to file
- **Screenshot Capture**: Automatic screenshots for both successful and failed test cases with descriptive naming
- **Structured Architecture**: Object-oriented design with separate classes for test data and test execution
- **Multiple Test Execution**: Runs all test scenarios in sequence with summary reporting
- **Error Handling**: Robust exception handling with detailed error logging
- **Firefox Integration**: Optimized for Mozilla Firefox with GeckoDriver

## Tech Stack

### Core Technologies
- Python 3.x
- Selenium WebDriver
- Mozilla Firefox
- GeckoDriver

### Key Libraries
- `selenium` - Web automation framework
- `logging` - Comprehensive test logging
- `time` - Test timing and delays

## Installation

### Prerequisites
- Python 3.x (Download from python.org)
- Mozilla Firefox browser
- GeckoDriver for Firefox

### Setup

1. **Python Installation**:
   ```bash
   # Download Python from python.org
   # During installation, check "Add Python to PATH"
   # Verify installation
   python --version
   ```

2. **Install Selenium**:
   ```bash
   pip install selenium
   ```

3. **Setup GeckoDriver**:
   - Download GeckoDriver from [Mozilla/GeckoDriver releases](https://github.com/mozilla/geckodriver/releases)
   - Extract the executable file
   - Add GeckoDriver to your system PATH or place in project folder

4. **Clone and Run**:
   ```bash
   git clone [your-repository-url]
   cd selenium-login-tests
   python login_test.py
   ```

## Project Structure

```
selenium-login-tests/
├── login_test.py           # Main test automation script
├── selenium_test.log       # Generated log file (created on run)
├── screenshots/            # Generated screenshots directory
│   ├── login-success-*.png # Successful login screenshots
│   ├── login-failed-*.png  # Failed login screenshots
│   └── login-error-*.png   # Error case screenshots
└── README.md              # Project documentation
```

## Test Scenarios

The automation suite covers four critical login scenarios:

1. **Valid Login Test**
   - Uses correct username and password
   - Expects successful authentication
   - Screenshot: `login-success-valid_credentials.png`

2. **Invalid Username Test**
   - Uses incorrect username with correct password
   - Expects authentication failure
   - Screenshot: `login-failed-invalid_username.png`

3. **Invalid Password Test**
   - Uses correct username with incorrect password
   - Expects authentication failure
   - Screenshot: `login-failed-invalid_password.png`

4. **Empty Fields Test**
   - Submits form with empty username and password
   - Expects authentication failure
   - Screenshot: `login-failed-empty_inputs.png`

## Code Architecture

### TestData Class
Manages test credentials and data:
```python
class TestData:
    def load_credentials():
        return {
            'valid': ('tomsmith', 'SuperSecretPassword!'),
            'invalid_username': ('Tomsmith', 'SuperSecretPassword!'),
            'invalid_password': ('tomsmith', 'SuperSecretPassword'),
            'empty': ('', '')
        }
```

### LoginTest Class
Main test execution class with methods for:
- Browser initialization and setup
- Individual test case execution
- Result verification and logging
- Screenshot capture
- Test cleanup

## Logging Features

The framework provides comprehensive logging including:
- **Timestamp tracking** for all actions
- **Detailed step logging** for each test operation
- **Result verification** with expected vs actual outcomes
- **Error tracking** with full exception details
- **Test summary** with pass/fail status for all scenarios

### Sample Log Output:
```
2025-05-23 13:33:10,551 - INFO - Going to Webpage https://the-internet.herokuapp.com/login
2025-05-23 13:33:10,567 - INFO - Clearing the Username Field
2025-05-23 13:33:10,595 - INFO - Sending Keys tomsmith to Username Field
2025-05-23 13:33:12,789 - INFO - Expected Result: Login Successful
2025-05-23 13:33:12,794 - INFO - Login was Successful
2025-05-23 13:33:12,812 - INFO - Test Result: SUCCESS
```

## Usage

### Running All Tests
```bash
python login_test.py
```

### Running Individual Tests
```python
# Create test instance
test_runner = LoginTest()

# Run specific test
result = test_runner.test_valid_login()
print(f"Test result: {result}")

# Clean up
test_runner.cleanup()
```

## Key Learning Outcomes

This project demonstrates several important test automation concepts:

- **Object-Oriented Test Design**: Structured approach using classes and methods
- **Explicit Waits**: Using WebDriverWait for reliable element interactions
- **Comprehensive Logging**: Industry-standard logging practices for debugging and reporting
- **Screenshot Documentation**: Visual proof of test execution and results
- **Error Handling**: Robust exception management for stable test execution
- **Test Data Management**: Centralized test data organization

## Future Enhancements

- [ ] Add support for multiple browsers (Chrome, Edge, Safari)
- [ ] Implement Page Object Model design pattern
- [ ] Add HTML test report generation
- [ ] Include performance metrics and timing analysis
- [ ] Add configuration file for test parameters
- [ ] Implement parallel test execution
- [ ] Add integration with CI/CD pipelines
- [ ] Include accessibility testing checks

## Comparison: First vs Second Implementation

### Original Implementation
- Single test execution approach
- Basic error handling
- Limited logging capabilities
- Manual screenshot management

### Enhanced Implementation
- **Multiple test scenarios** executed in sequence
- **Comprehensive logging** with file output and structured formatting
- **Automatic screenshot capture** with descriptive naming conventions
- **Object-oriented architecture** for better code organization and maintainability
- **Robust error handling** with detailed exception tracking
- **Test summary reporting** for quick result analysis

## Contributing

This project welcomes contributions! Areas for improvement include:
- Additional test scenarios
- Cross-browser compatibility
- Performance optimizations
- Enhanced reporting features

## License

This project is licensed under the MIT License - feel free to use and modify for your learning and testing needs.

## Acknowledgments

- [Selenium Documentation](https://selenium-python.readthedocs.io/)
- [Mozilla GeckoDriver](https://github.com/mozilla/geckodriver)
- [Python Logging Documentation](https://docs.python.org/3/library/logging.html)
- [The Internet - Herokuapp Test Site](https://the-internet.herokuapp.com/)
