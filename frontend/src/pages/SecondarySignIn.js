import React, { useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import styled from 'styled-components';

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

const SecondarySignIn = () => {
  const { role } = useParams();  // Get the role from the URL
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(`Sign-in as ${role} with email: ${email}`);
    // You can handle authentication here
    navigate(`/${role}-dashboard`);  // Redirect to respective dashboard (not implemented yet)
  };

  return (
    <SecondarySignInContainer>
      <Logo src="/assets/Grn Lite Logo.png" alt="Grn Lite Logo" />
      <h1>Sign In as {role.charAt(0).toUpperCase() + role.slice(1)}</h1>
      <Form onSubmit={handleSubmit}>
        <Input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <Input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <SignInButton type="submit">Sign In</SignInButton>
      </Form>
      <BackToSignIn onClick={() => navigate('/sign-in')}>Back to Sign In</BackToSignIn>
    </SecondarySignInContainer>
  );
};

export default SecondarySignIn;
