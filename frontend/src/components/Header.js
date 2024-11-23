import React from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom'; // Import useNavigate
import styled from 'styled-components';

const HeaderContainer = styled.header`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 50px;
  background-color: #145a32;
  color: white;
`;

const Logo = styled.img`
  height: 50px;
  cursor: pointer; /* Add pointer cursor to indicate clickability */
`;

const NavLinks = styled.nav`
  display: flex;
  gap: 20px;
`;

const NavLink = styled.a`
  color: white;
  text-decoration: none;
  font-weight: bold;
  transition: color 0.3s ease;

  &:hover {
    color: #2ecc71;
  }
`;

const Button = styled.button`
  background-color: #2ecc71;
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 1rem;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: #27ae60;
  }
`;

const Header = () => {
  const location = useLocation(); // Use location to determine current route
  const navigate = useNavigate(); // Use navigate hook

  // Function to handle logo click and redirect to home page
  const handleLogoClick = () => {
    navigate('/'); // This will navigate to the homepage
  };

  return (
    <HeaderContainer>
      <Logo 
        src="/assets/Grn Lite Logo.png" 
        alt="Grn Lite Logo" 
        onClick={handleLogoClick} // Handle logo click
      />
      {/* Only render links if we're on the homepage */}
      {location.pathname === "/" && (
        <NavLinks>
          <NavLink href="#features">Features</NavLink>
          <NavLink href="#about">About Us</NavLink>
          <NavLink href="#contact">Contact Us</NavLink> 
          <Link to="/sign-in">
            <Button>Sign In</Button>
          </Link>
          <Link to="/sign-up">
            <Button>Sign Up</Button>
          </Link>
        </NavLinks>
      )}
    </HeaderContainer>
  );
};

export default Header;
