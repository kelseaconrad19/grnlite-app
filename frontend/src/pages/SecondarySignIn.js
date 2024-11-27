import React, { useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import styled from 'styled-components';

// Styled-components for styling the page
const SecondarySignInContainer = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f4f4f4;
  text-align: center;
`;

const Logo = styled.img`
  height: 100px;
  margin-bottom: 30px;
`;

const Form = styled.form`
  display: flex;
  flex-direction: column;
  gap: 15px;
  width: 300px;
`;

const Label = styled.label`
  text-align: left;
  width: 100%;
  font-size: 1rem;
  margin-bottom: 5px;
  color: #333;
`;

const Input = styled.input`
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
`;

const SignInButton = styled.button`
  background-color: #27ae60;
  color: white;
  padding: 15px;
  font-size: 1.2rem;
  border-radius: 5px;
  cursor: pointer;
  width: 100%;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: #2ecc71;
  }

  &:disabled {
    background-color: #95a5a6;
    cursor: not-allowed;
  }
`;

const BackToSignIn = styled.button`
  margin-top: 20px;
  background-color: #145a32;
  color: white;
  padding: 10px 20px;
  font-size: 1rem;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: #27ae60;
  }
`;

const ErrorMessage = styled.p`
  color: red;
  font-size: 0.9rem;
`;

const SecondarySignIn = ({ setUser }) => {
  const { role } = useParams(); // Get the role from the URL
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false); // Track form submission
  const navigate = useNavigate();

  console.log('Role:', role); // Check if the role is correct

  const validateForm = () => {
    if (!email || !password) {
      setError('Please fill in all fields.');
      return false;
    }
    if (!email.includes('@')) {
      setError('Please enter a valid email address.');
      return false;
    }
    if (password.length < 6) {
      setError('Password must be at least 6 characters long.');
      return false;
    }
    setError('');
    return true;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!validateForm()) return;

    setIsSubmitting(true); // Disable button while submitting

    try {
      // Log the email, password, and role to check the values
      console.log('Email:', email);
      console.log('Password:', password);
      console.log('Role:', role);

      // Simulate API authentication (use this for testing before real API)
      const response = await simulateAuthentication(email, password, role);
      
      if (response.success) {
        // Set the user role and navigate to the dashboard
        setUser({ role, email });
        navigate(`/${role}-dashboard`); // Redirect to the respective dashboard
      } else {
        setError('Authentication failed. Please try again.');
      }
    } catch (err) {
      setError('An error occurred. Please try again later.');
    } finally {
      setIsSubmitting(false); // Re-enable button after submission
    }
  };

  // Simulate API authentication (replace with real API call)
  const simulateAuthentication = (email, password, role) => {
    return new Promise((resolve) => {
      setTimeout(() => {
        if (role === 'author' && email === 'author@example.com' && password === 'password123') {
          resolve({ success: true });
        } else if (role === 'reader' && email === 'reader@example.com' && password === 'password123') {
          resolve({ success: true });  
        } else {
          resolve({ success: false });
        }
      }, 1000); // Simulate API delay
    });
  };

  return (
    <SecondarySignInContainer>
      <Logo src="/assets/Grn Lite Logo.png" alt="Grn Lite Logo" />
      <h1>Sign In as {role.charAt(0).toUpperCase() + role.slice(1)}</h1>
      <Form onSubmit={handleSubmit}>
        {error && <ErrorMessage>{error}</ErrorMessage>}
        <div>
          <Label htmlFor="email">Email</Label>
          <Input
            id="email"
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div>
          <Label htmlFor="password">Password</Label>
          <Input
            id="password"
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <SignInButton type="submit" disabled={isSubmitting}>
          {isSubmitting ? 'Signing In...' : 'Sign In'}
        </SignInButton>
      </Form>
      <BackToSignIn onClick={() => navigate('/sign-in')}>Back to Sign In</BackToSignIn>
    </SecondarySignInContainer>
  );
};

export default SecondarySignIn;
