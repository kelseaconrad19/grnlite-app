import React from 'react';
import { useNavigate } from 'react-router-dom';
import styled from 'styled-components';

const SignInContainer = styled.div`
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

const SignInOptions = styled.div`
  display: flex;
  gap: 20px;
  margin-bottom: 30px;
`;

const OptionButton = styled.button`
  background-color: #27ae60;
  color: white;
  padding: 15px 30px;
  font-size: 1.2rem;
  border-radius: 5px;
  cursor: pointer;
  width: 200px;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: #2ecc71;
  }
`;

const BackToHome = styled.button`
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

const SignIn = () => {
  const navigate = useNavigate();

  const handleNavigation = (role) => {
    // Navigate to the secondary sign-in page with the role
    navigate(`/sign-in/${role}`);
  };

  return (
    <SignInContainer>
      <Logo src="/assets/Grn Lite Logo.png" alt="Grn Lite Logo" />
      <h1>Sign In</h1>
      <SignInOptions>
        <OptionButton onClick={() => handleNavigation('author')}>Author</OptionButton>
        <OptionButton onClick={() => handleNavigation('reader')}>Reader</OptionButton>
        <OptionButton onClick={() => handleNavigation('editor')}>Editor</OptionButton>
      </SignInOptions>
      <BackToHome onClick={() => navigate('/')}>Back to Home</BackToHome>
    </SignInContainer>
  );
};

export default SignIn;
