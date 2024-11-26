import React from 'react';
import { useNavigate } from 'react-router-dom';
import styled from 'styled-components';

const SignUpContainer = styled.div`
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
  cursor: pointer;
`;

const SignUpOptions = styled.div`
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

const SignUp = () => {
  const navigate = useNavigate();

  const handleNavigation = (role) => {
    navigate(`/sign-up/${role.toLowerCase()}`); // Redirects to secondary sign-up page based on role
  };

  return (
    <SignUpContainer>
      <Logo src="/assets/Grn Lite Logo.png" alt="Grn Lite Logo" onClick={() => navigate('/')} />
      <h1>Sign Up</h1>
      <SignUpOptions>
        <OptionButton onClick={() => handleNavigation('Author')}>Author</OptionButton>
        <OptionButton onClick={() => handleNavigation('Reader')}>Reader</OptionButton>
        <OptionButton onClick={() => handleNavigation('Editor')}>Editor</OptionButton> {/* New Editor Button */}
      </SignUpOptions>
      <BackToHome onClick={() => navigate('/')}>Back to Home</BackToHome>
    </SignUpContainer>
  );
};

export default SignUp;
