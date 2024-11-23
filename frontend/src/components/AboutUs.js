import React from 'react';
import styled from 'styled-components';
import { motion } from 'framer-motion';

const AboutContainer = styled.div`
  padding: 50px 20px;
  background-color: #27ae60;
  color: white;
  text-align: center;
`;

const Cards = styled.div`
  display: flex;
  justify-content: center;
  gap: 20px;
  flex-wrap: wrap;
`;

const Card = styled(motion.div)`
  background: white;
  color: #145a32;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 300px;

  &:hover {
    transform: translateY(-10px);
    transition: 0.3s ease;
  }
`;

const AboutUs = () => (
  <AboutContainer id="about">
    <h2>About Us</h2>
    <Cards>
      <Card initial={{ opacity: 0, scale: 0.8 }} animate={{ opacity: 1, scale: 1 }} transition={{ duration: 0.5 }}>
        <h3>Our Mission</h3>
        <p>Connecting authors and readers to create amazing stories.</p>
      </Card>
      <Card initial={{ opacity: 0, scale: 0.8 }} animate={{ opacity: 1, scale: 1 }} transition={{ duration: 0.5, delay: 0.3 }}>
        <h3>Our Vision</h3>
        <p>Empowering creativity and collaboration through technology.</p>
      </Card>
    </Cards>
  </AboutContainer>
);

export default AboutUs;
