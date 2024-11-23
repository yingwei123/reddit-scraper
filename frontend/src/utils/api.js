import axios from 'axios';

const apiClient = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL || 'http://localhost:8001', // Adjust the base URL as needed
  headers: {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
  },
  withCredentials: true,
});

// Response interceptor to handle responses globally
apiClient.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    // Handle errors globally
    return Promise.reject(error);
  }
);

// Utility function for making GET requests
export const getRequest = async (url, params) => {
  try {
    const response = await apiClient.get(url, { params });
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

// Utility function for making POST requests
export const postRequest = async (url, data) => {
  try {
    const response = await apiClient.post(url, data);
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

// Utility function for making PUT requests
export const putRequest = async (url, data) => {
  try {
    const response = await apiClient.put(url, data);
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

// Utility function for making DELETE requests
export const deleteRequest = async (url) => {
  try {
    const response = await apiClient.delete(url);
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

// Centralized error handling
const handleError = (error) => {
  console.error('API call failed. ', error);
  throw error; // Re-throw the error to be caught by calling function if necessary
};