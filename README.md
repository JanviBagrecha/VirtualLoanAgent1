# Virtual Loan Agent

## Overview
Virtual Loan Agent is a platform designed to simplify the process of finding, comparing, and calculating loans offered by multiple banks. This project was developed between May 2023 and June 2023 with the aim of providing users with a user-friendly interface to explore various loan options.

## Features
- **Backend Development**: The platform is built using Python and Django to ensure a robust backend that handles various functionalities seamlessly.
- **Database Management**: SQL is employed for efficient and effective management of the database, ensuring smooth data handling.
- **Loan Information**: Users can access comprehensive information about available bank loans. The platform filters loan options based on interest rates, loan terms, and eligibility criteria to match user requirements.
- **Loan Categories**: Loans are classified into categories like personal, business, home, vehicle, and student for easy navigation and specific search results.
- **Loan Calculator**: To assist users in making informed decisions, a user-friendly loan calculator is integrated. This tool allows for effortless comparisons between different loan options, empowering users to make well-informed financial decisions.
- **Admin Panel**: Django's admin panel is utilized, featuring a login and signup page. In the admin panel, administrators have access to the entire database containing information on all banks and their interest rates for various loan categories. Operations like create, add, update, edit, or delete can be performed here.
  ![image](https://github.com/JanviBagrecha/VirtualLoanAgent1/assets/111588269/8e591e3d-1728-4a65-83f2-563277269f17)


## Technologies Used
- **Python**: Used for the core functionality and backend development.
- **Django**: Framework utilized for creating a robust and scalable web application.
- **SQL**: Employed for efficient database management.

## Setup Instructions
To set up the Virtual Loan Agent project locally, follow these steps:
1. Clone the repository from [repository_link].
2. Install the necessary dependencies using `pip install -r requirements.txt`.
3. Configure the database settings in `settings.py`.
4. Run migrations to set up the database schema: `python manage.py makemigrations` followed by `python manage.py migrate`.
5. Start the development server: `python manage.py runserver`.

## Usage
- Access the platform via a web browser.
- Users can input their loan requirements (interest rate, loan term, eligibility) to view a curated list of available loans categorized under personal, business, home, vehicle, and student loans.
- Utilize the loan calculator feature to compare and calculate different loan options.
- Admins can log in to the Django admin panel to access and manage the entire database of banks, their interest rates, and loan categories.

## Support or Contact
For any inquiries or support regarding the Virtual Loan Agent project, please contact janvi.bagrecha@gmail.com
