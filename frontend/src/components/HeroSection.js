import React from 'react';
import styled from 'styled-components';
import { motion } from 'framer-motion';

const HeroContainer = styled.div`
  background-color: #27ae60;
  color: white;
  text-align: center;
  padding: 100px 20px;
`;

const Heading = styled(motion.h1)`
  font-size: 3rem;
  margin-bottom: 20px;
`;

const Subheading = styled(motion.p)`
  font-size: 1.5rem;
  margin-bottom: 40px;
`;

const HeroSection = () => (
  <HeroContainer>
    <Heading initial={{ opacity: 0, y: -50 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 1 }}>
      Welcome to Grn Lite
    </Heading>
    <Subheading initial={{ opacity: 0, y: 50 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 1, delay: 0.5 }}>
      By Authors, For Readers
    </Subheading>
  </HeroContainer>
);

export default HeroSection;
