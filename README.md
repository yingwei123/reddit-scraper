# Reddit Comments to Table Converter

This application converts Reddit post comments into a structured table format. It uses Python Flask for the backend and React for the frontend.

---

## Prerequisites

- Python 3.x
- Node.js and npm
- Reddit API credentials

---

## Installation

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Create a .env file in the backend directory with the following variables:
```
CLIENT_ID=your_reddit_client_id
CLIENT_SECRET=your_reddit_client_secret
REDIRECT_URI=http://localhost:8001/callback
TOKEN_URL=https://www.reddit.com/api/v1/access_token
GRANT_TYPE=password
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password
```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
### Frontend Setup
1. Navigate to the frontend directory
```bash
    cd frontend
```
2. Create a .env file in the frontend directory with the following content
   ```bash
   REACT_APP_API_BASE_URL="http://localhost:8001"
   ```
3. Install the required npm packages
   ```bash
   npm install
   ```  
4. Build the frontend
   ```bash
   npm run build
   ```

### Running the Application
1. Start the Flask backend server (from the backend directory)
   ```bash
   python main.py
   ```

The application will be available at http://localhost:8001.

Note: The python server will serve the most recent built frontend static files. To modify frontend code, you will need to run `npm run build` again. If you're developing the frontend, you can run `npm run start` to run the frontend server at http://localhost:3000.

### Usage
Open your browser and navigate to http://localhost:8001.
Enter a Reddit post URL in the input field.
Example URL format: https://www.reddit.com/r/CompetitiveTFT/comments/1gxghkw/keep_augment_stats_fair/
The application will fetch the comments and display them in a table format.

### Note:
Make sure to keep your Reddit API credentials secure and never commit them to version control.
You can create your own Reddit API credentials [here](https://www.reddit.com/prefs/apps).
