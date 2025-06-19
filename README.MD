# 🚽 FlushMart

Welcome to **FlushMart**! An e-commerce platform dedicated to all things toilet-related: from premium thrones and bidets to toilet paper and plumbing accessories.

All good ideas are born on the toilet… right? 

FlushMart was dreamed up exactly there, clean in code and concept. Whether you're outfitting a home bathroom or stocking up your plumbing business, this project is built to showcase how a focused niche and solid software architecture can flush out boring design.

## 🧱 Project Structure

This project is a **work-in-progress** implementation inspired by **Hexagonal Architecture** (also known as Ports and Adapters). That means:

- Domain logic is decoupled from frameworks and infrastructure
- Application services sit between the domain and external layers (like Django views and database models)
- Easier testing, better modularity, and room for long-term scalability

## 🚀 Setup Instructions

1. **Clone the repository**  

   ```git clone https://github.com/your-username/flushmart.git```

2. **Install dependencies**

    ```pip install -r requirements.txt```

3. **Install development dependencies**

    Install development dependencies to run tests, code formatting and so on:

    ```pip install -r requirements-dev.txt```

4. **Run the development server**

    ```python manage.py runserver```

## 🧪 Tests

The project has integration tests for the database interaction and then unit-tests for the services and later the domain layer. Pytest is used for testing. 

Tests in this project are always in a tests folder in each layer where tests are in place.

To run all the tests run the ```pytest``` command. To run specific tests add the folder path behind the ```pytest``` command.

## ✅ Current Features

As the project has only very recently started and is a work in progress as for now then there is only one feature, that is, displaying list of products on the home page. 

More features coming soon. See the next section.


## 🧭 Future Features

- 🏷️ Category filtering
- 🔐 User registration and login  
- 🛒 Shopping cart functionality  
- 📦 Order management and checkout flow   
- 🔍 Search functionality
- 🚚 Shipping options and payment integrations
- 🎨Improved visual UI
